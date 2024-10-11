import requests
import bs4

res = requests.get ('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text,"lxml")
 
#list of unique authors on 1st page: 
authors_list = []
page = soup.select ('.quote')
for one_quote in page: 
    author = one_quote.find(class_= "author").text
    authors_list.append(author)
unique_list = set (authors_list)
#print (unique_list)

#all quotes on 1st page: 
quote_list = []
for one_quote in page: 
    quote = one_quote.find(class_='text').text
    quote_list.append(quote)
#print (quote_list)

# quotes from right side of page 
tags = soup.find_all(class_='tag-item')  
tags_list = []
for one_tag in tags: 
    tag = one_tag.text.strip()
    tags_list.append(tag)
#print (tags_list)


#All unique authors on website
authors_list = set ()
n=0
page_template = 'http://quotes.toscrape.com/page/{}/'
page_still_valid = True

while page_still_valid:
    n+=1
    scrape_url = page_template.format(n)
    res = requests.get(scrape_url)
    if "No quotes found!" in res.text:
        page_still_valid = False
        break
    soup = bs4.BeautifulSoup(res.text,"lxml")
    for name in soup.select (".author"):  
        authors_list.add(name.text)
print (authors_list)
