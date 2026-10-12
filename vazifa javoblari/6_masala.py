import csv

with open("cfe8761e-f107-41a2-8864-9a7ebd6c1662/vazifa/inventory_homework.csv", "r") as file:
    viewer = csv.DictReader(file)
    saqlagich = list(viewer)
    
    eng_kam = saqlagich[0]

    for mahsulot in saqlagich:
        print(f"{mahsulot['item']}, {mahsulot['category']}, {mahsulot['stock']}")
        if int(mahsulot["stock"]) < int(eng_kam["stock"]):
            eng_kam = mahsulot

    print(f"Eng kam qolgan mahsulot: {eng_kam['item']}")
    print(f"Omborda qolgan soni: {eng_kam['stock']}")
