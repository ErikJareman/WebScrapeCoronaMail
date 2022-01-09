import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class corona_scraper:

    URL = ''
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/81.0.4044.92 Safari/537.36'}

    def __init__(self, URL):
        self.URL = URL

    def get_total_cases(self):
        page = requests.get(self.URL, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        totalcases = soup.find(attrs={'maincounter-number'}).get_text()

        return totalcases.replace(',', '')

    def seleniumTest(self):

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