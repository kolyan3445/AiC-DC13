# 14.	Определить количество женщин на борту в возрастном интервале мода  10 лет и сколько из них выжило

import csv
import statistics

with open('titanic.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    age_mode = 0
    age_list = []
    lower_mode_bound = 0
    higher_mode_bound = 0
    counter = 0

    for row in csv_reader:

        if age_mode == 0:
            age_list.append(float({row["Age"]}.pop()))
            age_mode = statistics.mode(age_list)
            lower_mode_bound = age_mode - 10
            higher_mode_bound = age_mode + 10

        if float(row["Survived"]) == 1 and str(row["Sex"]).replace('{', '').replace('}', '').replace(
                "'", '') == 'female' and higher_mode_bound >= float(row["Age"]) >= lower_mode_bound:
            counter += 1

    print("Количество выживших на Титанике женщин в возрастном интервале мода +- 10(от 12 до 32 лет): ", counter)
