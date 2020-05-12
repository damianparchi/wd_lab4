def liczby(ile):
    A = [x for x in range(0,ile,4)]
    return A

print(liczby(1000))

plik = open("plik1.py", "w+")
plik.writelines(str(liczby(1000)))
plik.close()