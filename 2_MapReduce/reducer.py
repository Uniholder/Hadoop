#!/home/uniholder/anaconda3/bin/python
import sys

last_key, sum_ = None, 0

for line in sys.stdin:
    key, value = line.strip().split('\t')
    if last_key and key != last_key:
        print('\t'.join([last_key, str(sum_)]))
        last_key, sum_ = key, int(value)
    else:
        last_key, sum_ = key, sum_ + int(value)

if last_key:
    print('\t'.join([last_key, str(sum_)]))
