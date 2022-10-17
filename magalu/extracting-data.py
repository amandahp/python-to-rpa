from itertools import product
from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By

import pyautogui as waitingTime
import pyautogui as keyboardFunctions

def Magalu(address, id, content_search, class_name):
  products = {"refrigerators": []}
  driver = seleniumOptions.Chrome()
  driver.get(address)

  driver.find_element(By.ID, id).send_keys(content_search)
  waitingTime.sleep(2)
  keyboardFunctions.press("enter")
  waitingTime.sleep(10)
  
  
  products = {"product_name":[],"price": []}
  
  products_list = driver.find_elements(By.TAG_NAME, "ul")
  for item in products_list:
    try:
      product_name = item.find_element(By.PARTIAL_LINK_TEXT, "Gel").text
    except:
      pass
    

  
      
      


Magalu("https://www.magazineluiza.com.br/?partner_id=974&gclid=CjwKCAjw-rOaBhA9EiwAUkLV4ntLIsOZboowafRPPR94t-XLNUoiIVGQMWRdlz_kQGMFy7y9Y2TL3RoCmDcQAvD_BwE&gclsrc=aw.ds",
"input-search", "geladeira", "botGsS")

