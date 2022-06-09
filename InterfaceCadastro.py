import tkinter
from tkinter import *


def format_cpf(event=None):
    text = e3.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace":
        return

    for i in range(len(text)):

        if not text[i] in "0123456789":
            continue
        if i in [2, 5]:
            new_text += text[i] + "."
        elif i == 8:
            new_text += text[i] + "-"
        else:
            new_text += text[i]

    e3.delete(0, "end")
    e3.insert(0, new_text)


def format_data(event=None):
    text = e2.get().replace("/", "")[:8]
    new_text = ""

    if event.keysym.lower() == "backspace":
        return

    for i in range(len(text)):

        if not text[i] in "0123456789":
            continue
        if i in [1, 3]:
            new_text += text[i] + "/"
        else:
            new_text += text[i]

    e2.delete(0, "end")
    e2.insert(0, new_text)


def format_tel(event=None):
    text = e4.get().replace("(", "").replace(")", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace":
        return

    for i in range(len(text)):

        if not text[i] in "0123456789":
            continue
        if i in [0]:
            new_text += "(" + text[i]
        elif i in [1]:
            new_text += text[i] + ")"
        elif i in [6]:
            new_text += text[i] + "-"
        else:
            new_text += text[i]

    e4.delete(0, "end")
    e4.insert(0, new_text)


cad = Tk()
cad.geometry('700x300+600+300')
cad.title('Cadastro')
radioVale = tkinter.IntVar()

f1 = Frame(cad)
f2 = Frame(cad, pady=20)
f3 = Frame(cad)

t1 = Label(f1, text='Dados Pessoais', anchor=E, pady=5, padx=0)
t2 = Label(f1, text='Nome:', anchor=E, pady=5, padx=0, width=12)
t3 = Label(f1, text='Data Nasc:', anchor=E, pady=5, padx=0, width=10)
t4 = Label(f1, text='CPF:', anchor=E, pady=7, padx=0, width=12)
t5 = Label(f1, text='Telefone:', anchor=E, pady=7, padx=0)
t12 = Label(f1, text='Sexo:', anchor=E, pady=7, padx=0, width=12)
es = Radiobutton(f1, text='Feminino', variable=radioVale, value=1, anchor=W, pady=7, padx=0)
es1 = Radiobutton(f1, text='Masculino', variable=radioVale, value=2)
e1 = Entry(f1)
e2 = Entry(f1)
e2.bind("<KeyRelease>", format_data)
e3 = Entry(f1)
e3.bind("<KeyRelease>", format_cpf)
e4 = Entry(f1)
e4.bind("<KeyRelease>", format_tel)

t6 = Label(f2, text='Endereço', anchor=E, padx=0, pady=5)
t7 = Label(f2, text='Rua:', anchor=E, padx=0, pady=5, width=7)
t8 = Label(f2, text='Nº:', anchor=E, padx=0, pady=5, width=4)
t9 = Label(f2, text='Bairro:', anchor=E, padx=0, pady=7, width=7)
t10 = Label(f2, text='Cidade:', anchor=E, padx=0, pady=7, width=7)
t11 = Label(f2, text='UF:', anchor=E, padx=0, pady=7, width=4)
e5 = Entry(f2)
e6 = Entry(f2, width=8)
e7 = Entry(f2)
e8 = Entry(f2)
e9 = Entry(f2, width=8)

b1 = Button(f3, text='Gravar Dados', anchor=E)
b2 = Button(f3, text='Listar Dados', anchor=E)

f1.grid(sticky=NSEW)
f2.grid(sticky=NSEW)
f3.grid(sticky=NSEW)

t1.grid(row=0, column=0)
t2.grid(row=1, column=0)
e1.grid(row=1, column=1, columnspan=6, sticky=EW)
t3.grid(row=1, column=10)
e2.grid(row=1, column=11)
t4.grid(row=4, column=0)
e3.grid(row=4, column=1)
t5.grid(row=4, column=5)
e4.grid(row=4, column=6)
t12.grid(row=7, column=0)
es.grid(row=7, column=1)
es1.grid(row=7, column=2)
t6.grid(row=0, column=0)
t7.grid(row=1, column=0)
e5.grid(row=1, column=1, columnspan=8, sticky=EW)
t8.grid(row=1, column=10)
e6.grid(row=1, column=11)
t9.grid(row=2, column=0)
e7.grid(row=2, column=1)
t10.grid(row=2, column=5)
e8.grid(row=2, column=6)
t11.grid(row=2, column=10)
e9.grid(row=2, column=11)
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
cad.mainloop()
