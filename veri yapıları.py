data = {
    'isim': 'Ahmet',
    'yas': 25,
    'dersler': [
        {'isim': 'Matematik', 'not': 90},
        {'isim': 'Fizik', 'not': 85}
    ]
}

# Ders notlarını yazdırma
for ders in data['dersler']:
    print(f"{ders['isim']} dersinden alınan not: {ders['not']}")
