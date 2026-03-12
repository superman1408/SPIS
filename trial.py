# Create an Excel calculation sheet for the DNV-RP-F105 span calculation summary
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Free Span Calculation"

rows = [
    ["DNV-RP-F105 Free Span Calculation Sheet", "", "", "", ""],
    [],
    ["INPUT DATA"],
    ["Parameter", "Symbol", "Unit", "Value"],
    ["Steel Outside Diameter", "Ds", "m", 0.406],
    ["Wall Thickness", "ts", "m", 0.019],
    ["Concrete Coating Thickness", "tc", "m", 0.05],
    ["Steel Density", "rho_s", "kg/m3", 7850],
    ["Concrete Density", "rho_c", "kg/m3", 3040],
    ["Water Density", "rho_w", "kg/m3", 1025],
    ["Youngs Modulus", "E", "Pa", 2.1e11],
    ["SMYS", "SMYS", "Pa", 450e6],
    ["Current Velocity", "U", "m/s", 1.2],
    ["Thermal Expansion Coefficient", "alpha", "1/C", 1.2e-5],
    ["Temperature Difference", "dT", "C", 60],
    [],
    ["PIPE GEOMETRY"],
    ["Inner Diameter", "ID", "m", "=D5-2*D6"],
    ["Total Diameter with Coating", "D", "m", "=D5+2*D7"],
    [],
    ["SECTION AREAS"],
    ["Steel Area", "As", "m2", "=PI()/4*(D5^2-D18^2)"],
    ["Concrete Area", "Ac", "m2", "=PI()/4*(D19^2-D5^2)"],
    [],
    ["MASS PER UNIT LENGTH"],
    ["Steel Mass", "ms", "kg/m", "=D8*D21"],
    ["Concrete Mass", "mc", "kg/m", "=D9*D22"],
    ["Total Mass", "m", "kg/m", "=D24+D25"],
    [],
    ["HYDRODYNAMIC ADDED MASS"],
    ["Added Mass", "ma", "kg/m", "=D10*PI()*D19^2/4"],
    ["Effective Mass", "me", "kg/m", "=D26+D28"],
    [],
    ["MOMENT OF INERTIA"],
    ["I", "", "m4", "=PI()/64*(D5^4-D18^4)"],
    [],
    ["BENDING STIFFNESS"],
    ["EI", "", "Nm2", "=D11*D31"],
    [],
    ["SUBMERGED WEIGHT"],
    ["Displaced Water Mass", "", "kg/m", "=D10*PI()*D19^2/4"],
    ["Submerged Weight", "Ws", "N/m", "=(D26-D34)*9.81"],
    [],
    ["INLINE VIV SPAN"],
    ["Reduced Velocity", "Vr", "", 2],
    ["Natural Frequency", "fn", "Hz", "=D13/(D37*D19)"],
    ["Inline VIV Span", "L1", "m", "=(9.87*D32/(D29*(2*PI()*D38)^2))^(1/4)"],
    [],
    ["CROSSFLOW VIV SPAN"],
    ["Reduced Velocity", "Vr", "", 6],
    ["Natural Frequency", "fn", "Hz", "=D13/(D41*D19)"],
    ["Crossflow VIV Span", "L2", "m", "=(9.87*D32/(D29*(2*PI()*D42)^2))^(1/4)"],
    [],
    ["INLINE ULS SPAN"],
    ["Allowable Stress", "", "Pa", "=0.87*D12"],
    ["Inline ULS Span", "L3", "m", "=SQRT((8*D45*D31)/(D35*(D5/2)))"],
    [],
    ["CROSSFLOW ULS SPAN"],
    ["Crossflow ULS Span", "L4", "m", "=0.8*D46"],
    [],
    ["BUCKLING SPAN"],
    ["Axial Force", "P", "N", "=D11*D21*D14*D15"],
    ["Buckling Span", "L5", "m", "=PI()*SQRT(D32/D49)"],
    [],
    ["FINAL RESULT"],
    ["Maximum Allowable Span", "", "m", "=MIN(D39,D43,D46,D48,D50)"]
]

for r in rows:
    ws.append(r)

path = "E:/SPIS/views/dnv_rp_f105_span_calculation.xlsx"
wb.save(path)

path