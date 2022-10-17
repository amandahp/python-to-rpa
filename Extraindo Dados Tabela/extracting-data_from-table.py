from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By

import pandas as pd 

def Table(address, tableElement, tableRow, tableColumn):
  table = { "tableRows": [], "tableColumns": []}

  driver = seleniumOptions.Chrome()
  driver.get(address)
  
  element = driver.find_element(By.XPATH, tableElement)
  rows = element.find_elements(By.TAG_NAME, tableRow)
  columns = element.find_elements(By.TAG_NAME, tableColumn)
  
  row = 0
  for actualRow in rows:
    table["tableRows"].append(actualRow.text)
    
    row += 1
  
  column = 0
  for actualColumn in columns:
    table["tableColumns"].append(actualColumn.text)

    column += 1
  
  dataFrame = pd.DataFrame(table["tableRows"], columns=['Nome_coluna'])
  file = pd.ExcelWriter("data.xlsx", engine='xlsxwriter')
  
  dataFrame.to_excel(file, sheet_name='Sheet1', index=False)
  file.save()
  

#Table("https://rpachallengeocr.azurewebsites.net/","//*[@id='tableSandbox']", "tr", "td")

