class ciagi:
    def __init__(self,a1,n,r):
        self.a1=a1
        self.n=n
        self.r=r

    def wyswietl_dane(self):
        print("a1 =",self.a1,"\nn =",self.n,"\nr =",self.r)
    
    def pobierz_element(self):
        a1 = input('podaj a1:')
        n = input('podaj n:')
        r = input('podaj r:')

    def pobierz_parametry(self):
        a1 = input('podaj a1:')
        r = input('podaj r:')
        n = input('podaj ilosc:')
    
    def policz_sume(self):
        an = self.a1 + (self.n-1)*self.r
        suma = (self.a1 + an)/2*self.n
        return suma

x=ciagi(4,5,6)

x.wyswietl_dane()
x.pobierz_element()
print(x.policz_sume())