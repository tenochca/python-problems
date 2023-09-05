'''The article is long, so it is split up between 4 pages. Your task is to print out the 
text to the screen so that you can read the full article without having to click any buttons.'''

import requests
from bs4 import BeautifulSoup

def getHtml(url):
    'get html from url'
    r = requests.get(url) #http request for html code
    r_html = r.text #converts unicode to readible text
    return r_html #returns readable html

def getSoup(html):
    'creats bs4 object using built in parser'
    soup = BeautifulSoup(html, features = 'html.parser') #create beautiful soup object
    return soup #return the soup

def getText():
    'returns the condensed article text'
    url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    code = getHtml(url) #calling getHtml function
    soup = getSoup(code) #use html to call getSoup function
    for text in soup.find_all('p'):
        articletext = text.get_text().replace(" ", "").strip()
        print(articletext)
    return articletext

if __name__ == '__main__':
    print(getText())
