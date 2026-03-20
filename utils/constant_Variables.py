__version__ = "Constant variables are loaded"

print(__version__)


constant = {
    "density_seawater" : 1025.0,
    "density_water" : 1000.0,
    "density_concrete" : 2400.0,
    "gravity" : 9.807,
    "submerged_unit_soil_weight_for_sand_gamma_s" : 13.5,
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