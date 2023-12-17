import requests
from bs4 import BeautifulSoup

def get_books(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text,"html.parser")
  books = soup. find_all("li", class_= 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
  for book in books:
      book_soup = BeautifulSoup(str(book),"html.parser")
      book = book_soup.find('h3').find('a').get('title')
      print(book)
      price = book_soup.find('div', class_='product_price').find('p', 
      class_ = 'price_color').text
      new_price = price.replace('Â','')
      print(new_price)

def give_books():
    url="https://books.toscrape.com/catalogue/category/books/classics_6/index.html"
    get_books(url)
give_books()
