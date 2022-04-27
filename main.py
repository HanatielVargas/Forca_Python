'''
Jogo Da Forca by Hanatiel Vargas
Jogo clássico da forca com letras e boneco sendo enforcado caso erre a letra e a palavra.
Criando o jogo para aprender tkinter, web scrape e data storage com xlsx e sql. 
'''

#Importa funções que eu criei em outro arquivo python
from functions import func 
from tkinter import *
from tkinter import ttk
from tkinter import font

#Preenche a lista que, inicialmente vazia, vai disponibilizar as palavras para o jogo (por enquanto)
lista = func.preencherlista() 

# Dicionário com os temas do app
tema = {'Branco':{'Letra': '#000000', 
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

# Cria e configura a tela principal
root = Tk()
root.geometry('900x500+225+150')
root.configure(background=tema[temaatual]['Fundo'])

# passa o jogo para uma classe
myapp = App(root)
myapp.master.iconphoto(False, PhotoImage(file='imgs/favicon.png'))
myapp.master.title('Forca')
myapp.master.minsize(900, 500)

# Configura alguns esilos para o jogo
style = ttk.Style(root)
style.configure('TFrame', background=tema[temaatual]['Fundo'])
style.configure('BW.TFrame', background=tema[temaatual]['Fback'])

# Parte de baixo da interface do jogo 
baixo = Frame(root)
baixo.pack(side='bottom')


# Botão de novo jogo
novojogo_button = Canvas(baixo, bg=tema[temaatual]['Fundo'], width=150, height=50, relief='flat', bd=-1)
novojogo_button.pack()
btn = novojogo_button.create_rectangle(150, 50, 0, 0, fill=tema[temaatual]['Fundo'], outline='#00FF00')
btn_txt = novojogo_button.create_text(75, 25, text='Novo Jogo', fill=tema[temaatual]['Letra'], font='Times 17 bold')
novojogo_button.tag_bind(btn, '<Button-1>', func.novojogo)
novojogo_button.tag_bind(btn_txt, '<Button-1>', func.novojogo)

if __name__ == '__main__':
    myapp.mainloop()
