"""
A python module for converting units for distance
"""
convert_factor = 1.61

def miles_to_kilometers(a):
    """
    Convert from miles to kilometers 
    
    PARAMETERS
    ----------
    a : tuple 
        A distance in miles.
        
    RETURNS
    ----------
    distance: float
        Convert a to distance in kilometers.
    """
    return a*convert_factor

def kilometers_to_miles(a):
    """
    Convert from kilometers to miless 
    
    PARAMETERS
    ----------
    a : tuple 
        A distance in kilometers.
        
    RETURNS
    ----------
    distance: float
        Convert a to distance in miles.
    """
    return a/convert_factor
