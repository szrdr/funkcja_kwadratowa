def oblicz_miejsce_zerowe(a,b,c):
    import math

    # Dodanie potrzebnych zmiennych
    parametr_a = a
    parametr_b = b
    parametr_c = c

    # Obliczanie delty
    delta = pow(parametr_b, 2) - 4 * parametr_a * parametr_c

    if delta >= 0:  # sprawdza czy delta jest dodatnia
        try:
            miejsce_zerowe1 = (-parametr_b + math.sqrt(delta)) / (2 * parametr_a)
            miejsce_zerowe2 = (-parametr_b - math.sqrt(delta)) / (2 * parametr_a)
            return miejsce_zerowe1, miejsce_zerowe2  # zwraca mniejsca zerowe
        except ZeroDivisionError:
            print("Nie ma takiej funkcji. Wprowadź poprawne dane")
    else:  # sprawdza czy delta jest ujemna
        try:
            delta_zespolona = complex(0, math.sqrt(-delta))
            miejsce_zerowe1 = (complex(-parametr_b, 0) + delta_zespolona) / (complex(2 * parametr_a, 0))
            miejsce_zerowe2 = (complex(-parametr_b, 0) - delta_zespolona) / (complex(2 * parametr_a, 0))
            return miejsce_zerowe1, miejsce_zerowe2  # zwraca mniejsca zerowe
        except ZeroDivisionError:
            print("Nie ma takiej funkcji. Wprowadź poprawne dane")

# test
print(oblicz_miejsce_zerowe(0,0,0)) #zwraca ((-1+1.4142135623730951j), (-1-1.4142135623730951j))