import json

veri = '{"ad": "Ahmet", "yas": 25, "sehir": "İstanbul"}'
kisi = json.loads(veri)
print("Ad:", kisi["ad"])
print("Yaş:", kisi["yas"])
print("Şehir:", kisi["sehir"])
