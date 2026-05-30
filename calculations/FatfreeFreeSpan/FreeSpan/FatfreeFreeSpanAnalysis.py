# import math
# from utils import constant


# __version__ = "Free Span Analysis calculation version: 0.0.1"

# print(__version__)


# def freeSpan_Analysis_calculation(frontendData):
    
    
#     try:
        
#         test_case = frontendData["Test_Case"]

#         PipeGeometry = {
#             "Outer_Diameter":   frontendData["Outer_Diameter"], #Frontend
#             "Wall_Thickness":   frontendData["Wall_Thickness"], #Frontend
#             "Coating_Thickness":  frontendData["Coating_Thickness"], #Frontend
#             "Concrete_Thickness": frontendData["Concrete_Thickness"], #Frontend
#         }

#         Constant = {
#             "Beta_Value":frontendData["Beta_Value"],
#             "Gravity": constant["gravity"],
#         }

#         MaterialProperty = {
#             "Steel_density": constant["Steel_density"],
#             "Coating_Density": frontendData["Coating_Density"], #Frontend
#             "Concrete_Density": constant["Concrete_Density"],
#             "Water_Density": constant["Water_Density"],
#             "Youngs_Modulus": constant["Youngs_Modulus"],
#             "Yield_Strength": frontendData["Yield_Strength"],
#             "Content_Density": frontendData["Content_Density"],
#         }

#         Environment = {
#             "Current_Velocity": frontendData["Current_Velocity"], #Frontend
#             "Wave_Velocity": frontendData["Wave_Velocity"], #Frontend
#         }
        
#         print("Pipe Geometry: ", PipeGeometry)
#         print("Material Properties: ", MaterialProperty)
#         print("Environment: ", Environment)
#         print("Test Case: ", test_case)
#         print("Constants: ", Constant)
        
#         print("****************************************Calculation started for test case: ", test_case, "****************************************")

     
        


#         SN_curve = [
#             (8, 1.0e16),
#             (10, 1.0e11),
#             (15, 1.3e10),
#             (20, 3.1e9),
#             (25, 1.0e9),
#             (26, 8.4e8),
#             (30, 4.1e8),
#             (40, 9.8e7),
#             (50, 3.2e7)
#         ]

#         def get_SN_value(stress):
#             for i in range(len(SN_curve) - 1):
#                 s1, n1 = SN_curve[i]
#                 s2, n2 = SN_curve[i + 1]

#                 if s1 <= stress <= s2:
#                     # Linear interpolation (log scale recommended)
#                     log_n1 = math.log10(n1)
#                     log_n2 = math.log10(n2)

#                     log_n = log_n1 + (stress - s1) * (log_n2 - log_n1) / (s2 - s1)

#                     return 10 ** log_n

#             # Outside range
#             if stress < SN_curve[0][0]:
#                 return SN_curve[0][1]
#             else:
#                 return SN_curve[-1][1]
            

        

#         Assumed_Span_Length = frontendData["Assumed_Span_Length"]


#         Vibration_Amplitude = 0.2 * PipeGeometry["Outer_Diameter"]

#         Curvature = Vibration_Amplitude/Assumed_Span_Length**2

#         Stress_from_curvature = (
#             MaterialProperty["Youngs_Modulus"]
#             * (PipeGeometry["Outer_Diameter"] / 2)
#             * Curvature
#         ) / 10**6


#         # ---- THEN STORE ----
#         Stress_Range = {
#             "Vibration_Amplitude": Vibration_Amplitude,
#             "Curvature": Curvature,
#             "Stress": Stress_from_curvature
#         }
#         print("****************Stress Range Calculation****************")
#         print("Stress Range: ", Stress_Range)




#         # ---- CALCULATIONS FIRST ---- 


#         def LD_Check():
            
#             Assumed_Span_Length_by_Outer_Diameter = Assumed_Span_Length / PipeGeometry["Outer_Diameter"]
#             print("****************Length by Outer Diameter Check****************")
#             print("Assumed Span Length by Outer Diameter: ", Assumed_Span_Length_by_Outer_Diameter)

#             if Assumed_Span_Length_by_Outer_Diameter < 140:
#                 L_by_D_check = "PASS"
                
#             else:
#                 L_by_D_check = "FAIL"
                
#             print("L/D Check Result: ", L_by_D_check)

#             return L_by_D_check

        
#         # ✅ ADD THIS BLOCK HERE
#         ld_result = LD_Check()

#         if ld_result == "FAIL":
#             ld_resultStatus = "L/D failed stopping further calculations"

#             return {
#                 "LD_Check": "FAIL",
#                 "message": "L/D ratio not acceptable as L/D < 140. No further calculations done."
#             }

#         def Steel_Area():
#             Steel_Area = math.pi/4 * ((PipeGeometry["Outer_Diameter"])**2-(PipeGeometry["Outer_Diameter"] - 2 * PipeGeometry["Wall_Thickness"])**2)
#             print("****************Steel Area Calculation****************")
#             print("Steel Area of Pipe:",  Steel_Area)
#             return Steel_Area

#         Steel_Area()


#         def Outer_Diameter_including_coating_concrete():
#             D_Outer = frontendData["Outer_Diameter"] + 2 * (frontendData["Coating_Thickness"] + frontendData["Concrete_Thickness"])
#             print("****************Outer Diameter including Coating and Concrete Calculation****************")
#             print("Outer Diameter including coating and concrete:", D_Outer)
#             return D_Outer

#         Outer_Diameter_including_coating_concrete()

#         def Total_Outer_Area():
#             A_Outer = math.pi/4 * (Outer_Diameter_including_coating_concrete())**2
#             print("****************Total Outer Area Calculation****************")
#             print("Total Outer Area:", A_Outer)
#             return A_Outer

#         Total_Outer_Area()

#         def Outer_Diameter_after_Coating():
#             D_Coat = PipeGeometry["Outer_Diameter"]+2*(PipeGeometry["Coating_Thickness"])
#             print("****************Outer Diameter after Coating Calculation****************")
#             print("Outer Diameter after coating:", D_Coat)
#             return D_Coat

#         Outer_Diameter_after_Coating()

#         def Coating_Area():
#             A_Coat = math.pi/4*((Outer_Diameter_after_Coating()**2)-PipeGeometry["Outer_Diameter"]**2)
#             print("****************Coating Area Calculation****************")
#             print("Coating Area:", A_Coat)
#             return A_Coat

#         Coating_Area()

#         def Outer_Diameter_after_Concrete():
#             D_cwc = Outer_Diameter_after_Coating() + 2 *PipeGeometry["Concrete_Thickness"]
#             print("****************Outer Diameter after Concrete Calculation****************")
#             print("Outer Diameter after concrete:", D_cwc)
#             return D_cwc

#         Outer_Diameter_after_Concrete()

#         def Concrete_Area():
#             A_cwc = math.pi/4*(Outer_Diameter_after_Concrete()**2 - Outer_Diameter_after_Coating()** 2)
#             print("****************Concrete Area Calculation****************")
#             print("Concrete Area:", A_cwc)
#             return A_cwc

#         Concrete_Area()


#         # STEP 2
        
#         def Internal_Area():
#             ID = PipeGeometry["Outer_Diameter"] - 2 * PipeGeometry["Wall_Thickness"]

#             A_internal = math.pi / 4 * (ID ** 2)

#             return A_internal
        
#         def Content_Mass():
#             try:
#                 m_content = Internal_Area() * MaterialProperty["Content_Density"]
#                 return m_content
#             except Exception as e:
#                 print(f"Error occurred while calculating content mass: {e}")
#                 return 1  # Return 0 or some default value if there's an error

#         def Mass_per_meter_Steel():
#             m_s = MaterialProperty["Steel_density"] * Steel_Area()
#             return m_s

#         Mass_per_meter_Steel()


#         def Concrete_Coating():
#             m_c = Concrete_Area() * MaterialProperty["Concrete_Density"] + MaterialProperty["Coating_Density"] * Coating_Area()
            
#             return m_c

#         Concrete_Coating()
        
        

#         def Total():
#             # m_total = Mass_per_meter_Steel() + Concrete_Coating()
#             m_total = (
#                 Mass_per_meter_Steel()
#                 + Concrete_Coating()
#                 + Content_Mass()
#             )
           
#             return m_total

#         Total()


#         # STEP 3.5

#         def Buoyancy():
#             Water_Mass_m_water = Total_Outer_Area() * MaterialProperty["Water_Density"]
            
#             return Water_Mass_m_water

#         Buoyancy()


#         def Submerged_Mass():
#             m_eff = Total() - Buoyancy()
            
#             return m_eff

#         Submerged_Mass()

#         def Submerged_Weight():
#             w = Submerged_Mass() * Constant["Gravity"]
            
#             return w

#         Submerged_Weight()

#         def Bending_Stiffness():
#             Moment_of_Inertia = math.pi/64 * (
#                 PipeGeometry["Outer_Diameter"]**4 -
#                 (PipeGeometry["Outer_Diameter"] - 2 * PipeGeometry["Wall_Thickness"])**4
#             )
            
            
#             # EI = MaterialProperty["Youngs_Modulus"] * Moment_of_Inertia
            
#             return Moment_of_Inertia

#         Bending_Stiffness()


#         def Bending_Stiffness_EI():
#             EI = MaterialProperty["Youngs_Modulus"] * Bending_Stiffness()
            
            
#             return EI

#         Bending_Stiffness_EI()


#         # def Bending_Stiffness():
#         #     Moment_of_Inertia = math.pi/64*(PipeGeometry["Outer_Diameter"]**4 - ((PipeGeometry["Outer_Diameter"] - 2 * PipeGeometry["Wall_Thickness"])**4))
#         #     print("Moment_of_Inertia", Moment_of_Inertia)
            

#         #     E_into_I = MaterialProperty["Youngs_Modulus"] * Moment_of_Inertia
#         #     print("E_into_I", E_into_I)

#         #     return Moment_of_Inertia, E_into_I


#         def Deflection():

#             E_into_I = Bending_Stiffness_EI()
#             delta = (5* Submerged_Weight() * Assumed_Span_Length**4)/(384 * E_into_I)
            

            

#             if delta < 25:
#                 Deflection_result = "PASS"
#             else:
#                 Deflection_result = "FAIL"

            

#             return delta, Deflection_result


#         Deflection()

#         delta, def_status = Deflection()


#         # step 6

#         def Bending_Stress_Moment():
#             M = (Submerged_Weight() * (Assumed_Span_Length**2))/8
#             print("Bending_Stress_Moment M in N-m: ", M)
            
#             return M

#         Bending_Stress_Moment()

#         def Section_Modulus():
#             D = PipeGeometry["Outer_Diameter"]
#             I = Bending_Stiffness()
            
#             Z = I / (D / 2)
#             print("Section_Modulus Z in m^3: ", Z)
#             return Z


#         Section_Modulus()

#         def Stress_rho():
#             M = Bending_Stress_Moment()   
#             Z = Section_Modulus()  
#             # σ = M / Z  
#             rho = (M / Z) / 1e6
#             print("Bending Stress (rho) in MPa: ", rho)
#             # return rho
#             # Srho = Stress_rho()

#             if 10 <= rho <= 100 :
#                 BendingStress_Result = "SAFE"
#             else:
#                 BendingStress_Result = "UNSAFE"

#             return rho, BendingStress_Result


#         Stress_rho()


#         rho, BendingStress_Result = Stress_rho()


 

#         #step 7

#         def Natural_Frequency():
#             # natural_frequency = Submerged_Mass() * (Assumed_Span_Length**4)
#             # print("natural_frequency", natural_frequency)

#             # return natural_frequency

#             m_eff_into_L = Submerged_Mass() * (Assumed_Span_Length**4)
            
#             return m_eff_into_L

#         Natural_Frequency()

#         def Natural_Frequency_fn():

#             mL = Natural_Frequency() 

#             if mL <= 0:
#                 raise ValueError("Submerged mass is negative → Pipe is buoyant → Invalid condition")

#             EI_by_mL = Bending_Stiffness_EI() / mL
            

#             f_n = 0.5 * math.sqrt(EI_by_mL)

            

#             return f_n                                                                                        

#         Natural_Frequency_fn()


# #--------------------------------------------------Natural frequency for beta--------------------------------------------------------------

#         def Natural_Frequency_for_beta():

#             fn_beta = (Constant["Beta_Value"])**2 / (2 * math.pi * (Assumed_Span_Length)**2 ) * (math.sqrt(Bending_Stiffness_EI()/Submerged_Mass()))


#             return fn_beta
        

#         Natural_Frequency_for_beta()


#         # Step 8
#         def Flow_Regime():
#             alpha = Environment["Current_Velocity"] / (Environment["Current_Velocity"] + Environment["Wave_Velocity"])
            
#             if alpha < 0.5 :
#                 Flow_Regime_result = "Wave dominated"

#             elif alpha >0.8 :
#                 Flow_Regime_result = "Current dominated"
            
#             else:
#                 Flow_Regime_result = "MIXED (Combined Wave-Current Regime)"

#             # print("Flow_Regime_result", Flow_Regime_result)

#             return alpha, Flow_Regime_result

#         Flow_Regime()

#         alpha, Flow_Regime_status = Flow_Regime()





#         #step 9
#         def Reduced_Velocity():
#             V_r = Environment["Current_Velocity"] / (Natural_Frequency_for_beta() * PipeGeometry["Outer_Diameter"])
            
#             if V_r < 1 :
#                 VIV_result = "No VIV"

#             elif V_r <= 3 :
#                 VIV_result = "Inline VIV"

#             elif V_r <=8 :
#                 VIV_result = "Cross flow VIV"

#             else:
#                 VIV_result = "Severe VIV"

#             return V_r, VIV_result

#         Reduced_Velocity()

#         V_r, VIV_result = Reduced_Velocity()



        

#         #step 10 

#         def fatigue():
#             For_100_years_design = 100 * 365 * 24 * 3600

#             fn = Natural_Frequency_for_beta()
#             Number_of_cycle_n = fn * For_100_years_design

#             SN_Curve_for_N = get_SN_value(Stress_from_curvature)

            
#             D_fat = Number_of_cycle_n / SN_Curve_for_N

            
#             if D_fat > 1:
#                 Fatigue_status = "FAIL"
#             else:
#                 Fatigue_status = "PASS"


            

#             return D_fat, SN_Curve_for_N, Number_of_cycle_n, Fatigue_status
        
#         fatigue()

#         D_fat, SN_Curve_for_N, Number_of_cycle_n, Fatigue_status = fatigue() 


#         #step11

#         def Ultimate_Limit_State():
#             Allowable_Stress = 0.87 * MaterialProperty["Yield_Strength"]
#             print("Allowable_Stress : ", Allowable_Stress)

#             Unity_check = rho / Allowable_Stress
#             print("Unity_check : ", Unity_check)

#             if Unity_check < 1 :
#                 ULS_status = "SAFE"

#             else:
#                 ULS_status = "UNSAFE"


            
#             return Allowable_Stress, Unity_check, ULS_status

#         Ultimate_Limit_State()

#         Allowable_Stress, Unity_check, ULS_status = Ultimate_Limit_State() 



#         result = {
#             "LD_Check" : ld_result,
#             "Steel_Area" : Steel_Area(),
#             "Outer_Diameter_after_Coating" : Outer_Diameter_after_Coating(),
#             "Submerged_Mass" : Submerged_Mass(),
#             "Natural_Frequency" : Natural_Frequency(),
#             "Outer_Diameter_after_Concrete" : Outer_Diameter_after_Concrete(),
#             "Submerged_Weight" : Submerged_Weight(),
#             "alpha" : alpha,
#             "Flow_Regime_status" : Flow_Regime_status,
#             "Coating_Area" : Coating_Area(),
#             "Concrete_Coating" : Concrete_Coating(),
#             "Bending_Stiffness" : Bending_Stiffness(),
#             "Reduced_velocity" : V_r,
#             "VIV_Status" : VIV_result,
#             "Concrete_Area" : Concrete_Area(),
#             "Total" : Total(),
#             "Bending_Stiffness_EI" : Bending_Stiffness_EI(),
#             "D_fat" : D_fat,
#             "SN_Curve_for_N" : SN_Curve_for_N,
#             "Number_of_cycle_n" : Number_of_cycle_n,
#             "Fatigue_status" : Fatigue_status,
#             "Outer_Diameter_including_coating_concrete" : Outer_Diameter_including_coating_concrete(),
#             "Buoyancy" : Buoyancy(),
#             "Deflection_value" : delta,
#             "Deflection_status": def_status,
#             "stress_rho" : rho,
#             "BendingStress_status" : BendingStress_Result,
#             "Flow_Regime_status" : Flow_Regime_status,
#             "Total_Outer_Area" : Total_Outer_Area(),
#             "Bending_Stress_Moment" : Bending_Stress_Moment(),
#             "Allowable_Stress" : Allowable_Stress,
#             "Unity_check" : Unity_check,
#             "ULS_status" : ULS_status,
#             "SN_curve": SN_curve,
#             "Stress_Range": Stress_Range,
#         }

#         return result

#     except Exception as e:
#         print("error: ",e)


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

        PipeGeometry = {
            "Outer_Diameter": frontendData["Outer_Diameter"],             # m
            "Wall_Thickness": frontendData["Wall_Thickness"],             # m
            "Coating_Thickness": frontendData["Coating_Thickness"],       # m
            "Concrete_Thickness": frontendData["Concrete_Thickness"],     # m
        }

        Constant = {
            "Beta_Value": frontendData["Beta_Value"],
            "Gravity": constant["gravity"],                               # m/s²
        }

        MaterialProperty = {
            "Steel_density": constant["Steel_density"],                   # kg/m³
            "Coating_Density": frontendData["Coating_Density"],           # kg/m³
            "Concrete_Density": constant["Concrete_Density"],             # kg/m³
            "Water_Density": constant["Water_Density"],                   # kg/m³
            "Youngs_Modulus": constant["Youngs_Modulus"],                 # Pa
            "Yield_Strength": frontendData["Yield_Strength"],             # MPa
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
            * MaterialProperty["Content_Density"]
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
            * MaterialProperty["Water_Density"]
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
            5
            * submerged_weight
            * Assumed_Span_Length**4
        ) / (
            240
            * EI
        )
        # Beam deflection formula for uniformly distributed load with fixed-fixed ends: δ = (5 * w * L^4) / (384 * EI)
        # Condition:
        #| Criterion | Meaning              |
        # | --------- | -------------------- |
        # | L/180     | Very flexible        |
        # | L/240     | Moderate             |
        # | L/360     | Typical              |
        # | L/500     | Strict               |
        # | L/1000    | Precision structures |


        delta_mm = delta * 1000

        if delta_mm < 25:
            Deflection_status = "PASS"
        else:
            Deflection_status = "FAIL"

        print("\n================ DEFLECTION ================")
        print("Deflection:", delta_mm, "mm")
        print("Deflection Status:", Deflection_status)

        # ============================================================
        # BENDING STRESS
        # ============================================================

        M = (
            submerged_weight
            * Assumed_Span_Length**2
        ) / 8

        rho = (
            M / Z
        ) / 1e6

        if 10 <= rho <= 100:
            BendingStress_status = "SAFE"
        else:
            BendingStress_status = "UNSAFE"

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
