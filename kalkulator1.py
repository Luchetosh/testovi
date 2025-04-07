print("Kalkulator (+, -, /, *)")

def kalkulator():
    try:
        broj1 = float(input("Unesi prvi broj: "))
        print("Izaberij operaciju:\n 1 = +\n 2 = -\n 3 = *\n 4 = /")
        operacija = int(input("Operacija: "))
        broj2 = float(input("Unesi drugi broj: "))
    except ValueError:
        print("Unesi tocan broj ili operaciju!!!")
        return None

    if operacija == 1:
        rezultat = broj1 + broj2
    elif operacija == 2:
        rezultat = broj1 - broj2
    elif operacija == 3:
        rezultat = broj1 * broj2
    elif operacija == 4:
        if broj2 == 0:
            print("ERROR, Djeljenje s nulom nije moguce. ")
            return None
        rezultat = broj1 / broj2
    else:
        print("Nepoznata operacija. ")
        return None
    
    return rezultat

rez = kalkulator()
if rez is not None:
    print(f"Rezultat: {rez}")