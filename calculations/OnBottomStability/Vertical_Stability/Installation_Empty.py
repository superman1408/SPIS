import math
from utils import constant
import random


__version__ = "Vertical Stability Installation Empty version: 0.0.1"

print(__version__)


def verticalStability_installationEmpty(frontendData):
    # frontendData = {
    #                 "rh_HDPE": float(self.rho_HDPE_lineEdit.text()),
    #                 "OD": float(self.OD_lineEdit.text()),
    #                 "t_HDPE": float(self.tHDPE_lineEdit.text()),
    #                 "CA": float(self.CA_lineEdit.text()),
    #                 "V_c": float(self.Vc_lineEdit.text()),
    #                 "rh_c": float(self.rho_c_lineEdit.text()),
    #                 "rh_cont": float(self.rho_cont_lineEdit.text()),
    #                 "gamma_w": float(self.yw_lineEdit.text()),
    #             }

    try:

        rh_HDPE = frontendData["rh_HDPE"]
        OD = frontendData["OD"]/1000
        t_HDPE = frontendData["t_HDPE"]/1000
        CA = frontendData["CA"]
        V_c = frontendData["V_c"]
        rh_c = frontendData["rh_c"]
        rh_cont = frontendData["rh_cont"]
        gamma_w = frontendData["gamma_w"]
        rh_seawater = frontendData["rh_seawater"]

        g= 9.81

        ID = round((OD - 2* t_HDPE),3)

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

        if UC<=1:
            UC_status = ("SINK")

        else:
            UC_status = ("FLOAT")


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