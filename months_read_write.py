#!/bin/python3

months = open("months.txt")
print(months.read())

for month in months:
    print(month.strip())

months.close()