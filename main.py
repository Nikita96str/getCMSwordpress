import requests
from bs4 import BeautifulSoup

def wordpress_by_url(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    meta = soup.find_all("meta")
    cmsWordPress = False
    if "wordpress" in str(meta).lower():
        cmsWordPress = True
    else:
        robots = requests.get(url + "/robots.txt")
        if robots.text.find("wp-") != -1:
            cmsWordPress = True
        else:
            pass
    return cmsWordPress


inputURL = input("Введите URL:")
if wordpress_by_url(inputURL):
    print("Сайт сделан с помощью WordPress")
else:
    print("Сайт сделан с помощью другой технологии")