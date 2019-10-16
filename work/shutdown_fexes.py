#!/usr/bin/env python3

with open('fexes.txt') as f:
    for line in f:
        line = line.rstrip().split()

        if line:
            fex = line[0]

            print ('interface Port-channel{}'.format(fex) + '\n shutdown')