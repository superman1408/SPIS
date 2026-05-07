import math
from utils import constant


__version__ = "Free Span Analysis calculation version: 0.0.1"

print(__version__)


def freeSpan_Analysis_calculation(frontendData):
    
    try:

        PipeGeometry = {
            "Outer_Diameter":   frontendData["Outer_Diameter"], #Frontend
            "Wall_Thickness":   frontendData["Wall_Thickness"], #Frontend
            "Coating_Thickness":  frontendData["Coating_Thickness"], #Frontend
            "Concrete_Thickness": frontendData["Concrete_Thickness"], #Frontend
        }

        Constant = {
            "Gravity": constant["gravity"],
            "Fixed_Fixed": constant["Fixed_Fixed"],
            "Pinned_Pinned": constant["Pinned_Pinned"],
            "Fixed_Pinned": constant["Fixed_Pinned"],
        }

        MaterialProperty = {
            "Steel_density": constant["Steel_density"],
            "Coating_Density": frontendData["Coating_Density"], #Frontend
            "Concrete_Density": constant["Concrete_Density"],
            "Water_Density": constant["Water_Density"],
            "Youngs_Modulus": constant["Youngs_Modulus"],
            "Yield_Strength": constant["Yield_Strength"],
        }

        Environment = {
            "Current_Velocity": frontendData["Current_Velocity"], #Frontend
            "Wave_Velocity": frontendData["Wave_Velocity"], #Frontend
        }


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
                    # Linear interpolation (log scale recommended)
                    log_n1 = math.log10(n1)
                    log_n2 = math.log10(n2)

                    log_n = log_n1 + (stress - s1) * (log_n2 - log_n1) / (s2 - s1)

                    return 10 ** log_n

            # Outside range
            if stress < SN_curve[0][0]:
                return SN_curve[0][1]
            else:
                return SN_curve[-1][1]

        Assumed_Span_Length = frontendData["Assumed_Span_Length"]


        Vibration_Amplitude = 0.2 * PipeGeometry["Outer_Diameter"]
        print("Vibration_Amplitude : ", Vibration_Amplitude)

        Curvature = Vibration_Amplitude/Assumed_Span_Length**2
        print("Curvature", Curvature)

        Stress_from_curvature = (
            MaterialProperty["Youngs_Modulus"]
            * (PipeGeometry["Outer_Diameter"] / 2)
            * Curvature
        ) / 10**6

        print("Stress_from_curvature", Stress_from_curvature)

        # ---- THEN STORE ----
        Stress_Range = {
            "Vibration_Amplitude": Vibration_Amplitude,
            "Curvature": Curvature,
            "Stress": Stress_from_curvature
        }




        # ---- CALCULATIONS FIRST ---- 


        def LD_Check():
            
            Assumed_Span_Length_by_Outer_Diameter = Assumed_Span_Length / PipeGeometry["Outer_Diameter"]

            print(f"L/D Ratio = {Assumed_Span_Length_by_Outer_Diameter}")

            if Assumed_Span_Length_by_Outer_Diameter < 140:
                L_by_D_check = "PASS"
                
            else:
                L_by_D_check = "FAIL"

            print("L_by_D_check", L_by_D_check)

            return L_by_D_check

        
        # ✅ ADD THIS BLOCK HERE
        ld_result = LD_Check()

        if ld_result == "FAIL":
            ld_resultStatus = "L/D failed stopping further calculations"

            return {
                "LD_Check": "FAIL",
                "message": "L/D ratio not acceptable as L/D < 140. No further calculations done."
            }

        def Steel_Area():
            Steel_Area = math.pi/4 * ((PipeGeometry["Outer_Diameter"])**2-(PipeGeometry["Outer_Diameter"] - 2 * PipeGeometry["Wall_Thickness"])**2)
            print("Steel_Area",  Steel_Area)
            return Steel_Area

        Steel_Area()


        def Outer_Diameter_including_coating_concrete():
            D_Outer = 1.0668 + 2 * (0.0042 + 0.06)
            # print("D_Outer" , D_Outer)
            return D_Outer

        Outer_Diameter_including_coating_concrete()

        def Total_Outer_Area():
            A_Outer = math.pi/4 * (Outer_Diameter_including_coating_concrete())**2
            # print("A_Outer", A_Outer)
            return A_Outer

        Total_Outer_Area()

        def Outer_Diameter_after_Coating():
            D_Coat = PipeGeometry["Outer_Diameter"]+2*(PipeGeometry["Coating_Thickness"])
            print("D_Coat", D_Coat)
            return D_Coat

        Outer_Diameter_after_Coating()

        def Coating_Area():
            A_Coat = math.pi/4*((Outer_Diameter_after_Coating()**2)-PipeGeometry["Outer_Diameter"]**2)
            print("A_Coat" , A_Coat)
            return A_Coat

        Coating_Area()

        def Outer_Diameter_after_Concrete():
            D_cwc = Outer_Diameter_after_Coating() + 2 *PipeGeometry["Concrete_Thickness"]
            print("D_cwc" , D_cwc)
            return D_cwc

        Outer_Diameter_after_Concrete()

        def Concrete_Area():
            A_cwc = math.pi/4*(Outer_Diameter_after_Concrete()**2 - Outer_Diameter_after_Coating()** 2)
            print("A_cwc" , A_cwc)
            return A_cwc

        Concrete_Area()


        # STEP 2

        def Mass_per_meter_Steel():
            m_s = MaterialProperty["Steel_density"] * Steel_Area()
            print("m_s" , m_s )
            return m_s

        Mass_per_meter_Steel()


        def Concrete_Coating():
            m_c = Concrete_Area() * MaterialProperty["Concrete_Density"] + MaterialProperty["Coating_Density"] * Coating_Area()
            print("m_c" , m_c)
            return m_c

        Concrete_Coating()

        def Total():
            m_total = Mass_per_meter_Steel() + Concrete_Coating()
            print("m_total" , m_total)
            return m_total

        Total()


        # STEP 3.5

        def Buoyancy():
            Water_Mass_m_water = Total_Outer_Area() * MaterialProperty["Water_Density"]
            print("Water_Mass_m_water" , Water_Mass_m_water)
            return Water_Mass_m_water

        Buoyancy()


        def Submerged_Mass():
            m_eff = Total() - Buoyancy()
            print("m_eff", m_eff)
            return m_eff

        Submerged_Mass()

        def Submerged_Weight():
            w = Submerged_Mass() * Constant["Gravity"]
            print("w",w)
            return w

        Submerged_Weight()

        def Bending_Stiffness():
            Moment_of_Inertia = math.pi/64 * (
                PipeGeometry["Outer_Diameter"]**4 -
                (PipeGeometry["Outer_Diameter"] - 2 * PipeGeometry["Wall_Thickness"])**4
            )
            
            print("Moment_of_Inertia : ", Moment_of_Inertia)
            # EI = MaterialProperty["Youngs_Modulus"] * Moment_of_Inertia
            
            return Moment_of_Inertia

        Bending_Stiffness()


        def Bending_Stiffness_EI():
            EI = MaterialProperty["Youngs_Modulus"] * Bending_Stiffness()
            print ("EI : ", EI)
            
            return EI

        Bending_Stiffness_EI()


        # def Bending_Stiffness():
        #     Moment_of_Inertia = math.pi/64*(PipeGeometry["Outer_Diameter"]**4 - ((PipeGeometry["Outer_Diameter"] - 2 * PipeGeometry["Wall_Thickness"])**4))
        #     print("Moment_of_Inertia", Moment_of_Inertia)
            

        #     E_into_I = MaterialProperty["Youngs_Modulus"] * Moment_of_Inertia
        #     print("E_into_I", E_into_I)

        #     return Moment_of_Inertia, E_into_I


        def Deflection():

            E_into_I = Bending_Stiffness_EI()
            delta = (5* Submerged_Weight() * Assumed_Span_Length**4)/(384 * E_into_I)
            print("delta", delta)

            

            if delta < 25:
                Deflection_result = "PASS"
            else:
                Deflection_result = "FAIL"

            print("Deflection_result", Deflection_result)

            return delta, Deflection_result


        Deflection()

        delta, def_status = Deflection()


        # step 6

        def Bending_Stress_Moment():
            M = (Submerged_Weight() * (Assumed_Span_Length**2))/8
            print("M : ", M )
            return M

        Bending_Stress_Moment()

        def Section_Modulus():
            D = PipeGeometry["Outer_Diameter"]
            I = Bending_Stiffness()
            
            Z = I / (D / 2)
            
            print("Section Modulus:", Z)
            return Z


        Section_Modulus()

        def Stress_rho():
            M = Bending_Stress_Moment()   
            Z = Section_Modulus()    
            

            rho = (M / Z) / 10**6           # σ = M / Z
            
            print("rho:", rho)
            # return rho

       

            # Srho = Stress_rho()

            if 10 <= rho <= 100 :
                BendingStress_Result = "SAFE"
            else:
                BendingStress_Result = "UNSAFE"



            print("BendingStress_Result", BendingStress_Result)

            return rho, BendingStress_Result


        Stress_rho()


        stress_rho, BendingStress_Result = Stress_rho()


 

        #step 7

        def Natural_Frequency():
            # natural_frequency = Submerged_Mass() * (Assumed_Span_Length**4)
            # print("natural_frequency", natural_frequency)

            # return natural_frequency

            m_eff_into_L = Submerged_Mass() * (Assumed_Span_Length**4)
            print("m_eff_into_L : ",m_eff_into_L )
            return m_eff_into_L

        Natural_Frequency()

        def Natural_Frequency_fn():

            mL = Natural_Frequency() 

            if mL <= 0:
                raise ValueError("Submerged mass is negative → Pipe is buoyant → Invalid condition")

            EI_by_mL = Bending_Stiffness_EI() / mL
            print("EI_by_mL : ", EI_by_mL)

            f_n = 0.5 * math.sqrt(EI_by_mL)

            print("f_n", f_n)

            return f_n                                                                                        

        Natural_Frequency_fn()



        # Step 8
        def Flow_Regime():
            alpha = Environment["Current_Velocity"] / (Environment["Current_Velocity"] + Environment["Wave_Velocity"])
            print("Flow Regime :", alpha)

            

            if alpha < 0.5 :
                Flow_Regime_result = "Wave dominated"

            elif alpha >0.8 :
                Flow_Regime_result = "Current dominated"
            
            else:
                Flow_Regime_result = "Mixed"

            # print("Flow_Regime_result", Flow_Regime_result)

            return alpha, Flow_Regime_result

        Flow_Regime()

        alpha, Flow_Regime_status = Flow_Regime()





        #step 9
        def Reduced_Velocity():
            V_r = Environment["Current_Velocity"] / (Natural_Frequency_fn() * PipeGeometry["Outer_Diameter"])
            print("Reduced velocity : ", V_r)

            if V_r < 1 :
                VIV_result = "No VIV"

            elif V_r <= 3 :
                VIV_result = "Inline VIV"

            elif V_r <=8 :
                VIV_result = "Cross flow VIV"

            else:
                VIV_result = "Severe VIV"

            return V_r, VIV_result

        Reduced_Velocity()

        V_r, VIV_result = Reduced_Velocity()



        

        #step 10 

        def fatigue():
            For_100_years_design = 100 * 365 * 24 * 3600

            fn = Natural_Frequency_fn()
            Number_of_cycle_n = fn * For_100_years_design

            SN_Curve_for_N = get_SN_value(Stress_from_curvature)

            print("SN_Curve_for_N :", SN_Curve_for_N)

            D_fat = Number_of_cycle_n / SN_Curve_for_N

            print("D_fat :", D_fat)

            if D_fat > 1:
                Fatigue_status = "FAIL"
            else:
                Fatigue_status = "PASS"


            # print("Fatigue_result",Fatigue_result)
            

            return D_fat, SN_Curve_for_N, Number_of_cycle_n, Fatigue_status
        
        fatigue()

        D_fat, SN_Curve_for_N, Number_of_cycle_n, Fatigue_status = fatigue() 


        #step11

        def Ultimate_Limit_State():
            Allowable_Stress = 0.87 * MaterialProperty["Yield_Strength"]
            print("Allowable_Stress : ", Allowable_Stress)

            Unity_check = stress_rho / Allowable_Stress
            print("Unity_check : ", Unity_check)

            if Unity_check < 1 :
                ULS_status = "SAFE"

            else:
                ULS_status = "UNSAFE"


            # print("ULS_result", ULS_result)

            return Allowable_Stress, Unity_check, ULS_status

        Ultimate_Limit_State()

        Allowable_Stress, Unity_check, ULS_status = Ultimate_Limit_State() 



        
        



        result = {
            "LD_Check" : ld_result,
            "Steel_Area" : Steel_Area(),
            "Outer_Diameter_after_Coating" : Outer_Diameter_after_Coating(),
            "Submerged_Mass" : Submerged_Mass(),
            "Natural_Frequency" : Natural_Frequency(),
            "Outer_Diameter_after_Concrete" : Outer_Diameter_after_Concrete(),
            "Submerged_Weight" : Submerged_Weight(),
            "alpha" : alpha,
            "Flow_Regime_status" : Flow_Regime_status,
            "Coating_Area" : Coating_Area(),
            "Concrete_Coating" : Concrete_Coating(),
            "Bending_Stiffness" : Bending_Stiffness(),
            "Reduced_velocity" : V_r,
            "VIV_Status" : VIV_result,
            "Concrete_Area" : Concrete_Area(),
            "Total" : Total(),
            "Bending_Stiffness_EI" : Bending_Stiffness_EI(),
            "D_fat" : D_fat,
            "SN_Curve_for_N" : SN_Curve_for_N,
            "Number_of_cycle_n" : Number_of_cycle_n,
            "Fatigue_status" : Fatigue_status,
            "Outer_Diameter_including_coating_concrete" : Outer_Diameter_including_coating_concrete(),
            "Buoyancy" : Buoyancy(),
            "Deflection_value" : delta,
            "Deflection_status": def_status,
            "stress_rho" : stress_rho,
            "BendingStress_status" : BendingStress_Result,
            "Flow_Regime_status" : Flow_Regime_status,
            "Total_Outer_Area" : Total_Outer_Area(),
            "Bending_Stress_Moment" : Bending_Stress_Moment(),
            "Allowable_Stress" : Allowable_Stress,
            "Unity_check" : Unity_check,
            "ULS_status" : ULS_status,
            "SN_curve": SN_curve,
            "Stress_Range": Stress_Range
        }


        print("result", result)

        return result

    except Exception as e:
        print("error: ",e)


