# Seoul Subway > 위키디피아 서울 지하철
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway'
response = requests.get(url)
#print(response)
#print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)
#print(soup.head)
print(soup.title.string)

# 지하철 사진 가져오기
target_img = soup.find('img, attr{'alt': "Seoul Metro 2000 series train in Line2')

# 이미지 소스 가져오기
target_img _rc = target_img.get('src')
# print(target_im

#