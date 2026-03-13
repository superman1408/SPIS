import math


class FreeSpanSolver:

    def __init__(self, data):

        self.Ds = data["D_steel"]
        self.ts = data["t_steel"]
        self.tc = data["t_coating"]

        self.rho_s = data["rho_steel"]
        self.rho_c = data["rho_concrete"]
        self.rho_w = data["rho_water"]

        self.E = data["E"]
        self.SMYS = data["SMYS"]

        self.U = data["current_velocity"]

        self.alpha = data["alpha"]
        self.deltaT = data["deltaT"]

        self.g = 9.81

        self.calculate_section_properties()


    def calculate_section_properties(self):

        self.ID = self.Ds - 2*self.ts
        self.D = self.Ds + 2*self.tc

        self.As = math.pi/4 * (self.Ds**2 - self.ID**2)
        self.Ac = math.pi/4 * (self.D**2 - self.Ds**2)

        ms = self.rho_s * self.As
        mc = self.rho_c * self.Ac

        self.m = ms + mc

        ma = self.rho_w * math.pi*self.D**2/4
        self.me = self.m + ma

        self.I = math.pi/64 * (self.Ds**4 - self.ID**4)

        self.EI = self.E * self.I

        mw = self.rho_w * math.pi*self.D**2/4
        self.Ws = (self.m - mw) * self.g

        self.q = self.Ws


    def viv_span(self, Vr):

        fn = self.U/(Vr*self.D)

        C1 = 9.87

        L = ((C1*self.EI)/(self.me*(2*math.pi*fn)**2))**0.25

        return L


    def inline_viv_span(self):

        return self.viv_span(2)


    def crossflow_viv_span(self):

        return self.viv_span(6)


    def inline_uls_span(self):

        y = self.Ds/2

        sigma_allow = 0.87*self.SMYS

        L = math.sqrt((8*sigma_allow*self.I)/(self.q*y))

        return L


    def crossflow_uls_span(self):

        L = self.inline_uls_span()

        # simplified dynamic amplification factor
        return L*0.8


    def buckling_span(self):

        A = self.As

        P = self.E*A*self.alpha*self.deltaT

        L = math.pi * math.sqrt(self.EI/P)

        return L


    def solve(self):

        L1 = self.inline_viv_span()
        L2 = self.crossflow_viv_span()
        L3 = self.inline_uls_span()
        L4 = self.crossflow_uls_span()
        L5 = self.buckling_span()

        allowable = min(L1, L2, L3, L4, L5)

        spans = {
            "Inline_VIV_span": L1,
            "Crossflow_VIV_span": L2,
            "Inline_ULS_span": L3,
            "Crossflow_ULS_span": L4,
            "Buckling_span": L5,
            "Maximum_allowable_span": allowable
        }

        return spans



# Example Input

data = {

"D_steel": 0.406,
"t_steel": 0.019,
"t_coating": 0.05,

"rho_steel": 7850,
"rho_concrete": 3040,
"rho_water": 1025,

"E": 2.1e11,

"SMYS": 450e6,

"current_velocity": 1.2,

"alpha": 1.2e-5,
"deltaT": 60

}


solver = FreeSpanSolver(data)

result = solver.solve()

for k,v in result.items():

    print(k, ":", round(v,2), "m")