#!/usr/bin/env python
# http://stackoverflow.com/questions/1159524/how-to-replace-a-column-in-a-csv-file-in-python
# See: http://docs.python.org/library/csv.html
from __future__ import with_statement

import csv

def twiddle_csv(file1, file2):
    def mess_with_record(record):
        record['90mdist'] = 2 * int(record['90mdist']) + 30
    with open(file1, "r") as fin:
        with open(file2, "w") as fout:
            fields = ['ID', 'transect', '90mdist']
            reader = csv.DictReader(fin, fieldnames=fields)
            writer = csv.DictWriter(fout, fieldnames=fields)
            fout.write(",".join(fields) + '\n')
            reader.next()   # Skip the column header
            for record in reader:
                mess_with_record(record)
                writer.writerow(record)

if __name__ == '__main__':
    twiddle_csv('1159524-file1', 'file2')
