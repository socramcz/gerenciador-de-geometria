from tkinter import *

janela = Tk()
janela.columnconfigure(0, minsize=250)
janela.rowconfigure([0, 1], minsize=100)

label1 = Label(text="A")
label1.grid(row=0, column=0)

label2 = Label(text="B")
label2.grid(row=1, column=0)

mainloop()
