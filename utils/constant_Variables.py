__version__ = "0.0.1"

print(f"Loading constants and variables for version {__version__}...")


constant = {
    "beta" : 3.14,
    "gravity" : 9.807,
    "submerged_unit_soil_weight_for_sand_gamma_s" : 13.5,
    "Steel_density": 7850,
    "Concrete_Density": 3040,
    "density_seawater" : 1030.0,
    "Water_Density": 1000,
    "Air_Density" : 1.2,
    "Youngs_Modulus": 2.07 * 10**11,
}

PIPE_GRADES = {
    "A25": 172,
    "B": 241,
    "X42": 290,
    "X46": 317,
    "X52": 359,
    "X56": 386,
    "X60": 414,
    "X65": 450,
    "X70": 483,
    "X80": 552,
}


BOUNDARY_CONDITIONS = {
    "Fixed-Fixed": 4.73,
    "Pinned-Pinned": 3.14,
    "Fixed-Pinned": 3.93,
}

Boundary_Library = {
    
    "Pinned-Pinned": {
        "beta": 3.142,
        "deflection_factor": 5,
        "moment_factor": 1/8
    },

    "Fixed-Pinned": {
        "beta": 3.927,
        "deflection_factor": 2.6,
        "moment_factor": 1/10
    },

    "Fixed-Fixed": {
        "beta": 4.730,
        "deflection_factor": 1,
        "moment_factor": 1/12
    }
}


Content_Type_For_Installation = {
    "Light Crude": 800,
    "Medium Crude": 870,
    "Heavy Crude": 950,
    "Condensate": 750,
    "Gas": 120
}


# | Criterion | Meaning              |
# | --------- | -------------------- |
# | L/180     | Very flexible        |
# | L/240     | Moderate             |
# | L/360     | Typical              |
# | L/384     | Strict               |
# | L/500     | Very Strict          |
# | L/1000    | Precision structures |

Deflection_Criteria = {
    "Very Flexible": 180,
    "Moderate": 240,
    "Typical": 360,
    "Strict": 500,
    "Precision Structures": 1000,
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


