from tkinter import *

janela = Tk()

frame = Frame(master=janela, width=150, height=150)
frame.pack()

label1 = Label(master=frame, text="i'm at (0,0)", bg="light blue")
label1.place(x=0, y=0)

label2 = Label(master=frame, text="i'm at (75,75)", bg="light green")
label2.place(x=75, y=75)

mainloop()
