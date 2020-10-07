import csv

with open('table.csv', 'r') as file1:
    to_read = csv.reader(file1, delimiter=';')
    R = []
    for ln in to_read:
        R.append(ln)
n = [-200, -200, -200, -200]
R.insert(2,n)
with open('middle_row.csv', 'w') as file2:
    to_write = csv.writer(file2, delimiter=',')
    for ln in R:
        to_write.writerow(ln)
