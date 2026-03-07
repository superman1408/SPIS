from ast import Str
from cmath import sqrt
import math
import random
from cgitb import small
from unittest import result
import numpy as np  
import numpy.polynomial.polynomial  as roots



def pressure_sysTest(Outside_Diameter_OD, Nominal_Wall_Thickness_tnom, Fabrication_Thickness_Tolerance_tfab, Corrosion_Allowance_tcorr, Ovality_of_Pipe_Oo,SMYS_σsmys,SMTS_σsmts,Derating_value_temp_yieldStress_fy_temp,Derating_value_temp_tensileStress_fu_temp,Youngs_Modulus_E ,Poission_s_Ratio_ν ,Maximum_Fabrication_Factor_alpha_fab,Pd,Elevation_at_Pressure_Reference_Level_href,Elevation_level_at_Pressure_Point_hl ,Product_Density_ρcont,Hydrotest_Water_Density_ρt,Incidental_to_Design_Pressure_Ratio_gamma_inc,Water_Depth_WD,Sea_Water_Density_ρsea,Min_Elevation_wrt_MSL_hmin,Safety_Class_RF_gamma_SCPC,Material_Strength_Factor_alpha_u,Material_resistant_factor_gamma_m):
    
    
    
    try:

        # Material_Strength_Factor_alpha_u = 1.15
        Gravity_of_Acceleration_g = 9.81
        Constant_for_Mill_Pressure_test_k = 1
        # Safety_Class_RF_gamma_SCPC = 1.046

        Outside_Diameter_OD = float(Outside_Diameter_OD) 
        # print(O.utside_Diameter_OD) 
        Nominal_Wall_Thickness_tnom = float(Nominal_Wall_Thickness_tnom) 
        # print("t_nom  ", Nominal_Wall_Thickness_tnom)
        Fabrication_Thickness_Tolerance_tfab = float(Fabrication_Thickness_Tolerance_tfab) 
        # print("t_fab ", Fabrication_Thickness_Tolerance_tfab)
        Corrosion_Allowance_tcorr = float(Corrosion_Allowance_tcorr) 
        # print("t_corr",Corrosion_Allowance_tcorr)
        Ovality_of_Pipe_Oo = float(Ovality_of_Pipe_Oo) 
        # print("oo ",Ovality_of_Pipe_Oo)
        SMYS_σsmys = float(SMYS_σsmys) 
        # print("smys ",SMYS_σsmys)
        SMTS_σsmts = float(SMTS_σsmts) 
        # print("smts ",SMTS_σsmts)
        Derating_value_temp_yieldStress_fy_temp = float(Derating_value_temp_yieldStress_fy_temp) 
        # print("fy_temp ",Derating_value_temp_yieldStress_fy_temp)
        Derating_value_temp_tensileStress_fu_temp = float(Derating_value_temp_tensileStress_fu_temp) 
        # print("fu_temp ",Derating_value_temp_tensileStress_fu_temp)
        Youngs_Modulus_E = float(Youngs_Modulus_E) 
        # print("E ",Youngs_Modulus_E)
        Poission_s_Ratio_ν = float(Poission_s_Ratio_ν) 
        # print("v ",Poission_s_Ratio_ν)
        Maximum_Fabrication_Factor_alpha_fab = float(Maximum_Fabrication_Factor_alpha_fab) 
        # print("alpha_fab ",Maximum_Fabrication_Factor_alpha_fab)
        Material_Strength_Factor_alpha_u = float(Material_Strength_Factor_alpha_u) 
        # print("alpha_u ",Material_Strength_Factor_alpha_u)
        Pd = float(Pd) 
        # print("Pd ",Pd)
        Material_resistant_factor_gamma_m = float(Material_resistant_factor_gamma_m) 
        # print("gamma_m ",Material_resistant_factor_gamma_m)
        
        Elevation_at_Pressure_Reference_Level_href = float(Elevation_at_Pressure_Reference_Level_href) 
        # print("href ",Elevation_at_Pressure_Reference_Level_href)
        Elevation_level_at_Pressure_Point_hl = float(Elevation_level_at_Pressure_Point_hl) 
        # print("hl ",Elevation_level_at_Pressure_Point_hl)
        Product_Density_ρcont = float(Product_Density_ρcont) 
        # print("rho_cont ",Product_Density_ρcont)
        Hydrotest_Water_Density_ρt = float(Hydrotest_Water_Density_ρt) 
        # print("rho_t ",Hydrotest_Water_Density_ρt)
        Incidental_to_Design_Pressure_Ratio_gamma_inc = float(Incidental_to_Design_Pressure_Ratio_gamma_inc) 
        # print("gamma_inc ",Incidental_to_Design_Pressure_Ratio_gamma_inc)
        Water_Depth_WD = float(Water_Depth_WD) 
        # print("WDmin ",Water_Depth_WD)
        Sea_Water_Density_ρsea = float(Sea_Water_Density_ρsea) 
        # print("rho_sea ",Sea_Water_Density_ρsea)
        Min_Elevation_wrt_MSL_hmin = float(Min_Elevation_wrt_MSL_hmin)
        # print("hmin ",Min_Elevation_wrt_MSL_hmin)

        Safety_Class_RF_gamma_SCPC = float(Safety_Class_RF_gamma_SCPC) 
        # print("gamma_SCPC ",Safety_Class_RF_gamma_SCPC)
    
    # print("___________________PIPELINE INPUTS___________________")

        Measured_Minimum_Thickness_for_Test_Pressure_t1 = round((Nominal_Wall_Thickness_tnom - Fabrication_Thickness_Tolerance_tfab),3)
        print(f"Measured Minimum Thickness for Test Pressure : {Measured_Minimum_Thickness_for_Test_Pressure_t1}")


    # print("___________________________ENVIRONMENTAL INPUTS______________________________")

       

        Depth = round(float(Water_Depth_WD + Min_Elevation_wrt_MSL_hmin),3)
        print(Depth)

        
    # print("_____________________________DESIGNS FACTOR AS PER DNGVL____________________")

        # print("\n\tSAFETY CLASS : 'Medium'")

        
        # #  Stresses

        # print("_________________STRESSES_______________________")

        fy= round((float(SMYS_σsmys-Derating_value_temp_yieldStress_fy_temp)*Material_Strength_Factor_alpha_u),3)
        print("fy",fy)
        fu=round((float(SMTS_σsmts-Derating_value_temp_tensileStress_fu_temp)*Material_Strength_Factor_alpha_u),3)
        print("fu",fu)
        fcb=min(fy,(fu/1.15))
        print("fcb",fcb)




        # print("__________________________________PRESSURE_____________________________")

        # Pd = float(input("Enter Design Pressure : ")) 
        Pt = round(float(1.155*Pd),3)
        print("Pt",Pt)
        Plt = round(float(Incidental_to_Design_Pressure_Ratio_gamma_inc * Pd),3)
        print("Plt",Plt)
        Pe = round(float(((Sea_Water_Density_ρsea*Gravity_of_Acceleration_g*Depth))/1000000),3)
        print("Pe",Pe)

        if(Pe>0):
            ExternalPressure = Pe
            
        else:
            ExternalPressure = 0


        print("External Pressure : ",ExternalPressure)

        Pb_t1 = round(float(((2*Measured_Minimum_Thickness_for_Test_Pressure_t1)/(Outside_Diameter_OD-Measured_Minimum_Thickness_for_Test_Pressure_t1)) * fcb * 2/(math.sqrt(3))),3)
        print("Pb_t1",Pb_t1)

        Pmpt = round(float(Constant_for_Mill_Pressure_test_k * (2*Measured_Minimum_Thickness_for_Test_Pressure_t1/(Outside_Diameter_OD - Measured_Minimum_Thickness_for_Test_Pressure_t1)) * min(SMYS_σsmys * 0.96, SMTS_σsmts * 0.84)),3)
        print(Pmpt)


        # # Hydrotest Checks

        # # Pressure Containment

        # print("_______Pressure Containment check___________")





        if((Plt - Pe ) <= min((Pb_t1/Safety_Class_RF_gamma_SCPC),(Pmpt))):
            P_check = "Wall Thickness Accepted ✅"
            
        else:
            P_check = "Redesign Wall Thickness ❌"

           
            


        # Utility Check

        UC_prss_cont = round((Plt-Pe)/min((Pb_t1/Safety_Class_RF_gamma_SCPC),(Pmpt)),3)

        print("UC_prss_cont",UC_prss_cont)

        list_variable_names = ["Gravity of Acceleration g  [N]","Constant for Mill Pressure test k","Nominal Outer Diameter OD  [mm]","Nominal Wall Thickness tnom  [mm]", "Fabrication tolerance tfab  [mm]", "Corrosion Allowance tcorr  [mm]","Ovality of Pipe Oo","Specified minimum yield stress SMYS","Specified minimum tensile strength SMTS","Derating value temp yield Stress fytemp  [Mpa]","Derating value temp tensile strength futemp  [Mpa]","Young's Modulus E  [Mpa]","Poission's Ration v","Maximum Fabrication αfab","Material Strength Factor αu","Design Pressure Pd  [Mpa]", "Material Resistant Factor γm","Elevation at Pressure Reference Level href  [m]","Elevation Level at Pressure Point hl  [m]", "Product Density ρcont  [kg/m³]", "Hydrotest Water Density ρt  [kg/m³]","Incidental to Design Pressure Ratio γinc","Water Depth WD  [m]","Sea Water Density ρsea  [kg/m³]","Min Elevation wrt MSL hmin  [hmin]","Safety Class RF gamma SCPC", "Measured Minimum Thickness for Test Pressure t1  [mm]", "Depth  [m]", "Design Yield Stress fy  [Mpa]", "Design Tensile Strength fu  [Mpa]", "Minimum of fy;fu/1.15 fcb  [Mpa]", "System Test Pressure Pt  [Mpa]", "Local System test Pressure Plt  [Mpa]", "External Pressure Pe  [Mpa]", "External Pressure  [Mpa]", "Pressure Containment Resistant Pbt1  [Mpa]", "Mill Test Pressure Pmpt  [Mpa]", "P_check", "Utility Check"]
        
        list_variable = [Gravity_of_Acceleration_g, Constant_for_Mill_Pressure_test_k, Outside_Diameter_OD, Nominal_Wall_Thickness_tnom, Fabrication_Thickness_Tolerance_tfab, Corrosion_Allowance_tcorr, Ovality_of_Pipe_Oo, SMYS_σsmys, SMTS_σsmts, Derating_value_temp_yieldStress_fy_temp, Derating_value_temp_tensileStress_fu_temp, Youngs_Modulus_E, Poission_s_Ratio_ν, Maximum_Fabrication_Factor_alpha_fab, Material_Strength_Factor_alpha_u, Pd, Material_resistant_factor_gamma_m, Elevation_at_Pressure_Reference_Level_href, Elevation_level_at_Pressure_Point_hl, Product_Density_ρcont, Hydrotest_Water_Density_ρt, Incidental_to_Design_Pressure_Ratio_gamma_inc, Water_Depth_WD, Sea_Water_Density_ρsea, Min_Elevation_wrt_MSL_hmin, Safety_Class_RF_gamma_SCPC, Measured_Minimum_Thickness_for_Test_Pressure_t1, Depth, fy, fu, fcb, Pt, Plt, Pe, ExternalPressure, Pb_t1, Pmpt, P_check, UC_prss_cont]

        return UC_prss_cont, P_check, list_variable_names, list_variable 
    
    
        



    except:
        print(f"error code:{random.random()}>>>>>>Error in Pressure Containment System check...")
