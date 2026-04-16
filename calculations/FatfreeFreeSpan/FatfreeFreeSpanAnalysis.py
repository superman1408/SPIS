import math

__version__ = "Free Span Analysis"

print(__version__)

PipeGeometry = {
    "Outer_Diameter": 1.0668,
    "Wall_Thickness": 0.0238,
    "Coating_Thickness": 0.0042,
    "Concrete_Thickness": 0.06,
}

Constant = {
   "Gravity": 9.81,
    "Fixed_Fixed": 4.73,
    "Pinned_Pinned": 3.14,
    "Fixed_Pinned": 3.93,
}

MaterialProperty = {
    "Steel_density": 7850,
    "Coating_Density": 940,
    "Concrete_Density": 3040,
    "Water_Density": 1030,
    "Youngs_Modulus": 2.07 * 10**11,
    "Yield_Strength": 450,
}

Environment = {
    "Current_Velocity": 0.8,
    "Wave_velocity": 0.5,
}


SN_curve = {

}

Assumed_Span_Length = 36.711


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
        print("PASS")
    else:
        print("FAIL")

 
LD_Check()

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
        print("PASS")
    else:
        print("FAIL")

    return delta


Deflection()


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
    return rho

Stress_rho()

if 10<= Stress_rho()<=100 :
    print("SAFE")
else:
    print("UNSAFE")



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

    EI_by_mL = Bending_Stiffness_EI() / Natural_Frequency()
    print("EI_by_mL : ", EI_by_mL)

    f_n = 0.5 * math.sqrt(EI_by_mL)

    print("f_n", f_n)

    return f_n

Natural_Frequency_fn()



# Step 8
def Flow_Regime():
    alpha = Environment["Current_Velocity"] / (Environment["Current_Velocity"] + Environment["Wave_velocity"])
    print("Flow Regime :", alpha)

    

    if alpha < 0.5 :
        print("Wave dominated")

    elif alpha >0.8 :
        print("Current dominated")
    
    else:
        print("Mixed")

    return alpha

Flow_Regime()



#step 9
def Reduced_Velocity():
    V_r = Environment["Current_Velocity"] / (Natural_Frequency_fn() * PipeGeometry["Outer_Diameter"])
    print("Reduced velocity : ", V_r)

    if V_r < 1 :
        print("No VIV")

    elif V_r <= 3 :
        print("Inline VIV")

    elif V_r <=8 :
        print("Cross flow VIV")

    else:
        print("Severe VIV")

    return V_r

Reduced_Velocity()

 

#step 10 

def fatigue():
    For_100_years_design = 100*365*24*3600

    Number_of_cycle_n = Natural_Frequency_fn() * For_100_years_design
    print("Number_of_cycle_n : ", Number_of_cycle_n)

    SN_Curve_for_N = (10**16) / (Stress_from_curvature**5)
    print("SN_Curve_for_N : ", SN_Curve_for_N)

    D_fat = Number_of_cycle_n / SN_Curve_for_N
    print("D_fat : ", D_fat)

    if D_fat > 1 :
        print("Fatigue Damage : FAIL")

    else:
        print("Fatigue Damage : PASS")

    return D_fat, SN_Curve_for_N, Number_of_cycle_n
fatigue()


#step11

def Ultimate_Limit_State():
    Allowable_Stress = 0.87 * MaterialProperty["Yield_Strength"]
    print("Allowable_Stress : ", Allowable_Stress)

    Unity_check = Stress_rho() / Allowable_Stress
    print("Unity_check : ", Unity_check)

    if Unity_check < 1 :
        print("SAFE")

    else:
        print("UNSAFE")

    return Allowable_Stress, Unity_check

Ultimate_Limit_State()