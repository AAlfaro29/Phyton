# Write a program that reads in colours_20_simple.csv 
# and output the colour data

import csv 


with open("colours_20_simple.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print({line[0]} +" "+ {line[1]} +" "+ {line[2]})

colours = []

print(colours)

