# temperature.py

from bs4 import BeautifulSoup #import bs4
from urllib.request import urlopen
import csv
from datetime import datetime


def writecsv(data):

    date = datetime.now().strftime('%Y-%m-%d')
    
    with open('data-temperature.csv','a',newline='',encoding='utf-8') as file:
        filewriter = csv.writer(file)
        filewriter.writerow(data)
alldata = {}

def checktemp(ID):
    url = 'https://www.tmd.go.th/weather/province/prachinburi' + str(ID)

    webopen = urlopen(url) #เปิด web โดยไม่ต้องเปิด chrome
    html_page = webopen.read() #.decode('utf-8)
    webopen.close() #ปิดเว็บ

    data= BeautifulSoup(html_page,'html.parser') # แปลง code ให้ bs4 ช่วยแปล

    try:
        temp = data.find('h2',{'class':'txt_temp'})
        title = data.find('h1',{'class':'text-dark1'})

        city = title.text
        temp = temp.text
        #print(city,temp)
        alldata[city] = temp
    except:
        pass

for i in range(1,101):
    checktemp(i)

#print(alldata[''])

for k,v in alldata.items():
    data = [k,v]
    writecsv(data)

print('saved')

#print(title.text) #.strip() ฟังก์ชันของข้อความ ตัด space ด้านหน้าและหลังของข้อความ
#print(temp.text)



#def checktemp(ID):
#for i  in range(1,101):
    #print(i)
    #checktemp(i)
    #print('---------')
#checktemp()

