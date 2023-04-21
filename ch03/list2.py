# 문자열 - 1차원 리스트
ss = "20230419Sunny"

year = ss[0:4]
print(year)

# day = 월일
day = ss[4:8]
print(day)

weather = ss[8:]
print(weather)

ss2 = year + day + weather
print(ss2)

# 문자열 관련 함수
# split(구분기호) -> 문자열이 리스트로 변환
fruit = "banana, apple, strawberry"
fruitlist = fruit.split(',')
print(fruitlist)
print(fruitlist[1]) # 1번 인덱스 -> apple

# replace('이전문자', '새문자')
str1 = 'Hello, World'
str1.replace('World', 'Korea')
print(str1)

# formal()
name = "Mario"
year = 40
str2 = "My name is {}.".format('Mario')
#str3 = "My name is %s." % 'Mario'
#name = "Mario"
#str4 = f"My name is {name}"
print(str2)
#print(str3)
#print(str4)

# split() 예제 - ':' 로 구분하고 리스트로 변경
string = "a:b:c:d"
string2 = string.split(':')
print(string2)
print(string2[-1])

# 두 수를 동시에 입력 받아서 더하기
"""
n1, n2 = input("두 수 입력 : ").split() #공백으로 구분

add = int(n1) + int(n2)
print(add)
"""
# find() - 문자열이 존재하는 위치 바나환
text = "Hello"
print(text.find('H'))
print(text.find('ll'))
print(text.find('k'))

print(text.find('Hello'))





