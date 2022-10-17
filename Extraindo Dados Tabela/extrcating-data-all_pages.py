from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By

import pyautogui as waitingTime


def Table(address, tableElement, tableRow, tableColumn, pages, buttonPath):
  table = { "tableRows": [], "tableColumns": []}

  driver = seleniumOptions.Chrome()
  driver.get(address)
  
  row = 0
  i = 0
  while i < pages:
    element = driver.find_element(By.XPATH, tableElement)
    rows = element.find_elements(By.TAG_NAME, tableRow)
    columns = element.find_elements(By.TAG_NAME, tableColumn)
    
    for actualRow in rows: 
      table["tableRows"].append(actualRow.text)
      print(actualRow.text)
      row += 1
      
    
    i += 1
    waitingTime.sleep(3)
    driver.find_element(By.XPATH, buttonPath).click()
    waitingTime.sleep(3)
  else:
    print("Success!")
  

#Table("https://rpachallengeocr.azurewebsites.net/","//*[@id='tableSandbox']", "tr", "td", 3, "//*[@id='tableSandbox_next']")

