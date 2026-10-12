import csv

with open("cfe8761e-f107-41a2-8864-9a7ebd6c1662/vazifa/students_homework.csv", "r") as file:
    viewer = csv.DictReader(file)
    saqlagich = list(viewer)
    
    for student in saqlagich:
        if int(student["score"]) >= 85:
            print(f"{student["name"]}, {student["age"]}, {student["score"]}")