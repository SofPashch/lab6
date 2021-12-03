from bs4 import BeautifulSoup
import requests

url = input('Вставте посилання на сторінку: \n')

def parse(url):
    r = requests.get(url)
    s = BeautifulSoup(r.content, 'html.parser')
    return s

page = parse(url)
content = page.find('div', 'content-article')

def inside():
    r = requests.get(url)
    s = BeautifulSoup(r.content, 'html.parser')
    k = BeautifulSoup(r.text, 'html.parser')
    i = 0
    for link in s.find_all('a', href=True):
        i+=1
        text = page.find('div', 'content-article')
        images = len([tag.name for tag in page.find_all('img')])
        links = len([tag.name for tag in page.find_all('link')])
        tags = len([tag.name for tag in page.find_all()])
    l = 0
    for anchor in k.find_all('a', href=True,):
      l += len(anchor['href'])
    print('Частота появи слів у тексті на цій сторінці: ', l)
    print('Зображень: ', images)
    print('Тегів: ', tags)
    print('Посилань: ', links)
print(inside())