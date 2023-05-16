"""
가위, 바위, 보 게임 만들기
- 게임 방법
1. 당신(you)은 가위, 바위, 보 중 하나를 입력한다.
2. 컴퓨터(com)는 가위, 바위, 보 중 하나를 랜덤 생성한다.
3. 결과 출력은 무승부, 패, 승이다.
4. 잘못 입력한 경우 "잘못된 입력입니다. 다시 입력해 주세요"
"""
import random

print("가위 바위 보")

try:
    you = input("당신 : ")

    choice = ['가위', '바위', '보']
    rnd = random.randint(0, 2)
    com = choice[rnd]
    print("컴퓨터 : ", com)

    if you == com:
        print("결과 : 무승부")
    elif you == "가위" and com == "보":
        print("결과 : 승")
    elif you == "바위" and com == "가위":
        print("결과 : 승")
    elif you == "보" and com == "바위":
        print("결과 : 패")
    elif you == "가위" and com == "바위":
        print("결과 : 패")
    elif you == "바위" and com == "보":
        print("결과 : 패")
    elif you == "보" and com == "가위":
        print("결과 : 패")

except:
    print("잘못된 입력입니다. 다시 입력해주세요.")


