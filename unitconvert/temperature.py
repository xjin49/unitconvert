"""
A python module for converting units for temperature
"""

def fahrenheit_to_celsius(a):
    """
    Convert from fahrenheit to celsius 
    
    PARAMETERS
    ----------
    a : tuple 
        A distance in fahrenheit.
        
    RETURNS
    ----------
    distance: float
        Convert temperature to celsius.
    """
    return (a-32)/1.8

def celsius_to_fahrenheit(a):
    """
    Convert from celsius to fahrenheit 
    
    PARAMETERS
    ----------
    a : tuple 
        A distance in celsius.
        
    RETURNS
    ----------
    distance: float
        Convert temperature to fahrenheit.
    """
    return a*1.8+32

