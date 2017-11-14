"""
A python module for converting units for temperature
"""

import pytest

from unitconvert.temperature import fahrenheit_to_celsius

def test_celsius_to_fahrenheit():
    # some known results
    assert celsius_to_fahrenheit(0) == 32
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(1, 2, 3, 4)
        
from unitconvert.temperature import celsius_to_fahrenheit        
def test_fahrenheit_to_celsius():
    # some known results
    assert fahrenheit_to_celsius(32) == 0
    with pytest.raises(TypeError):
        fahrenheit_to_celsius(1, 2, 3, 4)

from unitconvert.distance import miles_to_kilometers                
def test_miles_to_kilometers():
    # some known results
    assert abs(miles_to_kilometers(1) - 1.609) < 0.01
    with pytest.raises(TypeError):
        miles_to_kilometers(1, 2, 3, 4)

from unitconvert.distance import kilometers_to_miles
def test_kilometers_to_miles():
    # some known results
    assert abs(kilometers_to_miles(1) - 0.621) < 0.01
    with pytest.raises(TypeError):
        kilometers_to_miles(1, 2, 3, 4)        
