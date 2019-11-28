# Dodanie potrzebnych zmiennych
parametr_a = int(input("Podaj parametr a: "))
parametr_b = int(input("Podaj parametr b: "))
parametr_c = int(input("Podaj parametr c: "))
delta = 0
miejsce_zerowe1 = 0
miejsce_zerowe2 = 0

# Obliczanie delty

delta = pow(parametr_b, 2) - 4 * parametr_a * parametr_c

# Sprawdzanie czy delta jest dodatnia lub ujemna

if delta >= 0:
    miejsce_zerowe1 = (-parametr_b + delta)/(2*parametr_a)
    miejsce_zerowe2 = (-parametr_b - delta)/(2*parametr_a)
    print(f"Miejsce zerowe 1: {miejsce_zerowe1}")
    print(f"Miejsce zerowe 2: {miejsce_zerowe2}")
else:
    print('delta ujemna')

