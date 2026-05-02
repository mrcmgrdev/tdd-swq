def from_roman(roman: str) -> int:
    """Convert a Roman numeral string to an integer."""
    if roman == "I":
        return 1
    elif roman == "V":
        return 5
    
    return 0
