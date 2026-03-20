import math
from utils import constant
import random


__version__ = "Vertical Stability Installation Empty version: 0.0.1"

print(__version__)


def verticalStability_installationEmpty(frontendData):
    print("Vertical Stability Installation Empty calculation started")
    # print(type(constant["density_seawater"]))
    try:

        rh_HDPE = float(frontendData["rh_HDPE"])
        OD = float(frontendData["OD"])/1000
        t_HDPE = float(frontendData["t_HDPE"])/1000
        CA = float(frontendData["CA"])
        V_c = float(frontendData["V_c"])
        rh_cont = float(frontendData["rh_cont"])
        gamma_w = float(frontendData["gamma_w"])
        
        rh_seawater = constant["density_seawater"]
        rh_c = constant["density_concrete"]
        g= constant["gravity"]

        ID = round((OD - 2* t_HDPE),3) #calculating Internal Diameter of a pipe.
        print("ID : ",ID)

        # ---------------------------------Calculation------------------------------------


        print(math.pi)

        A_OD = round((math.pi * (OD*OD)/4),3)
        print("A_OD",A_OD)

        V_OD = A_OD * 1
        print("V_OD",V_OD)

        A_ID = round((math.pi * ((ID**2)/4)),3)
        print("A_ID",A_ID)

        V_ID = A_ID * 1 
        print("V_ID",V_ID)

        A_t = round((A_OD - A_ID ),3)
        print("A_t",A_t)

        V_t= round((V_OD - V_ID ),3)
        print("V_t",V_t)

        M_pipe = round((A_t * rh_HDPE ),3)
        print("M_pipe",M_pipe)

        M_seawater = A_ID * rh_cont
        print("M_seawater",M_seawater)

        B_pipe = round((A_OD * rh_seawater),0)
        print("B_pipe",B_pipe)

        # A_c = V_c 
        # print("A_c",A_c)

        M_c = rh_c * V_c
        print("M_c",M_c)

        B_c = (M_c*rh_seawater)/rh_c
        print("B_c",B_c)

        W_p = M_pipe - B_pipe
        print( "W_p",W_p)

        W_c = M_c - B_c
        print("W_c",W_c)

        W_s = W_p + W_c
        print( "W_s",W_s)

        SG = ((B_pipe * g + W_s *g)/B_pipe*g)/100
        print("SG",SG)

        UC = gamma_w/SG
        print(UC)

        UC_status = "SINK" if UC <= 1 else "FLOAT"


        resultInstallationEmpty = {
            "A_OD" : A_OD,
            "V_OD":V_OD,
            "A_ID":A_ID,
            "V_ID":V_ID,
            "A_t":A_t,
            "V_t":V_t,
            "M_pipe":M_pipe,
            "M_seawater":M_seawater,
            "B_pipe":B_pipe,
            "M_c":M_c,
            "B_c":B_c,
            "W_p":W_p,
            "W_c":W_c,
            "W_s":W_s,
            "SG":SG,
            "UC":UC,
            "UC_status":UC_status,

        }

        return resultInstallationEmpty
    


    except Exception as e:
        print(f"error code in installation:{random.random()}>>>>>>{e}")