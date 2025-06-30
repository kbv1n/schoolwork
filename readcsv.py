import csv 
file = 'input1.csv'

with open(f'{file}', 'r') as f:
    print(file.reader())