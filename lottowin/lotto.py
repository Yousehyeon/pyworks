import requests
from bs4 import BeautifulSoup
from tkinter import *

def lotto_win():
    # num = 1066
    num = entry.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(num)
    response = requests.get(url)
    # print(response)

    soup = BeautifulSoup(response.text, "html.parser")
    win_result = soup.select_one('div.win_result')
    # win_result.text
    win_list = win_result.text.split('\n')
    win_list
    win_list = win_result.text.split('\n')[7:13]
    win_list
    bonus_num = win_result.text.split('\n')[-4]
    bonus_num


# 출력상자에 번호 출력
    output.delete(0.0, END)
    output.insert(END, f'당첨번호: {win_list}\n\n보너스 : {bonus_num}')

"""
    print('당첨번호')
    print(win_list)
    print('보너스번호')
    print(bonus_num)
"""
# lotto_win()

window = Tk()
window.title("로또 당첨 확인")

Label(window, text="당첨 회자 입력: ").grid(row=0, column=0)
entry = Entry(window)
entry.grid(row=1, column=0, sticky=W)
btn = Button(window, text="당첨 번호 확인", command=lotto_win)
btn.grid(row=2, column=0, sticky=W)

output = Text(window, bg='skyblue', width=50, height=5)
output.grid(row=3, column=0, sticky=W)

window.mainloop()