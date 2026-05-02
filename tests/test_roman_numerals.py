import pytest
from src.roman_numerals import from_roman


# Step 1: Basic symbols
@pytest.mark.parametrize("roman, expected", [
    ("I", 1),
    ("V", 5),
    ("X", 10),
    ("L", 50),
    ("C", 100),
    ("D", 500),
    ("M", 1000),
])
def test_basic_symbols(roman, expected):
    assert from_roman(roman) == expected


# Step 2: Repetition
@pytest.mark.parametrize("roman, expected", [
    ("II", 2),
])
def test_repetition(roman, expected):
    assert from_roman(roman) == expected


# Step 3: Addition
@pytest.mark.parametrize("roman, expected", [
    ("VI", 6),
    ("LX", 60),
    ("DC", 600),
])
def test_addition(roman, expected):
    assert from_roman(roman) == expected


# Step 4: Subtraction
@pytest.mark.parametrize("roman, expected", [
    ("IV", 4),
    ("IX", 9),
    ("XL", 40),
    ("XC", 90),
    ("CD", 400),
    ("CM", 900),
])
def test_subtraction(roman, expected):
    assert from_roman(roman) == expected


# Step 5: Complex numbers
@pytest.mark.parametrize("roman, expected", [
    ("XLII", 42),
    ("XCIX", 99),
    ("MMXIII", 2013),
    ("MMMCMXCIX", 3999),
])
def test_complex_numbers(roman, expected):
    assert from_roman(roman) == expected


# Step 6: Empty string / invalid
def test_empty_string_raises_value_error():
    with pytest.raises(ValueError):
        from_roman("")


# Step 7: Out of range and invalid characters
@pytest.mark.parametrize("roman", [
    "MMMM",
    "ABC",
])
def test_invalid_input_raises_value_error(roman):
    with pytest.raises(ValueError):
        from_roman(roman)
