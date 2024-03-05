from selenium.webdriver.common.by import By
import time
from seleniumbase import Driver
import csv

driver = Driver(uc=True)
driver.maximize_window()

header = ["Brand", "Name", "Size", "Status", "Price", "Image URL"]
with open('category.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)

for i in range(1, 64):
    url = f'https://www.2ndstreet.jp/search?category=910001&other[]=nflg&sortBy=arrival&page={i}'
    print('--- ', url)
    driver.get(url)

    cards = driver.find_elements(By.CLASS_NAME, 'itemCard')
    for j in range(len(cards)):
        card = cards[j]

        try:
            brand = card.find_elements(By.CLASS_NAME, 'itemCard_brand')[0].text
        except:
            brand = ''
        try:
            name = card.find_elements(By.CLASS_NAME, 'itemCard_name')[0].text
        except:
            name = ''
        try:
            size = card.find_elements(By.CLASS_NAME, 'itemCard_size')[0].text
        except:
            size = ''
        try:
            status = card.find_elements(By.CLASS_NAME, 'itemCard_status')[0].text
        except:
            status = ''
        try:
            price = card.find_elements(By.CLASS_NAME, 'itemCard_price')[0].text
        except:
            price = ''
        try:
            image = card.find_elements(By.CSS_SELECTOR, 'div.itemCard_img img')[0].get_attribute('src')
        except:
            image = ''
        
        data = [brand, name, size, status, price, image]
        with open('category.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    
driver.close()
