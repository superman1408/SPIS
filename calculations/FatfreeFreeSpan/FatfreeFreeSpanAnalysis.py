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

def LD_Check():
    Assumed_Span_Length = 130
    Assumed_Span_Length_by_Outer_Diameter = Assumed_Span_Length / PipeGeometry["Outer_Diameter"]

    print(f"L/D Ratio = {Assumed_Span_Length_by_Outer_Diameter}")

    if Assumed_Span_Length_by_Outer_Diameter < 140:
        print("PASS")
    else:
        print("FAIL")

 
LD_Check()

def Steel_Area():
    Steel_Area = math.pi/4 * ((PipeGeometry["Outer_Diameter"])**2-(PipeGeometry["Outer_Diameter"] - 2 * PipeGeometry["Wall_Thickness"])**2)
    print(Steel_Area)

Steel_Area()

def Outer_Diameter_including_coating_concrete():
    D_Outer = 1.0668 + 2 * (0.0042 + 0.06)
    print(D_Outer)
    return D_Outer

Outer_Diameter_including_coating_concrete()

def Total_Outer_Area():
    A_Outer = math.pi * (Outer_Diameter_including_coating_concrete())**2
    print(A_Outer)

Total_Outer_Area()




