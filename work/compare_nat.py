#!/usr/bin/env python3

with open ('config.txt') as f1, open('result.txt') as f2:

    lst1 = []

    for line in f2:
        lst1.append(line.strip('\n'))

    for line2 in f1:
        if line2.strip('\n') not in lst1:
            print (line2)