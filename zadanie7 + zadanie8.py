class Robaczek:
    def __init__(self,x,y,krok):
        self.x = x
        self.y = y
        self.krok = krok
    
    def w_gore(self,ile):
        ruch = ile * self.krok
        self.y = self.y + ruch
        return self.y

    def w_dol(self,ile):
        ruch = ile * self.krok
        self.y = self.y - ruch
        return self.y

    def w_lewo(self,ile):
        ruch = ile * self.krok
        self.x = self.x - ruch
        return self.x
    
    def w_prawo(self,ile):
        ruch = ile * self.krok
        self.x = self.x + ruch
        return self.x
    
    def gdzie_jestes(self):
        print("X=",self.x,"\nY=",self.y)

    def __del__(self):
        return

x = Robaczek(0,0,1)
x.w_lewo(5)
x.w_gore(1)
x.w_dol(2)
x.w_prawo(2)
x.gdzie_jestes()
del x
