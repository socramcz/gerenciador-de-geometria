from tkinter import *
from turtle import left, right

janela = Tk()

frame1 = Frame(master=janela, width=100, height=100, bg='red')
frame1.pack(fill=BOTH, side=LEFT, expand=True)

frame2 = Frame(master=janela, width=50, height=50, bg='black')
frame2.pack(fill=BOTH, side=LEFT, expand=True)

frame3 = Frame(master=janela, width=25, height=25, bg='red')
frame3.pack(fill=BOTH, side=LEFT, expand=True)

mainloop()
