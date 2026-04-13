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



Vibration_Amplitude = 0.2 * PipeGeometry["Outer_Diameter"]

Curvature = Vibration_Amplitude

Stress = (
    MaterialProperty["Youngs_Modulus"]
    * (PipeGeometry["Outer_Diameter"] / 2)
    * Curvature
)

# ---- THEN STORE ----
Stress_Range = {
    "Vibration_Amplitude": Vibration_Amplitude,
    "Curvature": Curvature,
    "Stress": Stress
}

# ---- CALCULATIONS FIRST ---- 

Assumed_Span_Length = 130
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
    print("D_Outer" , D_Outer)
    return D_Outer

Outer_Diameter_including_coating_concrete()

def Total_Outer_Area():
    A_Outer = math.pi/4 * (Outer_Diameter_including_coating_concrete())**2
    print("A_Outer", A_Outer)
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
    Moment_of_Inertia = math.pi/64*(PipeGeometry["Outer_Diameter"]**4 - ((PipeGeometry["Outer_Diameter"] - 2 * PipeGeometry["Wall_Thickness"])**4))
    print("Moment_of_Inertia", Moment_of_Inertia)
    

    E_into_I = MaterialProperty["Youngs_Modulus"] * Moment_of_Inertia
    print("E_into_I", E_into_I)

    return Moment_of_Inertia, E_into_I

Bending_Stiffness()

def Deflection():

    _, E_into_I = Bending_Stiffness()
    delta = (5* Submerged_Weight() * Assumed_Span_Length**4)/(384 * E_into_I)
    print("delta", delta)

    return delta  
# This need to be check

Deflection()