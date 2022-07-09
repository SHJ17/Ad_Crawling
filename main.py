from urllib.request import Request, urlopen, urlretrieve, URLopener
from bs4 import BeautifulSoup as bs
import shutil
import os


def get_src(s):
    s = str(s)
    s = s.replace("=", " ")
    s = s.split(" ")
    s = s[s.index("src")+1]
    s = s.replace('"', "")
    return s


url = Request('https://marumaru266.com/', headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(url) # url 열기
soup = bs(html, "html.parser")
img = soup.find_all(class_='row w_banner', limit=50)

img = str(img).split('"')
tmp = []
for i in range(0, len(img)):
    if "src=" in img[i]:
        tmp.append(img[i+1])

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