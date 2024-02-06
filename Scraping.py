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

  
  discount_price = product.find('span', class_='andes-money-amount__fraction')
  discount_cents = product.find('span', class_='andes-money-amount__cents andes-money-amount__cents--superscript-16')

  # Se o preço com desconto for encontrado, use-o
  if discount_price and discount_cents:
       price_real = discount_price.text
       price_cents = discount_cents.text
  elif discount_price and not discount_cents:
        price_real = discount_price.text
        price_cents = '00'
  elif discount_cents and not discount_price:
        price_real = '0'
        price_cents = discount_cents.text
  else:
        original_price = product.find('span', class_='andes-money-amount ui-pdp-price__part ui-pdp-price__original-value andes-money-amount--previous andes-money-amount--cents-superscript andes-money-amount--compact')
        original_cents = product.find('span', class_='andes-money-amount__cents andes-money-amount__cents--superscript-16')


        if original_price and original_cents and discount_price and discount_cents:
            price_real = discount_price.text
            price_cents = discount_cents.text
        elif original_price and original_cents:
            price_real = original_price.text
            price_cents = original_cents.text
        else:
            return 'Preço não encontrado.'

  return price_real + ',' + price_cents
    

def product_link(product):
    link = product.find('a', attrs={'class':"ui-search-item__group__element ui-search-link__title-card ui-search-link"}).get('href')
    return link



if __name__ == '__main__':
    product_result = search_product(search_product)
    print(f"Nome do produto: \n {product_name(product_result)}")
    print(" ")
    print(f"Preço do produto: \n {product_price(product_result)}")
    print(" ")
    print(f"Link do produto: \n {product_link(product_result)}")
    print(" ")
    print("Fim da pesquisa.")