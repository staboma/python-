import csv

# CSV yazma
with open('veriler.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['isim', 'yas'])
    writer.writerow(['Ahmet', 25])
    writer.writerow(['Ayşe', 30])

# CSV okuma
with open('veriler.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
