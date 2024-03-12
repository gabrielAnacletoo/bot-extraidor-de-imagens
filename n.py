import requests
from bs4 import BeautifulSoup

url = "https://superopa.com/home/?loja=greenstore"

# Definir os headers desejados
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Enviar uma solicitação GET com os headers personalizados
response = requests.get(url, headers=headers)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Criar um objeto BeautifulSoup para analisar o conteúdo HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')

    container = soup.find('div', class_='products-card-deck row my-row w-100 align-items-center')

    if container:
        img_elements = container.find_all('img')
        
        # Iterar sobre os elementos <img> e exibir os links das imagens
        for img in img_elements:
            img_link = img['src']
            print("Link da imagem:", img_link)
    else:
        print("Elemento <img> não encontrado.")
else:
    print("Erro ao acessar a página:", response.status_code)
