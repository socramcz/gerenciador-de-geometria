from tkinter import *

janela_principal = Tk()
mensagem = Label(text='Hello, World!', foreground='white', background='black')
mensagem.pack()
mensagem2 = Label(text='Hello, World', fg='#000000',
                  bg='#34A2FE', width=100, height=30,)
mensagem2.pack()

mainloop()
