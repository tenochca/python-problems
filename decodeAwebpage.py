'''Use the BeautifulSoup and requests Python packages 
to print out a list of all the article titles on the New York Times homepage.'''

import requests
from bs4 import BeautifulSoup

def getHtml(url):
    'get html from url'
    r = requests.get(url) #http request for html code
    r_html = r.text #converts unicode to readible text
    return r_html #returns readable html

def getSoup(html):
    'creats bs4 object using built in parser'
    soup = BeautifulSoup(html, features = 'html.parser') #creat beautiful soup object
    return soup #return the soup

def getTitles():
    'returns the article titles in the webpage'
    titles = [] #inint list to store titles
    url = 'https://www.nytimes.com/' #NY times url
    code = getHtml(url) #calling getHtml function
    soup = getSoup(code) #use html to call getSoup function
    for title in soup.find_all('h3'): #iterate through the <h3 tags in soup
        titles.append(title.get_text()) #append the text in those tags to the list
    return titles #return the list of titles

def main(): 
    print(getTitles())

if __name__ == "__main__":
    main()