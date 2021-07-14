#!/home/uniholder/anaconda3/bin/python
import sys

for line in sys.stdin:
    for token in line.strip().split(' '):
        if token: print('\t'.join([token, '1']))
