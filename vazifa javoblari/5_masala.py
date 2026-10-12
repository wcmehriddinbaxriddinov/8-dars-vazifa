import csv

with open("cfe8761e-f107-41a2-8864-9a7ebd6c1662/vazifa/orders_homework.csv", "r") as file:
    viewer = csv.DictReader(file)
    saqlagich = list(viewer)
    
    umumiy = 0
    
    for key in saqlagich:
        print(f"{key['order_id']}, {key['customer']}, {key['amount']}")
        umumiy += int(key["amount"])

ortacha = umumiy / len(saqlagich)
print(f"Umumiy buyurtmalar narxi - {umumiy}")
print(f"Umumiy buyurtmalarnign ortacha narxi - {ortacha}")
print(len(saqlagich))