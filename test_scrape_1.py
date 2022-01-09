import requests
from bs4 import BeautifulSoup
import smtplib
import time


def get_total_cases():
    URL = 'https://www.worldometers.info/coronavirus/'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup.prettify())

    totalcases = soup.find(attrs={'maincounter-number'}).get_text()

    spam_johan(totalcases.replace(',', ''))

def spam_johan(string):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('erik.jareman@gmail.com', '*******')

    subject = 'Total Cases'
    body = 'World:' + string

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('erik.jareman@gmail.com', 'johan.alsteryd@hotmail.se', msg)

    print(string)
    server.quit()

while True:
    get_total_cases()
    time.sleep(60 * 2)