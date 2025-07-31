import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
resposta = requests.get(url)
contagem_preco = 0

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.text, 'html.parser')
    livros_articles = soup.find_all('article', attrs={'class':'product_pod'})
    for livro_article in livros_articles:
        titulo = livro_article.h3.text
        preco = livro_article.find('p', attrs={'class':'price_color'}).text
        link = livro_article.h3.a['href']
        
        print(f"{titulo} - {preco}\n{link}\n")

        if float(preco.replace("Â£", "")) > 50:
            contagem_preco += 1
    
    print(f"Livros que cutam mais de £50: {contagem_preco}")
else:
    print("Não foi possível concluir sua solicitação")