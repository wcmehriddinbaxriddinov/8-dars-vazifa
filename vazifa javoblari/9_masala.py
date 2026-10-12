
import csv

katta_xarajatlar = []

with open("cfe8761e-f107-41a2-8864-9a7ebd6c1662/vazifa/expenses_homework.csv", "r") as file:
    reader = csv.DictReader(file)

    for xarajat in reader:
        if int(xarajat["amount"]) > 200:
            katta_xarajatlar.append([xarajat["category"], xarajat["amount"]])

with open("cfe8761e-f107-41a2-8864-9a7ebd6c1662/vazifa/large_expenses.csv", "w") as file:
    writer = csv.writer(file)

    writer.writerow(["category", "amount"])

    for xarajat in katta_xarajatlar:
        writer.writerow(xarajat)

print("Katta xarajatlar yangi faylga yozildi!")
