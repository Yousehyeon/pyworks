#vaccine.py 
byear=input("출생년도 입력 : ")

age = 2023 - int(byear) + 1

if age >= 20 and age <= 65:
    print("백신 접종 대상")
    # 접종대상 - 출생년도 끝자리 비교
    # if ~ elif ~ else
    if byear[-1] == "1" or byear[-1] == "6":
        print("월요일 접종")
    elif byear[-1] == "2" or byear[-1] == "7":
        print("화요일 접종")
    elif byear[-1] == "3" or byear[-1] == "8":
        print("수요일 접종")
    elif byear[-1] == "4" or byear[-1] == "9":
        print("목요일 접종")
    elif byear[-1] == "5" or byear[-1] == "0":
        print("금요일 접종")
else:
    print("하반기 일정 확인")
