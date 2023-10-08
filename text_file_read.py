import csv
with open("train.txt") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)