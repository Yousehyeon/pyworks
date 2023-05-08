# 계산기 - 간단한 숫자 표시

from tkinter import *

def click(key):
    if key == '=':
        try:
            # eval(문자열 계산) ->숫자로 표현
            value = eval(display.get()) # 입력된 계산값
            result = str(value)[0:10]
            display.insert(END, '=' + result)
        except:
            display.insert(END, "-->오류")
    elif key == 'C':
        display.delete(0, END)
    else:
        display.insert(END, key)

root = Tk()
root.title("나의 계산기")

# top_row 프레임 - 입력창
top_row = Frame(root)
top_row.grid(row=0, column=0, sticky=N) #N-North(북쪽)
display = Entry(top_row, width=50, bg='light green')
display.grid(row=0, column=0)

# num_pad 프레임 - 숫자 버튼 프레임
num_pad = Frame(root)
num_pad.grid(row=1, column=0, sticky=W)
num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
]
r = 0
c = 0
for btn_text in num_pad_list:
    def cmd(x=btn_text):  # 함수에 인수(연산자 키)를 전달
        click(x)

    Button(num_pad, text=btn_text).grid(row=r, column=c)
    c = c + 1
    if c > 2:
        c = 0
        r = r + 1


# 연산자 프레임
operator = Frame (root)
operator.grid(row=1, column=1)
operator_list = [
    '*', '/',
    '*', '-',
    '(', ')',
    'C']
r = 0
c = 0
for btn_text in operator_list:
    Button(operator, text=btn_text, width=5).grid(row=r, column=c)
    c = c + 1
    if c > 1:
        c = 0
        r = r + 1


root.mainloop()