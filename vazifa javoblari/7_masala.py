
import csv

ism = input("Student ismini kiriting: ")
yosh = int(input("Student yoshini kiriting: "))
ball = int(input("Student ballini kiriting: "))

if ball >= 70:
    with open("cfe8761e-f107-41a2-8864-9a7ebd6c1662/vazifa/new_students_homework.csv", "a") as file:
        viewer = csv.writer(file)
        viewer.writerow([ism, yosh, ball])

    print("Student CSV faylga qo'shildi!")
else:
    print("Ball 70 dan past. Fayl o'zgartirilmadi.")
