#ZADANIE 1================
plik = open("zad2.py","r")
wiersze = plik.readlines()
#ZADANIE 2================
with open("zad2.py","r") as plik:
    for linia in plik:
        print(linia,end="")

print("\n")

plik.close()

print(wiersze)
print("\n")
#ZADANIE 3============================
with open("dozad3.py","r+") as plik:
    for linia in plik:
        print(linia,end="")

print("\n")


#ZADANIE 4=======================================================
class NaZakupy():
    nazwa_produktu = "bułka" 
    ilosc = 4
    jednostka_miary = "gram" 
    cena_jed = 1
    def __init__ (self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed


wyswietl_produkt = NaZakupy('chleb', "1", " bochenek" , 3)
ile_produktu = NaZakupy('chleb', "1", " bochenek" , 3)
ile_kosztuje = NaZakupy('ziemniak', 3, " kg" , 2)


print(wyswietl_produkt.nazwa_produktu)

print(ile_produktu.ilosc + ile_produktu.jednostka_miary)

print(ile_kosztuje.ilosc * ile_kosztuje.cena_jed)

#zadanie 5==============
class ciagi_arytmetyczne:
    def __init__(self, pierwszy_wyraz_ciagu, różnica, długość_ciągu, Suma_ciągu):
        self.pierwszy_wyraz_ciagu = pierwszy_wyraz_ciagu
        self.różnica = różnica
        self.długość_ciągu = długość_ciągu
        self.Suma_ciągu = Suma_ciągu
    def wyświetl_dane(self):
        print("a1 =", self.pierwszy_wyraz_ciagu, "\n różnica ciągu to: r = ", self. różnica),
        print("długość ciągu to: ", self.długość_ciągu, "\n Suma ciągu o długości", self.długość_ciągu, "wynosi: S= ", self.Suma_ciągu)
    def pobierz_elementy(self):
        x=input("podaj elementy ciągu: ")
        print(x)
    def pobierz_parametry(self, pierwszy_wyraz_ciagu, róznica, długość_ciągu):
        self.pierwszy_wyraz_ciagu = pierwszy_wyraz_ciagu
        self.róznica = róznica
        self.długość_ciągu = długość_ciągu
        i=0
        licznik = 1
        an = 0
        while licznik<= self.długość_ciągu:
            an = self.pierwszy_wyraz_ciagu + (licznik-1)*self.róznica
            licznik += 1
        Suma_ciągu = ((self.pierwszy_wyraz_ciagu + an) /2) * self.długość_ciągu
        print("\n\n",an)
        print(licznik)
        print(Suma_ciągu,"essa")
    def policz_elementy(self, pierwszy_wyraz_ciagu, róznica, Suma_ciągu):
        self.pierwszy_wyraz_ciagu = pierwszy_wyraz_ciagu
        self.różnica = róznica
        długość_ciągu = Suma_ciągu/róznica
        print(długość_ciągu)

ciagi = ciagi_arytmetyczne(1, 2, 15, 500)
#ciagi.pobierz_elementy()
ciagi1.pobierz_parametry(1,2,10)
ciag1.policz_sume(1,4,10)
ciag1.policz_elementy(1,2,100)

#ZADANIE 6===============================
class slowa:
    def __init__(self,x,y):
        self.wyraz1=x
        self.wyraz2=y
    def sprawdz_czy_palindrom(self):
        if(len(self.wyraz1)%2==0):
            for i in range(0,int(len(self.wyraz1)/2-1)):
                if(self.wyraz1[i]!=self.wyraz1[len(self.wyraz1)-i-1]):
                    return print("wyraz nie jest palindromem")
        else:
            for i in range(0,int((len(self.wyraz1)-1)/2)):
                if(self.wyraz1[i]!=self.wyraz1[len(self.wyraz1)-i-1]):
                    return print("wyraz nie jest palindromem")
        return print("wyraz1 jest palindromem.")
    def sprawdz_czy_metagramy(self):
        if(len(self.wyraz1)!=len(self.wyraz2)):
            return print("wyrazy nie sa metagramami")
        else:
            count=0
            for i in range(0,len(self.wyraz1)-1):
                if (self.wyraz1[i]!=self.wyraz2[i]):
                    count+=1
                    if(count>1):
                        return print("wyrazy nie sa metagramami")
        if(count!=1):
            return print("wyrazy nie sa metagramami")

        return print("wyrazy nie sa metagramami")
    def sprawdz_czy_anagramy(self):
        if(len(self.wyraz1)!=len(self.wyraz2)):
            return print("wyrazy nie sa anagramami")
        else:
            for i in range (0,len(self.wyraz1)):
                if(self.wyraz1.count(self.wyraz1[i])!=self.wyraz2.count(self.wyraz1[i])):
                    return print("wyrazy nie sa anagramami")
        return print('wyrazy sa anagramami')
    def wyswietl_wyraz(self):
        print(self.wyraz1)
        print(self.wyraz2)

wyrazy=slowa('mata,tama')
wyrazy.sprawdz_czy_palindrom()
wyrazy.sprawdz_czy_metagramy()
wyrazy.sprawdz_czy_anagramy()
wyrazy.wyswietl_wyraz()    
        


#ZADANIE 7 ================================
import math
class Robaczek:
    def __init__(self,x,y,krok):
        self.x=x
        self.y=y
        self.krok=krok
    def idz_w_gore(self,ilosc_krokow):
        wynik=ilosc_krokow * self.krok
        self.y=self.y+wynik
        return self.y
    def idz_w_dol(self,ilosc_krokow):
        wynik=ilosc_krokow * self.krok
        self.y=self.y-wynik
        return self.y
    def idz_w_lewo(self,ilosc_krokow):
        wynik=ilosc_krokow * self.krok
        self.x=self.x-wynik
        return self.x
    def idz_w_prawo(self,ilosc_krokow):
        wynik=ilosc_krokow * self.krok
        self.x=self.x + wynik
        return self.x
    def twoje_wspolrzedne(self):
        return print(f"twoje wspolrzedne to : ({self.x},{self.y})") 
robak=Robaczek(1,1,1)
robak.idz_w_gore(2)
robak.idz_w_lewo(1)
robak.idz_w_dol(5)
robak.idz_w_prawo(1)
robak.twoje_wspolrzedne()