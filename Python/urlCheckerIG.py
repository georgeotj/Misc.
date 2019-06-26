# This script will be used to check to see the link that is visible on a IG account. 
import requests, time
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/nightcaps.keycaps/'
spotInUrl = 427
formsUrl = []

def getUrl(url, spotInUrl, formsUrl):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    results = soup.find_all('script', attrs={'type':'text/javascript'})
    resStr = str(results[3])
    while resStr[spotInUrl] != '\"':
        formsUrl += resStr[spotInUrl]
        spotInUrl+=1
    newUrl = ''.join(formsUrl)
    return newUrl

def verifyUrl(newUrl):
    if "forms" in newUrl:
        callArtisans = "@artisans " + str(newUrl)
        print(callArtisans)
        return callArtisans
    elif "geekhack" in newUrl: 
        print("This is the Geekhack thread: " + newUrl)
        time.sleep(5)
        verifyUrl(newUrl)
    else: 
        print("This might be empty or it might be another link: " + newUrl)
        return newUrl

def main():
    newUrl = getUrl(url, spotInUrl, formsUrl)
    form = verifyUrl(newUrl)
    print(form)
    return str(form)

main()
