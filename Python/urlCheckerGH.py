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
    linkPos = resStr.find(linkBeg)
    while resStr[linkPos] != '\"':
        formsUrl+=resStr[linkPos]
        linkPos+=1
    # Join the array into a single URL
    newUrl = ''.join(formsUrl)
    return newUrl

def verifyUrl(newUrl):
    if "forms" in newUrl:
        callArtisans = "@artisans " + str(newUrl)
        print(callArtisans)
        return callArtisans
    else:
        print("No Google Form present")
        time.sleep(5)
        verifyUrl(newUrl)

def main():
    newUrl = getUrl(url, formsUrl, linkBeg)
    form =verifyUrl(newUrl)
    return str(form)

if __name__ == "__main__":
    main()
