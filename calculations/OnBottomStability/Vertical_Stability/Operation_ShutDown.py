import math


rh_HDPE = 960
OD = 2300/1000
t_HDPE = 88.5/1000
CA = 0
V_c = 3.5
rh_c = 2400
rh_cont = 0
gamma_w = 1.1

rh_seawater = 1025

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
print("A_t :",A_t)

V_t= round((V_OD - V_ID ),3)
print("V_t :",V_t)

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

SG = round((((B_pipe * g + W_s *g)/B_pipe*g)/100),3)
print("SG",SG)

UC = round((gamma_w/SG),3)
print(UC)

if UC<=1:
    print("STABLE")

else:
    print("NOT STABLE")
