class Slowa:
    def __init__(self,sl1,sl2):
        self.sl1 = sl1
        self.sl2 = sl2

    def czy_palindrom(self):
        w1 = [x for x in self.sl1]
        w2 = []
        i=1
        for x in w1:
            w2.append(self.sl1[-i])
            i = i + 1
        if w2 == w1:
            return print("sa palindromami")
        else:
            return 0

    def czy_metagramy(self):
        w1 = [x for x in self.sl1]
        w2 = [x for x in self.sl2]
        i = 0
        ile = 0
        for x in self.sl1:   #tylko musza miec tyle samo liter
            if w1[i] != w2[i]:  
                ile = ile +1
            i = i + 1      
        if ile == 1:
            return "wyraz rozni sie 1 litera"
        else:
            return 0

    # def czy_anagramy(self): # brak pomyslow 

    def wyswietl_wyrazy(self):
        print(self.sl1)
        print(self.sl2)


x = Slowa('kajak','kajaa')

x.czy_palindrom()
print(x.czy_metagramy())
x.wyswietl_wyrazy()