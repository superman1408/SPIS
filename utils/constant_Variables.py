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

# analysisOption = {
#         "Lateral Stability": [
#             "Installation-Empty",
#             "Operation-Content Filled"],
#         "Vertical Stability": [
#             "Installation-Empty",
#             "Operation-Content Filled",
#             "Operation-Shutdown-Empty"
#         ]
#     }

