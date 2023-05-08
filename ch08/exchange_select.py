# select_one(태그요소, 선택자 이름) - 1개 선택
# select(태그요소, 선택자 이름) - 전체 검색(리스트로 반환)



import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
response = requests.get(url)

html = BeautifulSoup(response.text, 'html.parser')
ul = html.select_one('ul.data_list')
first_li = ul.select_one('')
print(first_li)
exchange = first_li.select_one('span.blind')
print(exchange.string)
exchange = first_li.select_one('span.value')
print(value.string)

# 전체 환율 정보
all_li = ul.select('ul.data.lst li')
# print(all_li)
for li in all_li:
    exchange = li.select_one('span.blind')
    value= li,select_one['span.value')
    print(exchange.string.split(' ')[-1], ':', value.string)