# 단위 변환기 - 테스트용
from tkinter import *

class App:
    def __init__ (self):
        frame = Frame(root)
        frame.pack()

        Label(frame, text="deg C").grid(row=0, column=0)
        Button(frame, text="변환", command=self.convert).grid(row=1, column=0)



root = Tk()
root.title("온도 변환기")
app = App(root)

root.mainloop()



root.mainloop()
