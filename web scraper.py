import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/andre/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
results = []
content = driver.page.source
soup = BeautifulSoup(content)
driver.quit()

for element in soup.findAll(attrs='lazyload-wrapper'):
    name = element.find('h2')
    if name not in results:
        results.append(name.text)
df = pd.Dataframe({'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')