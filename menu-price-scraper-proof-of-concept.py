from bs4 import BeautifulSoup
import urllib2
import re

menu_page = 'https://www.themodernnyc.com/menus/#dinner-1'
page = urllib2.urlopen(menu_page)
soup = BeautifulSoup(page, 'html.parser') ##creates the beautiful soup object

##looks for the first tag with the html attribute 'data-slug: dinner-1'
##inside that match, finds all p tags, takes the last one
##gets text from inside the last p tag
price = soup.find(attrs={'data-slug':'dinner-1'}).find_all("p")[-1].getText()

##regex match for digits inside price
match = re.search(r'\d{2,}',price)
print(match.group())
