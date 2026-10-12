
import csv

ballar = []

with open("cfe8761e-f107-41a2-8864-9a7ebd6c1662/vazifa/exam_results_homework.csv", "r") as file:
    reader = csv.DictReader(file)

    for student in reader:
        ballar.append(int(student["score"]))

eng_yuqori = max(ballar)
eng_past = min(ballar)
ortacha = sum(ballar) / len(ballar)

otganlar = 0

for ball in ballar:
    if ball >= 70:
        otganlar += 1

print(f"Eng yuqori ball: {eng_yuqori}")
print(f"Eng past ball: {eng_past}")
print(f"O'rtacha ball: {ortacha:.2f}")
print(f"70 yoki undan yuqori olganlar soni: {otganlar}")
