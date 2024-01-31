import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

#Utilizar findAll no product para fazer com varios produtos
def search_product(search_product):
    product_name = input('Digite o produto que deseja pesquisar: ') #input para o usuário digitar o produto que deseja pesquisar
    
    response = requests.get(url_base + product_name) #fazendo a requisição do site
   
    site = BeautifulSoup(response.text, 'html.parser') #transformando o site em um objeto BeautifulSoup
    
    product = site.find('div', attrs={'class':"ui-search-result__wrapper"}) #procurando a div que contém as informações do produto
    if product:
        return product
    else:
        not_find = 'Produto não encontrado.'
        return not_find

def product_name(product):
    name = product.find('h2', attrs={'class':"ui-search-item__title"}).text
    return name

def product_price(product):
    price_real = product.find('span', attrs={'class':"andes-money-amount__fraction"}).text
    price_cents = product.find('span', attrs={'class':"andes-money-amount__decimals"}).text
    # discounted_price = product.find('span', attrs={'class':"andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript"}).text
    if (price_cents):
        return price_real, price_cents
    else:
        return price_real



def product_link(product):
    link = product.find('a', attrs={'class':"ui-search-item__group__element ui-search-link__title-card ui-search-link"}).get('href')
    return link
    


if __name__ == '__main__':
    print(product_name(search_product(search_product)))
    print(product_price(search_product(search_product)))
    print(product_link(search_product(search_product)))
