import csv

with open('table.csv', 'r') as file1:
    to_read = csv.reader(file1, delimiter=';')
    R = []
    for ln in to_read:
        R.append(ln)       
for ln in R:
    if ln == R[0]:
        ln.append("my_col")
    else:
        ln.append("True")
with open('new_col.csv', 'w') as file2:
    to_write = csv.writer(file2, delimiter=',')
    for ln in R:
        to_write.writerow(ln)
