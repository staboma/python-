class Hayvan:
    def __init__(self, isim):
        self.isim = isim

    def ses_cikar(self):
        pass

class Kedi(Hayvan):
    def ses_cikar(self):
        return f"{self.isim} miyavladı!"

class Kopek(Hayvan):
    def ses_cikar(self):
        return f"{self.isim} havladı!"

kedi = Kedi("Minnak")
kopek = Kopek("Karabaş")

print(kedi.ses_cikar())
print(kopek.ses_cikar())
