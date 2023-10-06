# pricelist.py

"""
Pricelist for various vehicle components.

The cost values represent base prices for various vehicle components,
such as chassis, tire, and engine.

These values can be utilized across various modules where the cost 
calculation for assembling a vehicle is required. Should any pricing
need adjustment simply update this file.

Note: All prices are given in SEK (Swedish Krona).

Attributes:
    CAR_CHASSIS (float): Base price for a car chassis.
    CAR_TIRE (float): Base price for a car tire.
    CAR_ENGINE_MTRL (float): Material cost for a car engine.
    CAR_ENGINE_FIT_COEF (float): 
    Fitting coefficient for car engine sizing cost calculations based
    on engine size.

    MOTORCYCLE_CHASSIS (float): Base price for a motorcycle chassis.
    MOTORCYCLE_TIRE (float): Base price for a motorcycle tire.
    MOTORCYCLE_ENGINE_MTRL (float): Material cost for a motorcycle engine.
    MOTORCYCLE_ENGINE_FIT_COEF (float): 
    Fitting coefficient for motorcycle engine sizing cost calculations
    based on engine size.

    BICYCLE_CHASSIS (float): Base price for a bicycle chassis.
    BICYCLE_TIRE (float): Base price for a bicycle tire.
"""

# CAR PARTS
CAR_CHASSIS = 50_000  # SEK
CAR_TIRE = 3_000  # SEK
CAR_ENGINE_MTRL = 25_000  # SEK
CAR_ENGINE_FIT_COEF = 59.50  # SEK

# MOTORCYCLE PARTS
MOTORCYCLE_CHASSIS = 20_000  # SEK
MOTORCYCLE_TIRE = 2_000  # SEK
MOTORCYCLE_ENGINE_MTRL = 15_000  # SEK
MOTORCYCLE_ENGINE_FIT_COEF = 44.50  # SEK

# BICYCLE PARTS
BICYCLE_CHASSIS = 2_000  # SEK
BICYCLE_TIRE = 800  # SEK