class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def tanit(self):
        print("Araba:", self.marka, self.model, self.yil)

araba1 = Araba("Toyota", "Corolla", 2020)
araba1.tanit()
