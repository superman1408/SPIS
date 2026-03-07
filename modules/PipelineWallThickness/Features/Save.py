import csv
import pandas as pd
from tkinter import filedialog
import random
from PyQt5.QtWidgets import QMessageBox


def saveAs(Outside_Diameter_OD, Nominal_Wall_Thickness_tnom, Fabrication_Thickness_Tolerance_tfab, Corrosion_Allowance_tcorr, Ovality_of_Pipe_Oo, SMYS_σsmys, SMTS_σsmts, Derating_value_temp_yieldStress_fy_temp, Derating_value_temp_tensileStress_fu_temp, Youngs_Modulus_E, Poission_s_Ratio_ν, Maximum_Fabrication_Factor_alpha_fab, Material_Strength_Factor_alpha_u, Pd, Material_resistant_factor_gamma_m, Pmin, Elevation_at_Pressure_Reference_Level_href, Elevation_level_at_Pressure_Point_hl, Product_Density_ρcont, Hydrotest_Water_Density_ρt, Incidental_to_Design_Pressure_Ratio_gamma_inc, Water_Depth_WD, Sea_Water_Density_ρsea, Max_Elevation_wrt_MSL_hmax, Min_Elevation_wrt_MSL_hmin, Safety_Class_RF_gamma_SCPC, Safety_Class_RF_gamma_SCLB, System_Pressure_Test_Factor_alpha_spt, Mill_Pressure_Test_Factor_alpha_mpt):
        print(f"\n\tSaving file....!!!")
        try:
                
                filepath = filedialog.asksaveasfilename(
                # os.getenv('home'),
                        initialdir= "C:/Users/DELL/Desktop",
                        title= "Save As",
                        defaultextension= "*.csv",
                        filetypes=(
                                ("csv file","*.csv"),
                                ("HTML file","*.html"),
                                ("text file","*.txt"),
                                ("All file","*.*")
                        )
                )
        except:
                print(f"error code:{random.random()}>>>>>>Error in saving file while opening to write..$$%%^^&&&")
        try:
                if filepath is None:
                        return
                else:
                        with open(filepath, 'w'):
                                df = pd.DataFrame({"SL no" : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29], "INPUTS": ["Outer Diameter OD", "Nominal Wall Thickness tnom", "Fabrication Thickness Tolerance tfab", "Corrosion Allowance tcorr", "Ovality of Pipe Oo", "SMYS σsmys", "SMTS σsmts", "Derating value temp yieldStress fytemp", "Derating value temp tensile Stress futemp", "Youngs Modulus E", "Poission's Ratio ν", "Maximum Fabrication Factor alphafab", "Material Strength Factor alphau", "Design Pressure Pd", "Material resistant factor gamma m", "Pmin", "Elevation at Pressure Reference Level href", "Elevation level at Pressure Point hl", "Product Density ρcont", "Hydrotest Water Density ρt", "Incidental to Design Pressure Ratio gammainc", "Water Depth WD", "Sea Water Density ρsea", "Maximum Elevation wrt MSL hmax", "Minimum Elevation wrt MSL hmin", "Safety Class RF gamma SCPC", "Safety Class RF gamma SCLB", "System Pressure Test Factor alpha spt", "Mill Pressure Test Factor alpha mpt"], "Values": [Outside_Diameter_OD, Nominal_Wall_Thickness_tnom, Fabrication_Thickness_Tolerance_tfab, Corrosion_Allowance_tcorr, Ovality_of_Pipe_Oo, SMYS_σsmys, SMTS_σsmts, Derating_value_temp_yieldStress_fy_temp, Derating_value_temp_tensileStress_fu_temp, Youngs_Modulus_E, Poission_s_Ratio_ν, Maximum_Fabrication_Factor_alpha_fab, Material_Strength_Factor_alpha_u, Pd, Material_resistant_factor_gamma_m, Pmin, Elevation_at_Pressure_Reference_Level_href, Elevation_level_at_Pressure_Point_hl, Product_Density_ρcont, Hydrotest_Water_Density_ρt, Incidental_to_Design_Pressure_Ratio_gamma_inc, Water_Depth_WD, Sea_Water_Density_ρsea, Max_Elevation_wrt_MSL_hmax, Min_Elevation_wrt_MSL_hmin, Safety_Class_RF_gamma_SCPC, Safety_Class_RF_gamma_SCLB, System_Pressure_Test_Factor_alpha_spt, Mill_Pressure_Test_Factor_alpha_mpt]})
                                df.to_csv(filepath)
        except:
            print(f"error code:{random.random()}>>>>>>ERROR in saving your file...!!")
            QMessageBox.warning(None, "Warning", 'File is not saved..!!!!')



