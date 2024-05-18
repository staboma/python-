class Kedi:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def miyavla(self):
        return f"{self.isim} miyavladı!"

# Nesne oluşturma
kedi1 = Kedi("Minnak", 2)
print(kedi1.miyavla())
