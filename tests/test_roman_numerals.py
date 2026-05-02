import pytest
from src.roman_numerals import from_roman


# Step 1: Basic symbols ("I"→1, "V"→5, "X"→10, "L"→50, "C"→100, "D"→500, "M"→1000)
def test_I_returns_1():
    assert from_roman("I") == 1

def test_V_returns_5():
    assert from_roman("V") == 5

def test_X_returns_10():
    assert from_roman("X") == 10

def test_L_returns_50():
    assert from_roman("L") == 50

def test_C_returns_100():
    assert from_roman("C") == 100

def test_D_returns_500():
    assert from_roman("D") == 500

# Step 2: Repetition ("II"→2)

# Step 3: Addition ("VI"→6, "LX"→60, "DC"→600)

# Step 4: Subtraction ("IV"→4, "IX"→9, "XL"→40, "XC"→90, "CD"→400, "CM"→900)

# Step 5: Complex numbers ("XLII"→42, "XCIX"→99, "MMXIII"→2013, "MMMCMXCIX"→3999)

# Step 6: Empty string / invalid

# Step 7: Out of range (4000 = "MMMM" not valid, no negative representation)
