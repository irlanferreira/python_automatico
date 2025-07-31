import requests
from bs4 import BeautifulSoup

# url = "http://quotes.toscrape.com/"

# resposta = requests.get(url)
# if resposta.status_code == 200:
#     soup = BeautifulSoup(resposta.text, "html.parser")
#     frases = soup.find_all('span', attrs={'class':'text'})
#     for frase in frases:
#         print(frase.text)

url = "http://books.toscrape.com/"
resposta = requests.get(url)

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.text, 'html.parser')
    livros_articles = soup.find_all('article', attrs={'class':'product_pod'})
    for livro_article in livros_articles:
        titulo = livro_article.h3.text
        preco = livro_article.find('p', attrs={'class':'price_color'}).text

        print(f"{titulo} - {preco}")

else:
    print("Não foi possível concluir sua solicitação")