__version__ = "0.0.1"

print(f"Loading constants and variables for version {__version__}...")


constant = {
    "beta" : 3.14,
    "density_seawater" : 1025.0,
    "density_water" : 1000.0,
    "density_concrete" : 2400.0,
    "gravity" : 9.807,
    "submerged_unit_soil_weight_for_sand_gamma_s" : 13.5,

    # constant value for free span analysis

    "Fixed_Fixed": 4.73,
    "Pinned_Pinned": 3.14,
    "Fixed_Pinned": 3.93,
    "Steel_density": 7850,
    "Concrete_Density": 3040,
    "Water_Density": 1030,
    "Youngs_Modulus": 2.07 * 10**11,
}

caseOption = {
        "Lateral Stability": [
            "Installation-Empty",
            "Operation-Content Filled"],
        "Vertical Stability": [
            "Installation-Empty",
            "Operation-Content Filled",
            "Operation-Shutdown-Empty"
        ]
    }



allInputMap = {
    "Lateral Stability": [
        "rho_HDPE_lineEdit", "OD_lineEdit","concrete_coating_thickness_lineEdit",
        "tHDPE_lineEdit","Vc_lineEdit","rho_c_lineEdit","mg_thickness_lineEdit","mg_density_lineEdit",
        "rho_cont_lineEdit","yw_lineEdit","Hs_lineEdit","Tp_lineEdit","d_lineEdit",
        "related_angle_theta_lineEdit","zr_lineEdit","ys_lineEdit"
    ],

    "Vertical Stability": [
        "rho_HDPE_lineEdit", "OD_lineEdit","tHDPE_lineEdit",
        "CA_lineEdit","Vc_lineEdit","rho_c_lineEdit","rho_cont_lineEdit","yw_lineEdit"
    ]
}

# 👉 Required inputs per module
requiredInputMap = {
    "Lateral Stability": allInputMap["Lateral Stability"],

    "Vertical Stability": allInputMap["Vertical Stability"],
}


# 👉 Helper functions
def get_all_inputs():
    all_inputs = set()
    for inputs in allInputMap.values():
        all_inputs.update(inputs)
    return list(all_inputs)


def get_required_inputs(module):
    return requiredInputMap.get(module, [])


