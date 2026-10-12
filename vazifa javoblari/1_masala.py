import csv

with open("cfe8761e-f107-41a2-8864-9a7ebd6c1662/vazifa/employees_homework.csv", "r") as file:
    viewer = csv.DictReader(file)
    saqlagich = list(viewer)

    for xodim in saqlagich:
        print(f"{xodim["name"]}, {xodim["department"]}, {xodim["salary"]}")