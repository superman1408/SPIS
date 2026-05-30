import math
from utils import constant


__version__ = "Free Span Analysis calculation version 0.0.2"

print(__version__)


def freeSpan_Analysis_calculation(frontendData):

    try:

        # ============================================================
        # INPUT DATA
        # ============================================================

        test_case = frontendData["Test_Case"]
        deflection_Criteria = frontendData["Deflection_Criteria"]

        PipeGeometry = {
            "Outer_Diameter": frontendData["Outer_Diameter"],             # m
            "Wall_Thickness": frontendData["Wall_Thickness"],             # m
            "Coating_Thickness": frontendData["Coating_Thickness"],       # m
            "Concrete_Thickness": frontendData["Concrete_Thickness"],     # m
        }

        Constant = {
            "Beta_Value": frontendData["Beta_Value"],
            "Gravity": constant["gravity"],                               # m/s²
            "Deflection_Factor": frontendData["Deflection_Factor"],
            "Moment_Factor": frontendData["Moment_Factor"]
        }

        MaterialProperty = {
            "Steel_density": constant["Steel_density"],                   # kg/m³
            "Coating_Density": frontendData["Coating_Density"],           # kg/m³
            "Concrete_Density": constant["Concrete_Density"],             # kg/m³
            "Seawater_Density": constant["density_seawater"],                   # kg/m³
            "Youngs_Modulus": constant["Youngs_Modulus"],                 # Pa
            "Yield_Strength": frontendData["Yield_Strength"],             # MPa
            "Air_Density": constant["Air_Density"],                       # jg/m³
            "Content_Density": frontendData["Content_Density"],           # kg/m³
        }

        Environment = {
            "Current_Velocity": frontendData["Current_Velocity"],         # m/s
            "Wave_Velocity": frontendData["Wave_Velocity"],               # m/s
        }

        Assumed_Span_Length = frontendData["Assumed_Span_Length"]         # m

        print("======================================================")
        print("FREE SPAN ANALYSIS STARTED")
        print("======================================================")

        print("Pipe Geometry:", PipeGeometry)
        print("Material Properties:", MaterialProperty)
        print("Environment:", Environment)
        print("Constants:", Constant)
        print("Test Case:", test_case)


        # Switch case for select test case condition

        match frontendData["Test_Case"]:
            case "Installation":
                Density = constant["Air_Density"]

            case "Hydrotest":
                Density = constant["Seawater_Density"]

            case "Operational": 
                Density = frontendData["Content_Density"]

            case _:
                raise ValueError(
                    f"Unknown Test_Case: {frontendData['Test_Case']}"
                )

        
        print("Seawater Density" , Density)




        # ============================================================
        # BASIC GEOMETRY
        # ============================================================

        OD = PipeGeometry["Outer_Diameter"]
        WT = PipeGeometry["Wall_Thickness"]
        T_coat = PipeGeometry["Coating_Thickness"]
        T_conc = PipeGeometry["Concrete_Thickness"]

        ID = OD - 2 * WT

        D_coat = OD + 2 * T_coat

        D_total = D_coat + 2 * T_conc

        # ============================================================
        # AREA CALCULATIONS
        # ============================================================

        A_internal = math.pi / 4 * ID**2

        A_steel = math.pi / 4 * (OD**2 - ID**2)

        A_coating = math.pi / 4 * (D_coat**2 - OD**2)

        A_concrete = math.pi / 4 * (D_total**2 - D_coat**2)

        A_outer_total = math.pi / 4 * D_total**2

        print("\n================ AREA CALCULATIONS ================")
        print("Internal Area:", A_internal, "m2")
        print("Steel Area:", A_steel, "m2")
        print("Coating Area:", A_coating, "m2")
        print("Concrete Area:", A_concrete, "m2")
        print("Total Outer Area:", A_outer_total, "m2")

        # Verification
        area_balance = (
            A_internal
            + A_steel
            + A_coating
            + A_concrete
        )

        print("Area Verification:", area_balance)

        # ============================================================
        # MASS CALCULATIONS
        # ============================================================

        m_internal = (
            A_internal
            * Density
        )

        m_steel = (
            A_steel
            * MaterialProperty["Steel_density"]
        )

        m_coating = (
            A_coating
            * MaterialProperty["Coating_Density"]
        )

        m_concrete = (
            A_concrete
            * MaterialProperty["Concrete_Density"]
        )

        m_total = (
            m_internal
            + m_steel
            + m_coating
            + m_concrete
        )

        m_buoyancy = (
            A_outer_total
            * Density
        )

        m_submerged = (
            m_total
            - m_buoyancy
        )

        submerged_weight = (
            m_submerged
            * Constant["Gravity"]
        )

        print("\n================ MASS CALCULATIONS ================")
        print("Internal Mass:", m_internal, "kg/m")
        print("Steel Mass:", m_steel, "kg/m")
        print("Coating Mass:", m_coating, "kg/m")
        print("Concrete Mass:", m_concrete, "kg/m")
        print("Total Mass:", m_total, "kg/m")
        print("Buoyancy Mass:", m_buoyancy, "kg/m")
        print("Submerged Mass:", m_submerged, "kg/m")
        print("Submerged Weight:", submerged_weight, "N/m")

        # ============================================================
        # L/D CHECK
        # ============================================================

        L_by_D = Assumed_Span_Length / OD

        if L_by_D < 140:
            LD_status = "PASS"
        else:
            LD_status = "FAIL"

        print("\n================ L/D CHECK ================")
        print("L/D Ratio:", L_by_D)
        print("L/D Status:", LD_status)

        # ============================================================
        # SECTION PROPERTIES
        # ============================================================

        I = (
            math.pi / 64
            * (
                OD**4
                - ID**4
            )
        )

        EI = (
            MaterialProperty["Youngs_Modulus"]
            * I
        )

        Z = I / (OD / 2)

        print("\n================ SECTION PROPERTIES ================")
        print("Moment of Inertia:", I, "m4")
        print("EI:", EI, "N.m2")
        print("Section Modulus:", Z, "m3")

        # ============================================================
        # DEFLECTION
        # ============================================================

        delta = (
            Constant["Deflection_Factor"]
            * submerged_weight
            * Assumed_Span_Length**4
        ) / (
            384
            * EI
        )
        # Beam deflection formula for uniformly distributed load: δ = (5 * w * L^4) / (384 * EI)
        # Condition:
        #| Criterion  | Meaning              |
        # | --------- | -------------------- |
        # | L/180     | Very flexible        |
        # | L/240     | Moderate             |
        # | L/360     | Typical              |
        # | L/500     | Strict               |
        # | L/1000    | Precision structures |


        delta_mm = delta * 1000
        
        allowable_deflection_mm = (Assumed_Span_Length * 1000) / deflection_Criteria

        if delta_mm < allowable_deflection_mm:
            Deflection_status = "PASS"
        else:
            Deflection_status = "FAIL"

        # print("\n================ DEFLECTION ================")
        # print("Deflection:", delta_mm, "mm")
        # print("Deflection Status:", Deflection_status)
        # print("Allowable Deflection:", allowable_deflection_mm, "mm")
        print("\n================ DEFLECTION ================")
        print(f"Actual Deflection     : {delta_mm:.2f} mm")
        print(f"Allowable Deflection  : {allowable_deflection_mm:.2f} mm")
        print(f"Deflection Status     : {Deflection_status}")

        # ============================================================
        # BENDING STRESS
        # ============================================================

        M = (
            submerged_weight
            * Assumed_Span_Length**2
        ) * Constant["Moment_Factor"]  # M = wL^2 / c, where c is the moment factor based on boundary conditions
        
        allowable_stress = (
            0.87
            * MaterialProperty["Yield_Strength"]
        )
        
        rho = (
            M / Z
        ) / 1e6

        unity_check = (
            rho
            / allowable_stress
        )

        if unity_check < 1:
            BendingStress_status = "SAFE"
        else:
            BendingStress_status = "UNSAFE"

        # if 10 <= rho <= 100:
        #     BendingStress_status = "SAFE"
        # else:
        #     BendingStress_status = "UNSAFE"

        print("\n================ BENDING STRESS ================")
        print("Moment:", M, "N.m")
        print("Stress:", rho, "MPa")
        print("Stress Status:", BendingStress_status)

        # ============================================================
        # NATURAL FREQUENCY
        # ============================================================

        if m_submerged <= 0:
            raise ValueError(
                "Submerged mass <= 0. Pipe is buoyant."
            )

        fn = (
            (Constant["Beta_Value"]**2)
            / (
                2
                * math.pi
                * Assumed_Span_Length**2
            )
        ) * math.sqrt(
            EI / m_submerged
        )

        print("\n================ NATURAL FREQUENCY ================")
        print("Natural Frequency:", fn, "Hz")

        # ============================================================
        # FLOW REGIME
        # ============================================================

        alpha = (
            Environment["Current_Velocity"]
            / (
                Environment["Current_Velocity"]
                + Environment["Wave_Velocity"]
            )
        )

        if alpha < 0.5:
            Flow_Regime_status = "Wave Dominated"

        elif alpha > 0.8:
            Flow_Regime_status = "Current Dominated"

        else:
            Flow_Regime_status = (
                "Mixed Wave-Current"
            )

        print("\n================ FLOW REGIME ================")
        print("Alpha:", alpha)
        print("Flow Regime:", Flow_Regime_status)

        # ============================================================
        # REDUCED VELOCITY
        # ============================================================

        V_r = (
            Environment["Current_Velocity"]
            / (
                fn * OD
            )
        )

        if V_r < 1:
            VIV_status = "No VIV"

        elif V_r <= 3:
            VIV_status = "Inline VIV"

        elif V_r <= 8:
            VIV_status = "Cross Flow VIV"

        else:
            VIV_status = "Severe VIV"

        print("\n================ VIV CHECK ================")
        print("Reduced Velocity:", V_r)
        print("VIV Status:", VIV_status)

        # ============================================================
        # FATIGUE
        # ============================================================

        SN_curve = [
            (8, 1.0e16),
            (10, 1.0e11),
            (15, 1.3e10),
            (20, 3.1e9),
            (25, 1.0e9),
            (26, 8.4e8),
            (30, 4.1e8),
            (40, 9.8e7),
            (50, 3.2e7)
        ]

        def get_SN_value(stress):

            for i in range(len(SN_curve) - 1):

                s1, n1 = SN_curve[i]
                s2, n2 = SN_curve[i + 1]

                if s1 <= stress <= s2:

                    log_n1 = math.log10(n1)
                    log_n2 = math.log10(n2)

                    log_n = (
                        log_n1
                        + (stress - s1)
                        * (log_n2 - log_n1)
                        / (s2 - s1)
                    )

                    return 10**log_n

            if stress < SN_curve[0][0]:
                return SN_curve[0][1]

            return SN_curve[-1][1]

        vibration_amplitude = 0.2 * OD

        curvature = (
            vibration_amplitude
            / Assumed_Span_Length**2
        )

        stress_range = (
            MaterialProperty["Youngs_Modulus"]
            * (OD / 2)
            * curvature
        ) / 1e6

        design_life_seconds = (
            100
            * 365
            * 24
            * 3600
        )

        N_cycles = (
            fn
            * design_life_seconds
        )

        SN_N = get_SN_value(stress_range)

        D_fat = (
            N_cycles
            / SN_N
        )

        if D_fat > 1:
            Fatigue_status = "FAIL"
        else:
            Fatigue_status = "PASS"

        print("\n================ FATIGUE ================")
        print("Stress Range:", stress_range, "MPa")
        print("Cycles:", N_cycles)
        print("SN Curve N:", SN_N)
        print("Fatigue Damage:", D_fat)
        print("Fatigue Status:", Fatigue_status)

        # ============================================================
        # ULS CHECK
        # ============================================================

        allowable_stress = (
            0.87
            * MaterialProperty["Yield_Strength"]
        )

        unity_check = (
            rho
            / allowable_stress
        )

        if unity_check < 1:
            ULS_status = "SAFE"
        else:
            ULS_status = "UNSAFE"

        print("\n================ ULS CHECK ================")
        print("Allowable Stress:", allowable_stress, "MPa")
        print("Unity Check:", unity_check)
        print("ULS Status:", ULS_status)

        # ============================================================
        # RESULT DICTIONARY
        # ============================================================

        result = {

            # ---------------------------------------------------
            # EXISTING UI KEYS (KEEP SAME)
            # ---------------------------------------------------

            "LD_Check": LD_status,

            "Steel_Area": A_steel,

            "Outer_Diameter_after_Coating": D_coat,

            "Submerged_Mass": m_submerged,

            "Natural_Frequency": fn,

            "Outer_Diameter_after_Concrete": D_total,

            "Submerged_Weight": submerged_weight,

            "alpha": alpha,

            "Flow_Regime_status": Flow_Regime_status,

            "Coating_Area": A_coating,

            "Concrete_Coating": (
                m_concrete + m_coating
            ),

            "Bending_Stiffness": I,

            "Reduced_velocity": V_r,

            "VIV_Status": VIV_status,

            "Concrete_Area": A_concrete,

            "Total": m_total,

            "Bending_Stiffness_EI": EI,

            "D_fat": D_fat,

            "SN_Curve_for_N": SN_N,

            "Number_of_cycle_n": N_cycles,

            "Fatigue_status": Fatigue_status,

            "Outer_Diameter_including_coating_concrete": D_total,

            "Buoyancy": m_buoyancy,

            # ---------------------------------------------------
            # IMPORTANT
            # Keep same key name expected by UI
            # ---------------------------------------------------

            "Deflection_value": delta_mm,

            "Deflection_status": Deflection_status,

            "stress_rho": rho,

            "BendingStress_status": BendingStress_status,

            "Total_Outer_Area": A_outer_total,

            "Bending_Stress_Moment": M,

            "Allowable_Stress": allowable_stress,

            "Unity_check": unity_check,

            "ULS_status": ULS_status,

            "SN_curve": SN_curve,

            "Stress_Range": {
                "Vibration_Amplitude": vibration_amplitude,
                "Curvature": curvature,
                "Stress": stress_range,
            },
        }

        print("\n======================================================")
        print("FREE SPAN ANALYSIS COMPLETED")
        print("======================================================")

        return result

    except Exception as e:

        print("ERROR OCCURRED:", e)

        return {
            "status": "FAILED",
            "message": str(e)
        }
