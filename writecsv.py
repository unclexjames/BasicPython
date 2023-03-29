# writecsv.py

import csv
from datetime import datetime


def writecsv(data):

    date = datetime.now().strftime('%Y-%m-%d')
    
    with open('data-temperature.csv','a',newline='',encoding='utf-8') as file:
        filewriter = csv.writer(file)
        filewriter.writerow(data)


writecsv([' ', ])
