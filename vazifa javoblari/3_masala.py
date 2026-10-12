import csv

with open("cfe8761e-f107-41a2-8864-9a7ebd6c1662/vazifa/books_homework.csv", "r") as file:
    viewer = csv.DictReader(file)
    saqlagich = list(viewer)
    
    count = 0
    for books in saqlagich:
        if int(books["year"]) >= 2021:
            print(f"{books["title"]}, {books["author"]}, {books["year"]}")
            count += 1
            print(f"2021 dan keyingi kitoblar soni - {count}")