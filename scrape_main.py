from mail_server import mail_server
from corona_scraper import corona_scraper
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

class main:

    def __init__(self):
        self.spam_johan()

    def spam_johan(self):
        #server = mail_server('erik.jareman@gmail.com', 'johan.alsteryd@hotmail.se')
        scraper = corona_scraper('https://www.worldometers.info/coronavirus/')

        while True:
            #totalcases = scraper.get_total_cases()
            #server.send_total_cases(totalcases)

            driver = webdriver.Chrome(executable_path=r'C:\Users\Erik\Downloads\chromedriver_win32.zip')
            driver.get('https://www.google.co.in')
            print("Page Title is : %s" % driver.title)
            link = driver.find_element_by_link_text('Gmail')
            driver.execute_script('arguments[0].target="_blank";', link)
            link.click()
            wait = WebDriverWait(driver, 5)
            wait.until(EC.number_of_windows_to_be(2))
            driver.switch_to.window(driver.window_handles[-1])
            wait.until(EC.title_contains("Gmail"))
            print("Page Title is : %s" % driver.title)



            time.sleep(60*10)

main()