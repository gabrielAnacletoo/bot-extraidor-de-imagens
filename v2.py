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
    url = "https://superopa.com/"
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
    print(f'Acessando {url}')
      # Verifica se há cookies salvos
    if Path("cookies.pkl").is_file():
            with open("cookies.pkl", "rb") as f:
                cookies = pickle.load(f)
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
    
    def ir_categorias():
      sleep(2)
      btn_category = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3.pl-3.text-dark.m-0.carousel-header-title')))
      driver.execute_script("arguments[0].scrollIntoView();", btn_category)
      sleep(2)
      btn_category.click()
    
    try:
        ir_categorias()
        sleep(10)
        # Inicializa uma lista vazia para armazenar os itens de menu clicados
        itens_clicados = []

        # Titulo da categoria
        category_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.row.my-row.category-title.w-100.mb-4'))).text

        # ul menu 
        menu_categorys = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.d-flex.flex-column.text-center.list-group.list-group-flush.p-0.pl-4.pr-4')))
        children_menu = menu_categorys.find_elements(By.CSS_SELECTOR, 'li')

        for item in children_menu:
            texto_item = item.text
            
            # Verifica se o item já foi clicado
            if texto_item not in itens_clicados:
                sleep(2)
                print('Clicando no item:', texto_item)
                item.click()
                sleep(3)
                
                # Adiciona o texto do item à lista de itens clicados
                itens_clicados.append(texto_item)
            else:
                print('Item', texto_item, 'já clicado anteriormente. Pulando...')

        # Div Pai dos elementos
        # container_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.products-card-deck.row.my-row.w-100.align-items-center')))
        
        # # imagens dentro das divs
        # images_elements = container_element.find_elements(By.CSS_SELECTOR, 'img.prod-image')
        # sleep(2)
        # for images_items in images_elements:
        #     save_images([images_items], category_title)
        #     sleep(5)
        #     btn_page_home = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'li.breadcrumb-item')))
        #     btn_page_home.click()
        #     sleep(2)
        #     driver.quit()

        
    except:
        # Aqui você pode adicionar o código que deseja executar caso ocorra uma exceção
        print("O elemento não pôde ser encontrado.")

capture_images()