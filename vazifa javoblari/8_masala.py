
import csv

with open("cfe8761e-f107-41a2-8864-9a7ebd6c1662/vazifa/cities_homework.csv", "r") as file:
    reader = csv.DictReader(file)

    for shahar in reader:
        if int(shahar["population"]) > 500000:
            print(f"{shahar["city"]}, {shahar["population"]}")
