import math


# ----------------------------- INPUTS DATA ----------------------------------------------
HDPE_density_rho_HDPE = 960
Outside_diameter_OD = 2.3
Concrete_Coating_thickness_t_cc = 0.55
Wall_Thickness_t_HDPE = 88.5 /1000
Volume_of_Concrete_per_meter_of_pipe_Vc = 3.5
Concrete_density_rho_c = 2400
Marine_growth_Thickness_t_mg = 0
Marine_growth_density_rho_mg = 0

Content_density_seawater_rho_cont = 1100
Safety_factor_for_weight_gamma_w = 1.1
Seawater_density_rho_seawater = 1025
gravity_g = 9.807

# --------------------------------------------------- ENVIRONMENT DATA --------------------------------------
Significant_wave_height_Hs = 3.5
Spectral_peak_period_Tp = 13
Water_depth_d = 10.97
Related_angle_btw_pipeline_and_current_direction_teta = 90
Ref_major_height_above_the_seabed_zr = 3

#------------------------------------------------------ SOIL DATA -------------------------------------------------
Sunbmerged_unit_soil_weight_for_sand_gamma_s = 13.5



# ----------------------------------------------------CALCULATIOn--------------------------------------------

Inside_diameter_ID = round((Outside_diameter_OD - 2 * Wall_Thickness_t_HDPE),3)
print("Inside_diameter_ID : ",Inside_diameter_ID)

Hydodynamic_diameter_D = round((Outside_diameter_OD + 2 * (Marine_growth_Thickness_t_mg)+2*Concrete_Coating_thickness_t_cc),3)
print("Hydodynamic_diameter_D : ", Hydodynamic_diameter_D)
# ---------------------------------------------Water Partical Velocity---------------------------------------------

Peak_Enhanchment_factor_phi = round((Spectral_peak_period_Tp /math.sqrt(Significant_wave_height_Hs)),3)
print("Peak_Enhanchment_factor_phi: ", Peak_Enhanchment_factor_phi)

if Peak_Enhanchment_factor_phi <= 3.6 :
    Peakedness_Parameter_gamma = 5
elif 3.6 < Peak_Enhanchment_factor_phi < 5.0 :
    Peakedness_Parameter_gamma = math.exp(5.75 - 1.15*Peak_Enhanchment_factor_phi)
else :
    Peakedness_Parameter_gamma = 1

print("Peakedness_Parameter_gamma: ",Peakedness_Parameter_gamma)

Reference_Period_Tn = round((math.sqrt(Water_depth_d/gravity_g)),3)
print("Reference_Period_Tn: ",Reference_Period_Tn)


Significant_wave_induced_water_particle_velocity_Us = round((Significant_wave_height_Hs/Reference_Period_Tn * 0.4067),3)
print("Significant_wave_induced_water_particle_velocity_Us: ",Significant_wave_induced_water_particle_velocity_Us)

Data_extracted_for_below_figure_2 = round(((Significant_wave_induced_water_particle_velocity_Us * Reference_Period_Tn)/Significant_wave_height_Hs),3)
print("Data_extracted_for_below_figure_2: ",Data_extracted_for_below_figure_2)

# ------------------------------------------------------------- Data_extracted_from_figure_3_2 ---------------------------------------------------------------

Spectrally_Derived_mean_zero_Up_crossing_period_tn_tp = round((Reference_Period_Tn/Spectral_peak_period_Tp),3)
print("Spectrally_Derived_mean_zero_Up_crossing_period tn/tp :  " , Spectrally_Derived_mean_zero_Up_crossing_period_tn_tp)

Mean_zero_up_crossing_period_at_seabed_level_Tu = round((0.8415 * Spectral_peak_period_Tp),3)
print("Mean_zero_up_crossing_period_at_seabed_level_Tu :  ", Mean_zero_up_crossing_period_at_seabed_level_Tu)

Ratio_of_mean_zero_up_crossing_period_to_peak_wave_period_Tu_Tp = round((Mean_zero_up_crossing_period_at_seabed_level_Tu/Spectral_peak_period_Tp),3)
print("Ratio_of_mean_zero_up_crossing_period_to_peak_wave_period_Tu/Tp : ",Ratio_of_mean_zero_up_crossing_period_to_peak_wave_period_Tu_Tp)

# ------------------------------------------------------------------------Input ----------------------------------------------------------------------------------

Reduction_factor_due_to_spectral_directionally_and_spreading_R_D = 1
Angle_btw_wave_and_pipeline_headings_teta_w = 90


# -----------------------------------------------------Calculation-------------------------------------------------------------------
Significant_wave_induced_water_particle_velocity_for_design_UsD  = round((Reduction_factor_due_to_spectral_directionally_and_spreading_R_D * Significant_wave_induced_water_particle_velocity_Us),3)
print("Significant_wave_induced_water_particle_velocity_for_design_UsD : ",Significant_wave_induced_water_particle_velocity_for_design_UsD)


# -------------------------------------------------------------------------------Current Velocity--------------------------------------------------------------
# ----------------------------------------------------input---------------------------------------------------------------------------

Current_velocity_a_distance_Zr_above_the_seabed_Vzr = 0.46
Effective_Seabed_Roughness_z0a = 4/10**5
Friction_coefficient_for_pipe_soil_interface_Mu = 0.6

Characteristic_current_induced_flow_velocity_at_pipeline_level_V = round((Current_velocity_a_distance_Zr_above_the_seabed_Vzr * ((((1+Effective_Seabed_Roughness_z0a/Hydodynamic_diameter_D)* math.log(Hydodynamic_diameter_D/Effective_Seabed_Roughness_z0a +1)) -1)/ math.log(Ref_major_height_above_the_seabed_zr/Effective_Seabed_Roughness_z0a + 1)) * math.sin(math.radians(Related_angle_btw_pipeline_and_current_direction_teta))),3)
print("Characteristic_current_induced_flow_velocity_at_pipeline_level_V : ",Characteristic_current_induced_flow_velocity_at_pipeline_level_V)


if Peakedness_Parameter_gamma == 1.0 :
    Friction_for_calculation_of_kt = 1.25

elif Peakedness_Parameter_gamma == 3.3 :
    Friction_for_calculation_of_kt = 1.21

elif Peakedness_Parameter_gamma == 5 :
    Friction_for_calculation_of_kt = 1.17

print("Friction_for_calculation_of_kt : ",Friction_for_calculation_of_kt)



# Design_single_oscillation_velocity_period_at_seabed_level_T

if Reference_Period_Tn/Mean_zero_up_crossing_period_at_seabed_level_Tu <= 0.2 :
    Design_single_oscillation_velocity_period_at_seabed_level_T = round((Mean_zero_up_crossing_period_at_seabed_level_Tu * (Friction_for_calculation_of_kt - 5* (Friction_for_calculation_of_kt -1 )* (Reference_Period_Tn/Mean_zero_up_crossing_period_at_seabed_level_Tu))),3)
else:
    Design_single_oscillation_velocity_period_at_seabed_level_T = 1
print("Design_single_oscillation_velocity_period_at_seabed_level_T :",Design_single_oscillation_velocity_period_at_seabed_level_T)

Current_to_Wave_Velocity_Ratio_M = round((Characteristic_current_induced_flow_velocity_at_pipeline_level_V/Significant_wave_induced_water_particle_velocity_Us),3)
print("Current_to_Wave_Velocity_Ratio_M : ", Current_to_Wave_Velocity_Ratio_M)

Keulegan_Carpenter_Number_K = round((Significant_wave_induced_water_particle_velocity_Us *Design_single_oscillation_velocity_period_at_seabed_level_T / Hydodynamic_diameter_D),3)
print("Keulegan_Carpenter_Number_K : ",Keulegan_Carpenter_Number_K)



# Peak Load coefficients
Peak_horizontal_load_coefficient_Cy= 4.32
Peak_vertical_load_coefficient_Cz = 3.25

# Weight Calculation

Area_of_pipe_AOD = round((math.pi * Outside_diameter_OD**2 /4),3)
print("Area_of_pipe_AOD : " ,Area_of_pipe_AOD)

Volume_of_pipe_VOD = round((Area_of_pipe_AOD * 1),3)
print("Volume_of_pipe_VOD : " ,Volume_of_pipe_VOD)

Internal_Area_of_pipe_AID = round((math.pi * Inside_diameter_ID**2/4),3)
print("Internal_Area_of_pipe_AID : " ,Internal_Area_of_pipe_AID)

Volume_of_pipe_VID = Internal_Area_of_pipe_AID*1
print("Volume_of_pipe_VID : ", Volume_of_pipe_VID)

Area_of_Thickness_At = round((Area_of_pipe_AOD - Internal_Area_of_pipe_AID ),3)
print("Area_of_Thickness_At : ", Area_of_Thickness_At)

Volume_of_Thickness_Vt = round((Volume_of_pipe_VOD - Volume_of_pipe_VID),3)
print("Volume_of_Thickness_Vt : ", Volume_of_Thickness_Vt)

Mass_of_HDPE_pipe_Mpipe = round((Volume_of_Thickness_Vt * HDPE_density_rho_HDPE),3)
print("Mass_of_HDPE_pipe_Mpipe : ", Mass_of_HDPE_pipe_Mpipe)

Content_mass_inside_pipe_Mseawater = round((Volume_of_pipe_VID * Content_density_seawater_rho_cont),3)
print("Content_mass_inside_pipe_Mseawater : ", Content_mass_inside_pipe_Mseawater)

Buoyancy_for_pipe_Bpipe = round((Volume_of_pipe_VOD * Seawater_density_rho_seawater),3)
print("Buoyancy_for_pipe_Bpipe : ", Buoyancy_for_pipe_Bpipe)

Mass_of_concrete_Mc = round((Concrete_density_rho_c * Volume_of_Concrete_per_meter_of_pipe_Vc),3)
print("Mass_of_concrete_Mc : ", Mass_of_concrete_Mc)

Buoyancy_for_concrete_Bc = round(((Mass_of_concrete_Mc * Seawater_density_rho_seawater)/Concrete_density_rho_c),3)
print("Buoyancy_for_concrete_Bc : ", Buoyancy_for_concrete_Bc)

Submerged_Wt_of_pipe_Wp = round((Mass_of_HDPE_pipe_Mpipe - Buoyancy_for_pipe_Bpipe),3)
print("Submerged_Wt_of_pipe_Wp : ", Submerged_Wt_of_pipe_Wp)

Submerged_Wt_of_concrete_Wc = round((Mass_of_concrete_Mc - Buoyancy_for_concrete_Bc),3)
print("Submerged_Wt_of_concrete_Wc : ", Submerged_Wt_of_concrete_Wc)


# ---------------------------------------------------------------------input ------------------------------------------------------------------------------------
Additional_submerged_weight_W_add = 0

# -------------------------------------------------------------------calculation---------------------------------------------------------------------------------
Total_Submerged_Wt_pipe_concrete_waterfilled_Ws = round((Additional_submerged_weight_W_add + Submerged_Wt_of_pipe_Wp + Submerged_Wt_of_concrete_Wc + Content_mass_inside_pipe_Mseawater),3)
print("Total_Submerged_Wt_pipe_concrete_waterfilled_Ws : ", Total_Submerged_Wt_pipe_concrete_waterfilled_Ws)

Total_Submerged_Wt_pipe_concrete_waterfilled_Ws1 = (Total_Submerged_Wt_pipe_concrete_waterfilled_Ws * gravity_g)/1000
print("Total_Submerged_Wt_pipe_concrete_waterfilled_Ws1", Total_Submerged_Wt_pipe_concrete_waterfilled_Ws1)



# --------------------------------------------------------------------------Load Reduction-------------------------------------------------------------------------------
# (i) Load Reduction due to trenching
Trench_Depth_zt = 3.5
Trench_wall_angle_teta_t = 45


Load_reduction_factor_due_to_trenching_in_horizontal_direction_r_tr_y = round((1.0 - 0.18 * (Trench_wall_angle_teta_t - 5)**0.25 * (Trench_Depth_zt/Hydodynamic_diameter_D)**0.42),3)
print("Load_reduction_factor_due_to_trenching_in_horizontal_direction_r_tr_y : ", Load_reduction_factor_due_to_trenching_in_horizontal_direction_r_tr_y)

Load_reduction_factor_due_to_trenching_in_vertical_direction_r_tr_z = round((1.0 - 0.14 * (Trench_wall_angle_teta_t - 5)**0.43 * (Trench_Depth_zt/Hydodynamic_diameter_D)**0.46),3)
print("Load_reduction_factor_due_to_trenching_in_vertical_direction_r_tr_z : ", Load_reduction_factor_due_to_trenching_in_vertical_direction_r_tr_z)

Appendix_A_Ks = round((((Sunbmerged_unit_soil_weight_for_sand_gamma_s * (Hydodynamic_diameter_D**2))/Total_Submerged_Wt_pipe_concrete_waterfilled_Ws1) ),3)
print("Appendix_A_Ks : ",Appendix_A_Ks)

Initial_Penetration_Zpi = round(((0.037 * Hydodynamic_diameter_D * (Appendix_A_Ks)**(-2/3 )*1000 )/1000),3)
print("Initial_Penetration_Zpi : ", Initial_Penetration_Zpi)


#  (ii) Load reduction factors in horizontal direction


Load_Reduction_Factors_in_Horizontal_Direction_r_pen_y = round(max(1.0 - 1.4 * Initial_Penetration_Zpi/Hydodynamic_diameter_D, 0.3),3)
print("Load_Reduction_Factors_in_Horizontal_Direction_r_pen_y : ", Load_Reduction_Factors_in_Horizontal_Direction_r_pen_y)


Load_Reduction_Factors_in_Horizontal_Direction_r_toty = round((Load_Reduction_Factors_in_Horizontal_Direction_r_pen_y*Load_reduction_factor_due_to_trenching_in_horizontal_direction_r_tr_y),3)
print("Load_Reduction_Factors_in_Horizontal_Direction_r_toty : ",Load_Reduction_Factors_in_Horizontal_Direction_r_toty)

Load_Reduction_Factors_in_Horizontal_Direction_r_perm_z = 0.7

#  (iii) Load reduction factors in vertical direction


if Initial_Penetration_Zpi/Hydodynamic_diameter_D < 0.1 :
    Load_Reduction_Factors_in_Vertical_Direction_r_pen_z = 1
elif (0.1 <= Initial_Penetration_Zpi/Hydodynamic_diameter_D <= 0.869) :
    Load_Reduction_Factors_in_Vertical_Direction_r_pen_z = 1.0 - 1.3* (Initial_Penetration_Zpi/Hydodynamic_diameter_D - 0.1)

elif (Initial_Penetration_Zpi > 0.869):
    Load_Reduction_Factors_in_Vertical_Direction_r_pen_z = 0

print("Load_Reduction_Factors_in_Vertical_Direction_r_pen_z",Load_Reduction_Factors_in_Vertical_Direction_r_pen_z)




Load_Reduction_Factors_in_Vertical_Direction_r_totz = round((Load_Reduction_Factors_in_Vertical_Direction_r_pen_z * Load_Reduction_Factors_in_Horizontal_Direction_r_perm_z * Load_reduction_factor_due_to_trenching_in_vertical_direction_r_tr_z),3)
print("Load_Reduction_Factors_in_Vertical_Direction_r_totz : ", Load_Reduction_Factors_in_Vertical_Direction_r_totz)

# ---------------------------------------------------------------------------- Loads ------------------------------------------------------------------------------


Safety_factor_for_weight_gamma_SC = 1.1

Peak_Horizontal_Load_Fy = round(((Load_Reduction_Factors_in_Horizontal_Direction_r_toty * 0.5 * Seawater_density_rho_seawater * Hydodynamic_diameter_D * Peak_horizontal_load_coefficient_Cy*(Significant_wave_induced_water_particle_velocity_Us + Characteristic_current_induced_flow_velocity_at_pipeline_level_V)**2)),3)
print("Peak_Horizontal_Load_Fy : ",Peak_Horizontal_Load_Fy)



Peak_Vertical_Load_Fz = round((Load_Reduction_Factors_in_Vertical_Direction_r_totz*0.5*Seawater_density_rho_seawater *Hydodynamic_diameter_D * Peak_vertical_load_coefficient_Cz * (Significant_wave_induced_water_particle_velocity_Us + Characteristic_current_induced_flow_velocity_at_pipeline_level_V)**2),3)
print("Peak_Vertical_Load_Fz : ", Peak_Vertical_Load_Fz)


if Appendix_A_Ks <=20:
    Breakout_passive_resistance_F_R_brk = round(((5-0.15 * Appendix_A_Ks) * (Initial_Penetration_Zpi/Hydodynamic_diameter_D)**1.25 * Sunbmerged_unit_soil_weight_for_sand_gamma_s * Hydodynamic_diameter_D**2),3)

else:
    Breakout_passive_resistance_F_R_brk = round((2 * (Initial_Penetration_Zpi/Hydodynamic_diameter_D)**1.25 * Sunbmerged_unit_soil_weight_for_sand_gamma_s * Hydodynamic_diameter_D**2),3)

print("Breakout_passive_resistance_F_R_brk : ", Breakout_passive_resistance_F_R_brk*1000) 


# Lateral Stability criteria
# ---------------------------------------------Lateral Stability Design Criteria (Section 4.5.2 , DNV-RP-F109)----------------------------------------------------

print(Safety_factor_for_weight_gamma_SC * ((Peak_Horizontal_Load_Fy + Friction_coefficient_for_pipe_soil_interface_Mu * Peak_Vertical_Load_Fz)/(Friction_coefficient_for_pipe_soil_interface_Mu * Total_Submerged_Wt_pipe_concrete_waterfilled_Ws1 + Breakout_passive_resistance_F_R_brk))/1000)


print(Safety_factor_for_weight_gamma_SC * (Peak_Vertical_Load_Fz/Total_Submerged_Wt_pipe_concrete_waterfilled_Ws1)/1000)


if (Safety_factor_for_weight_gamma_SC * ((Peak_Horizontal_Load_Fy + Friction_coefficient_for_pipe_soil_interface_Mu * Peak_Vertical_Load_Fz)/(Friction_coefficient_for_pipe_soil_interface_Mu * Total_Submerged_Wt_pipe_concrete_waterfilled_Ws1 + Breakout_passive_resistance_F_R_brk)/1000)) <= 1 :
    LSC_min =  print("SATISFIED")
    if ((Safety_factor_for_weight_gamma_SC * (Peak_Vertical_Load_Fz/Total_Submerged_Wt_pipe_concrete_waterfilled_Ws1))/1000) <= 1:
        print("SATISFIED")

    else:
        print("NOT SATISFIED ")

else:
    print("NOT SATISFIED")





                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

