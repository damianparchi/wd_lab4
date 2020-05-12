class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print("Nazwa produktu:",self.nazwa_produktu,"\n ilosc:",self.ilosc,"\n jednostka miary:",self.jednostka_miary,"\n cena jednego:",self.cena_jed)

    def ile_produktu(self):
        print(self.ilosc,self.jednostka_miary)
    
    def ile_kosztuje(self):
        print("Razem kosztuje:",self.ilosc*self.cena_jed)






Chleb = NaZakupy("chleb",2,"szt",2)

Chleb.wyswietl_produkt()

Chleb.ile_produktu()
Chleb.ile_kosztuje()