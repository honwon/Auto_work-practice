from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")

try:
    driver.get("https://cafe.naver.com/joonggonara")

    elem = driver.find_element_by_id("topLayerQueryInput")

    elem.send_keys("자전거")
    elem.send_keys(Keys.RETURN)

    input()
except Exception as e:
    print(e)
finally:
    driver.quit()

