from urllib.request import Request, urlopen, urlretrieve, URLopener
from bs4 import BeautifulSoup as bs
import shutil
import os

url = Request('https://marumaru266.com/', headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(url) # url 열기
soup = bs(html, "html.parser")
img = soup.find_all(class_='col-md-3 col-sm-6 col-xs-6 banner_m', limit = 50) #클래스가 _img인 사진 50장으로 제한
print(img)

n = 1

def get_src(s):
    s = str(s)
    s = s.replace("=", " ")
    s = s.split(" ")
    s = s[s.index("src")+1]
    s = s.replace('"', "")
    return s


for i in img:     # 이미지를 50개 저장하기 위한 반복문
    print(i)
    print(type(i))
    i = get_src(i)
    print(type(i))
    print(i)

    with open(str(n)+'.jpg', 'wb') as h:     # 이미지 + 사진번호 + 확장자는 jpg
        opener = URLopener()
        opener.addheader('User-Agent', 'whatever')
        filename, headers = opener.retrieve(i, str(n)+'.jpg')
        h.close()
        shutil.copy(filename, './img')
        os.remove(filename)
    n += 1
print('다운로드 완료')


