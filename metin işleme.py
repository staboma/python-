import re

metin = "Bu bir test metnidir. Telefon numarası: 123-456-7890. Email: ornek@example.com."

# Telefon numarası bulma
telefon = re.findall(r'\d{3}-\d{3}-\d{4}', metin)
print("Telefon Numarası:", telefon)

# Email adresi bulma
email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', metin)
print("Email Adresi:", email)
