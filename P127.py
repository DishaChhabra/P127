from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

browser = webdriver.Chrome('./chromedriver.exe')
browser.get(url)
time.sleep(10)

def get_data():
    headers = ['Proper name',	'Distance (ly)',	'Mass (M☉)',	'Radius (R☉)']
    data = []
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    table = soup.find("table")
    for a in table.find_all('tr'):
            td = a.find_all('td')
            temp = []
            for w,o in enumerate(td):
                if w == 0:
                    try: 
                        temp.append(o.find_all('a')[0].contents[0])
                    except:
                        temp.append("")
                    
                else:
                    temp.append(o.contents[0])
            data.append(temp)
    print(data[0:5])
    with open('pdata.csv', 'w',encoding="utf-8") as file:
        Writer = csv.writer(file)
        Writer.writerow(headers)
        Writer.writerows(data)  

get_data()
