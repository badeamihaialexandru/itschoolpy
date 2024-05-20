def minim():
    a=int(input("Introduceti un nr a: "))
    b=int(input("Apoi introduceti un nr b, pentru a verifica care este cel mai mic dintre acestea 2: "))
    if a<b:
        print(f'Numarul {a} este cel mai mic dintre {a} si {b}')
    else:
        print(f'Numarul {b} este cel mai mic  dintre {a} si {b}')

minim()

