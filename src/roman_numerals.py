def from_roman(roman: str) -> int:
    """Convert a Roman numeral string to an integer."""
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for char in roman:
        result += values[char]
    return result
