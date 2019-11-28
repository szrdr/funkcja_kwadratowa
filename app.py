def oblicz_miejsce_zerowe(a,b,c):
    import cmath
    import math

    # Dodanie potrzebnych zmiennych
    parametr_a = a
    parametr_b = b
    parametr_c = c
    delta = 0
    miejsce_zerowe1 = 0
    miejsce_zerowe2 = 0

    # Obliczanie delty
    delta = pow(parametr_b, 2) - 4 * parametr_a * parametr_c

    if delta >= 0:  # Sprawdzanie czy delta jest dodatnia
        miejsce_zerowe1 = (-parametr_b + math.sqrt(delta)) / (2 * parametr_a)
        miejsce_zerowe2 = (-parametr_b - math.sqrt(delta)) / (2 * parametr_a)
        print(f"Miejsce zerowe 1: {miejsce_zerowe1}")
        print(f"Miejsce zerowe 2: {miejsce_zerowe2}")
    else:  # Sprawdzanie czy delta jest ujemna
        delta_zespolona = complex(0, math.sqrt(-delta))
        miejsce_zerowe1 = (complex(-parametr_b, 0) + delta_zespolona) / (complex(2 * parametr_a, 0))
        miejsce_zerowe2 = (complex(-parametr_b, 0) - delta_zespolona) / (complex(2 * parametr_a, 0))
        print(f"Miejsce zerowe 1: {miejsce_zerowe1}")
        print(f"Miejsce zerowe 2: {miejsce_zerowe2}")

oblicz_miejsce_zerowe(1,2,3)