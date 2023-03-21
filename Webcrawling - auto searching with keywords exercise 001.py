from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

query_txt = input("What is your crawling keywords?")

# Chrome web browser execution by Chrome driver
path = "C:/Users/chois/Desktop/Jupyter codes/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)

# driver.get("https://korean.visitkorea.or.kr/main/main.do#home")
# driver.get("https://daum.net")

driver.get("https://www.naver.com")

# Wait 2 seconds for opening the home page
time.sleep(2)

# Input keywords in the search text box
# driver.find_element_by_id("btnSearch").click()

element = driver.find_element(By.ID , 'query')

element.send_keys(query_txt)

# Click the search button for execution of searching

# driver.find_element(By.LINK_TEXT, ("search_btn")).click()