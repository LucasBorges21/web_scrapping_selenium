from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://books.toscrape.com/catalogue/page-1.html')
driver.maximize_window()
wait = WebDriverWait(driver, 20)

lista_livros = []

while True:
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.col-xs-6.col-sm-4.col-md-3.col-lg-3')))
    cards_livros = driver.find_elements(By.CSS_SELECTOR, '.col-xs-6.col-sm-4.col-md-3.col-lg-3')

    for card in cards_livros:
        try:
            titulo = card.find_element(By.CSS_SELECTOR, 'article.product_pod h3 a').get_attribute('title')
        except:
            titulo = ''

        try:
            preco = card.find_element(By.CSS_SELECTOR, 'div.product_price p.price_color').text
        except:
            preco = ''

        lista_livros.append({
            "Título": titulo,
            'Preço': preco
        })

    try:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.next a')))
        btn_proxima_pagina = driver.find_element(By.CSS_SELECTOR, 'li.next a')
        btn_proxima_pagina.click()
        time.sleep(0.5)

    except TimeoutException:
        break

df_livros = pd.DataFrame(lista_livros)
df_livros.to_excel('livros_scrapping.xlsx', index=False ,engine='openpyxl')

driver.quit()
