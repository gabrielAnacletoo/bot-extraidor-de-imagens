import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import requests

# Função para salvar as imagens em pastas separadas
def save_images(images, folder_name):
    if not os.path.exists(f'images/{folder_name}'):
        os.makedirs(f'images/{folder_name}')

    for index, image in enumerate(images):
        image_link = image.get_attribute('src')
        image_data = requests.get(image_link).content
        with open(f'images/{folder_name}/image_{index}.png', 'wb') as f:
            f.write(image_data)
            print(f'Imagem {index} salva com sucesso em {folder_name}')
            
def capture_images():
    urls = [ 'https://superopa.com/categoria?categoryId=d39d5730-8110-4698-81a3-f6e84c2a3231&loja=greenstore&categoryName=promo%C3%A7%C3%B5es&',
    'https://superopa.com/categoria?categoryId=a5497d10-2cdf-11ee-9e1b-f57970b52ced&loja=greenstore&categoryName=latic%C3%ADnios&',
    'https://superopa.com/categoria?categoryId=cbf8f500-2d1f-11ed-b770-fbc004be3af6&loja=greenstore&categoryName=mercearia-b%C3%A1sica&',
    'https://superopa.com/categoria?categoryId=d7cf0ee0-3067-11ee-8b47-316bf68dcc87&loja=greenstore&categoryName=mercearia-doce&',
    'https://superopa.com/categoria?categoryId=d44e7930-8f24-11ec-8d79-81306b66cbf7&loja=greenstore&categoryName=mercearia-salgada&',
    'https://superopa.com/categoria?categoryId=a6a132f0-2ce1-11ee-9e1b-f57970b52ced&loja=greenstore&categoryName=massas&',
    'https://superopa.com/categoria?categoryId=2651c500-95ac-11ed-a5a3-93d81ba6ae3f&loja=greenstore&categoryName=snacks&',
    'https://superopa.com/categoria?categoryId=4ed15c10-8f28-11ec-9484-f515b67cf416&loja=greenstore&categoryName=bomboniere&',
    'https://superopa.com/categoria?categoryId=d3b1aa10-f608-11ec-ade7-2355a2d55947&loja=greenstore&categoryName=saud%C3%A1veis-e%20veganos&',
    'https://superopa.com/categoria?categoryId=c90b92b0-a941-11ec-a64f-933289e50e1f&loja=greenstore&categoryName=refrigerantes-e%20energ%C3%A9ticos&',
    'https://superopa.com/categoria?categoryId=451a7960-94e4-11ec-86ab-bb592113ad9e&loja=greenstore&categoryName=outras-bebidas&',
    'https://superopa.com/categoria?categoryId=b7edf7b0-2cdb-11ee-b54d-f10087d57bea&loja=greenstore&categoryName=cervejas&',
    'https://superopa.com/categoria?categoryId=abffcc80-94a7-11ec-8923-e9cbabea8e81&loja=greenstore&categoryName=bebidas-alco%C3%B3licas&',
    'https://superopa.com/categoria?categoryId=9d623640-957e-11ec-8327-099feffb788b&loja=greenstore&categoryName=casa-e%20limpeza&',
    'https://superopa.com/categoria?categoryId=53ffb620-95b1-11ec-bf66-8b826dc6ea1a&loja=greenstore&categoryName=cuidado-pessoal&',
    'https://superopa.com/categoria?categoryId=e9b58460-95b1-11ec-92f3-0d32e1de73b0&loja=greenstore&categoryName=pets&'
    ]
   
    opt = Options()
    opt.add_argument("--disable-notifications")
    opt.add_argument("--log-level=3")
    opt.add_argument("--disable-dev-shm-usage")
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    opt.add_argument("--disable-extensions")
    opt.add_argument("test-type")
    opt.add_argument("--disable-logging")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    for key, value in headers.items():
        opt.add_argument(f"--{key}={value}")

    driver = webdriver.Chrome(options=opt)
    wait = WebDriverWait(driver, 10)

    for url in urls:
        try:
            driver.get(url)
            print(f'Acessando {url}')
            sleep(10)

            # Titulo da categoria
            category_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.row.my-row.category-title.w-100.mb-4'))).text

            # Div Pai dos elementos
            container_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.products-card-deck.row.my-row.w-100.align-items-center')))

            # imagens dentro das divs
            images_elements = container_element.find_elements(By.CSS_SELECTOR, 'img.prod-image')
            sleep(2)
            save_images(images_elements, category_title)
            # for images_items in images_elements:
            #      save_images([images_items], category_title)

        except Exception as e:
            print(f"Ocorreu um erro: {str(e)}")
            continue

    driver.quit()

capture_images()