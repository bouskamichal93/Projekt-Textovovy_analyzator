cislo_1 = float(input("Zadejte první číslo: "))
cislo_2 = float(input("Zadejte druhé číslo: "))

if cislo_1 == cislo_2:
    print("Obě čísla jsou stejná")
else:
    if cislo_1 > cislo_2:
        print("První číslo je větší než druhé")
    elif cislo_1 < cislo_2:
        print("První číslo je menší než druhé")

    