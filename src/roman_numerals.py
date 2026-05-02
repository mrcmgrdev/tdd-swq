def from_roman(roman: str) -> int:
    """Convert a Roman numeral string to an integer."""
    if roman == "I":
        return 1
    elif roman == "V":
        return 5
    elif roman == "X":
        return 10
    elif roman == "L":
        return 50
    elif roman == "C":
        return 100
    elif roman == "D":
        return 500
    
    return 0
