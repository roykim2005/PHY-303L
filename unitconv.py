units = {
    "m" : 1,
    "cm" : 1e-2,
    "mm" : 1e-3,
    "microm" : 1e-6,
    "nm" : 1e-9,
    "pm" : 1e-12
}

value = float(input("Enter a value: "))
current_unit = input("Current unit (m, cm, mm, microm, nm, pm): ").strip()
new_unit = input("New unit ((m, cm, mm, microm, nm, pm): ").strip()
dimension = int(input("Dimension of the unit: "))
num_or_den = input("Numerator or denominator? (type n or d): ")

current = units[current_unit]
new = units[new_unit]

converted = current / new
if num_or_den == "n":
    result = (converted * value) ** dimension
    print(f"{result:.3e} {new_unit}^{dimension}")
elif num_or_den == "d":
    result = 1 / ((converted * value) ** dimension)
    print(f"{result:.3e} {new_unit}^{-dimension}")
