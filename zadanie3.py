with open("plik3.py","w") as plik3:
    tekst = input('Wpisz tekst: ')
    plik3.writelines(tekst)

with open("plik3.py","r") as plik3:
    for linia in plik3:
        print(linia)