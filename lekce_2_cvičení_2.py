cislo = int(input("Zadejte číslo: "))
if cislo % 3 == 0 and cislo % 5 == 0:
    print("FizzBuzz")
elif cislo % 5 == 0:
    print("Buzz")
elif cislo % 3 == 0:
    print("Fizz")
else:
    print(cislo)
    
    