import requests, time
from bs4 import BeautifulSoup

url = 'https://geekhack.org/index.php?topic=79513.0'
formsUrl = []
linkBeg = "https://forms"

def getUrl(url, formsUrl, linkBeg):
    # Read the page and find the post where ETF posts the links
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    resStr = str(soup.find_all("div", {"id" : "msg_2048390"}))
    # While the string isn't present inside the element of the site wait 5 seconds then retry
    while linkBeg in resStr == False:
        time.sleep(5)
        getUrl(url, formsUrl, linkBeg)
    # When the link does appear in the element, compile the url by going through char by char
    linkPos = resStr.find(linkBeg)
    while resStr[linkPos] != '\"':
        formsUrl+=resStr[linkPos]
        linkPos+=1
    # Join the array into a single URL
    newUrl = ''.join(formsUrl)
    return newUrl

def confirmUrl(newUrl, url, formsUrl, linkBeg):
    if "forms" in newUrl:
        callArtisans = "@artisans " + str(newUrl)
        return callArtisans
    else:
        getUrl(url, formsUrl, linkBeg)

def main():
    newUrl = getUrl(url, formsUrl, linkBeg)
    form = confirmUrl(newUrl, url, formsUrl, linkBeg)
    print(form)
    return str(form)

main()
