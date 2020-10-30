from selenium import webdriver
import os

base_dir=os.path.dirname(os.path.realpath(__file__))

driver = webdriver.Chrome(os.path.join(base_dir,"chromedriver.exe"))

driver.get("https://cafe.naver.com/joonggonara")