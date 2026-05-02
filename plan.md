# TDD Roman Numerals Converter - Plan

## Ziel

Einen Römische-Zahl-zu-Integer Konverter mittels TDD entwickeln.
Jeder Schritt ist ein einzelner Testfall, der zuerst rot ist, dann grün gemacht wird.

## TDD-Schritte

- [x] Step 1: Grundsymbole — `from_roman("I")` → `1`, `"V"` → `5`, `"X"` → `10`, `"L"` → `50`, `"C"` → `100`, `"D"` → `500`, `"M"` → `1000`
- [x] Step 2: Wiederholung — `from_roman("II")` → `2`
- [ ] Step 3: Addition — `from_roman("VI")` → `6`, `"LX"` → `60`, `"DC"` → `600`
- [ ] Step 4: Subtraktion — `from_roman("IV")` → `4`, `"IX"` → `9`, `"XL"` → `40`, `"XC"` → `90`, `"CD"` → `400`, `"CM"` → `900`
- [ ] Step 5: Komplexe Zahlen — `from_roman("XLII")` → `42`, `"XCIX"` → `99`, `"MMXIII"` → `2013`, `"MMMCMXCIX"` → `3999`
- [ ] Step 6: Leerer String — `from_roman("")` → wirft `ValueError`
- [ ] Step 7: Außerhalb des Bereichs — `from_roman("MMMM")` → wirft `ValueError` (>3999), ungültige Zeichen → `ValueError`
