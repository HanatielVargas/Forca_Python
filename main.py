'''
Jogo Da Forca by Hanatiel Vargas
Jogo clássico da forca com letras e boneco sendo enforcado caso erre a letra e a palavra.
Criando o jogo para aprender tkinter, web scrape e data storage com xlsx e sql. 
'''

from functions import func #Importa funções que eu criei em outro arquivo python
from tkinter import *
from tkinter import ttk
from tkinter import font

lista = func.preencherlista() #Preenche a lista que, inicialmente vazia, vai disponibilizar as palavras para o jogo (por enquanto)

tema = {'Branco':{'Letra': '#000000', # Dicionário com os temas do app
                  'Fundo': '#FFFFFF',
                  'Fback': '#777777'}, 
        'Preto': {'Letra': '#FFFFFF', 
                  'Fundo': '#000000',
                  'Fback': '#777777'}, 
        'Roxo':  {'Letra': '#000000', 
                  'Fundo': '#E396FF',
                  'Fback': '#777777'},
        'Rosa':  {'Letra': '#361133',
                  'Fundo': '#FF7975',
                  'Fback': '#777777'}} 

temas = ['Branco', 'Preto', 'Roxo', 'teste']
temaatual = 'Roxo'

class App(Frame):
        def __init__(self, master=None):
                super().__init__(master)
                self.pack()

root = Tk()
root.geometry('900x500+225+150')
root.configure(background=tema[temaatual]['Fundo'])

style = ttk.Style(root)
style.configure('TFrame', background=tema[temaatual]['Fundo'])
style.configure('BW.TFrame', background=tema[temaatual]['Fback'])

ent1 = font.Font(family='Times', size=12)
btn1 = font.Font(family='Times', size=16)

root.overrideredirect(True)

titlebar = ttk.Frame(root, style='BW.TFrame', relief='raised', border=0)
titlebar.pack(fill=X)
titlelabel = Label(titlebar, text='Forca', font=ent1, background=tema[temaatual]['Fback'], foreground=tema[temaatual]['Letra'])
titlelabel.pack(side='left', pady=2, padx=2)

pck = ttk.Frame(root)
pck.pack(side='bottom')

bttn1 = Button(pck, text='Sair', font=btn1, activebackground=tema[temaatual]['Fundo'], activeforeground=tema[temaatual]['Letra'], bg=tema[temaatual]['Fundo'], fg=tema[temaatual]['Letra'], command=root.destroy, relief='flat').pack(side='bottom', pady=10)

entr1 = Entry(pck, font=ent1, exportselection=0, relief='solid', bg=tema[temaatual]['Fundo'], fg=tema[temaatual]['Letra']).pack(side='top')

myapp = App(root)
myapp.master.minsize(900, 500)

if __name__ == '__main__':
        myapp.mainloop()
