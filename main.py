from urllib.request import Request, urlopen, urlretrieve, URLopener
from bs4 import BeautifulSoup as bs
import shutil
import os
import re


def get_script(s):
    url = Request(s, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(url)
    soup = bs(html, "html.parser")
    # img = soup.find_all(class_='row w_banner', limit=50)
    img = soup.find_all(class_=re.compile("banner_m"))

    img = str(img).split('"')
    tmp = []
    for i in range(0, len(img)):
        if "src=" in img[i]:
            if img[i+1][0] == '/':
                img[i+1] = s.rstrip('\n') + img[i+1].lstrip(img[i+1][0])
                print(img[i+1])
            tmp.append(img[i + 1])
    return tmp


link_list = []
f = open("Sites.txt", 'r')
link_list = f.readlines()
for link in link_list:
    link = link.strip()
f.close()


tmp = []
for i in link_list:
    tmp.extend(get_script(i))

n = 1
for i in tmp:
    print(i)
    with open(str(n)+'.jpg', 'wb') as h:
        opener = URLopener()
        opener.addheader('User-Agent', 'whatever')
        filename, headers = opener.retrieve(i, str(n)+'.jpg')
        h.close()
        shutil.copy(filename, './img')
        os.remove(filename)
    n += 1


print('다운로드 완료')