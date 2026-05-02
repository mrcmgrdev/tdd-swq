def from_roman(roman: str) -> int:
    """Convert a Roman numeral string to an integer."""
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not roman:
        raise ValueError("Roman numeral must not be empty")
    for char in roman:
        if char not in values:
            raise ValueError(f"Invalid character: {char}")
    result = 0
    for i, char in enumerate(roman):
        if i + 1 < len(roman) and values[char] < values[roman[i + 1]]:
            result -= values[char]
        else:
            result += values[char]
    if result > 3999:
        raise ValueError("Roman numeral must not exceed 3999")
    return result
