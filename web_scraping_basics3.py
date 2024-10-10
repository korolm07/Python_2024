import requests
import bs4
book_list = []
base_URL = 'http://books.toscrape.com/catalogue/page-{}.html'

for n in range (0,51):
    res = requests.get(base_URL.format(n))
    soup = bs4.BeautifulSoup(res.text,"lxml")
    books = soup.select(".product_pod")
    for book in books:
        if len(book.select('.star-rating.Two')) != 0: 
            book_list.append(book.select('a')[1]['title'])
print (book_list)
    