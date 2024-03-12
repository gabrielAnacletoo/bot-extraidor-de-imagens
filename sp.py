import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from pathlib import Path
import pickle
import os
import requests




def capture_images():
    #url = "https://superopa.com/"
    url = "https://superopa.com/categoria?categoryId=d39d5730-8110-4698-81a3-f6e84c2a3231&loja=greenstore&categoryName=promo%C3%A7%C3%B5es&"
    opt = Options()
    opt.add_argument("--disable-notifications")
    #opt.add_argument("--headless")
    opt.add_argument("--log-level=3")
    opt.add_argument("--disable-dev-shm-usage")
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    opt.add_argument("--disable-extensions")
    opt.add_argument("test-type")
    opt.add_argument("--disable-logging")

      # Adicione os headers aqui 
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    for key, value in headers.items():
     opt.add_argument(f"--{key}={value}")

    driver = webdriver.Chrome(options=opt)
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    
      # Verifica se há cookies salvos
    if Path("cookies.pkl").is_file():
            with open("cookies.pkl", "rb") as f:
                cookies = pickle.load(f)
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
        
    try:
        sleep(5)
        # btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.carousel-category-card.cursor-pointer.default-box-shadow')))
        # accept_cookie = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#btnAcceptCookie')))
        # accept_cookie.click()
       
        sleep(10)
        # btn.click()


        container_products = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.products-card-deck.row.my-row.w-100.align-items-center')))
        
        ul_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.list-group w-100.border-pattern.bg-white.default-box-shadow')))
        li_element = ul_element.find_elements(By.CSS_SELECTOR, 'li')
        print(len(li_element))
        # if not os.path.exists('images'):
        #     os.makedirs('images')
        # sleep(5)  
        
        #  # Encontrar todas as divs dentro do container
        # images = container_products.find_elements(By.CSS_SELECTOR, 'img.prod-image')
        #  # Iterar sobre as imagens para obter os links
        # # for image in images:
        # #     image_link = image.get_attribute('src')
        # #     print("Link da imagem:", image_link)
        # for index, image in enumerate(images, start=-1):
        #     image_link = image.get_attribute('src')
        #     image_data = requests.get(image_link).content
        #     with open(f'images/image_{index}.png', 'wb') as f:      
        #         f.write(image_data)
        #         print(f'Imagem {index} salva com sucesso')          
    except:
        # Aqui você pode adicionar o código que deseja executar caso ocorra uma exceção
        print("O elemento não pôde ser encontrado.")

capture_images()