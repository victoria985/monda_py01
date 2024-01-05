""" Komandinio darbo / savarankiška užduotis
===[ Biudžetas ]===

Reikalavimai

* Biudžeto turinys - pajamų/išlaidų žurnalo žodynas
** raktas - paskirtis
** reikšmė - pajamos pozityvus float, išlaidos negatyvus float
* Galimybė pridėti pajamas arba išlaidas
* Spausdinti pajamų/išlaidų žurnalą
* Suskaičiuoti biudžeto balansą

"""
def likutis(biudzetas, lesos: str, suma: float):
    if lesos in biudzetas:
        biudzetas[lesos] += suma
    else:
        biudzetas[lesos] = suma
    return biudzetas

def pajamos(biudzetas, lesos: str, suma: float):
    if lesos in biudzetas:
        biudzetas[lesos] += suma
    else:
        biudzetas[lesos] = suma
    return biudzetas

def islaidos(biudzetas, lesos: str, suma: float):
    if lesos in biudzetas:
        biudzetas[lesos] -= suma
    else:
        biudzetas[lesos] = -suma
    return biudzetas

def finansu_judejimas(biudzetas):
    print('Pajamų/Išlaidų istorija:')
    for index, (lesos, suma) in enumerate(biudzetas.items()):
        if suma > 0:
            print(f'{index}. Pajamos ({lesos}): {suma:.2f} €')
        elif suma < 0:
            print(f'{index}. Išlaidos ({lesos}): {suma:.2f} €')
        else:
            print(f'{index}. {lesos}: {suma:.2f} €')

def balansas(biudzetas):
    balansas = 0
    for suma in biudzetas.values():
        balansas += suma
    return balansas

def main():
    biudzetas = {}

    while True:
        print("""
            === Pasirenkam eiga:===
        0: Baigti nepradėjus
        1: Įvesti likučio sumą, jeigu buvo likes likutis          
        2: Pridėti pajamas
        3: Minusuoti išlaidas     
        4: Spausdinti biudžeto judėjimą
        5: Balansas
        """)
        pasirinkimas = input('Pasirinkimas (0-5): ')
        
        if pasirinkimas == '0':
            print('Programa baigta. Have a nice day!:)')
            break
        elif pasirinkimas == "1":
            lesos = input('Įveskite prašom lėšų reikšmę: ')
            suma = float(input('Įveskite prašom sumą: '))
            biudzetas = likutis(biudzetas, lesos, suma)
        elif pasirinkimas == "2":
            lesos = input('Įveskite prašom lėšų reikšmę: ')
            suma = float(input('Įveskite prašom sumą: '))
            biudzetas = pajamos(biudzetas, lesos, suma)
        elif pasirinkimas == "3":    
            lesos = input('Įveskite prašom lėšų reikšmę: ')
            suma = float(input('Įveskite prašom sumą: '))
            biudzetas = islaidos(biudzetas, lesos, suma)
        elif pasirinkimas == "4":
            finansu_judejimas(biudzetas)
        elif pasirinkimas == "5":
            print(f'Balansas: {balansas(biudzetas):.2f} €')
        else:
            print('Klaida. Bandykite dar kartą.')
main()





         
                    



 





