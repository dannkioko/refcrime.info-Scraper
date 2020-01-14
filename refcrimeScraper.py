from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import csv

url = "https://www.refcrime.info/en/Crime/Chronology?Day=13&Month=1&Year=2020"

#add header to request
try:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    #open a connection and grab the page
    page = urlopen(req)

    page_htm = page.read()

    page.close()
except Exception as e:
    print("Error Occured")

page_html = BeautifulSoup(page_htm, "html.parser")
crimes = page_html.findAll("div",{"class":"crimeBox"})
with open("test.csv","wt") as file:
    writer = csv.writer(file)
    writer.writerow(('id', 'city', 'date','summary'))
    for crime in crimes:
        id = crime.find("span",{"class":"crimeCounter"}).text
        city = crime.find("span",{"class":"crimeCity"}).text
        date = ""
        summary = crime.find("div",{"class":"faded"}).text
        writer.writerow((id, city, date, summary))


