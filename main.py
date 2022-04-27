'''
Jogo Da Forca by Hanatiel Vargas
Jogo clássico da forca com letras e boneco sendo enforcado caso erre a letra e a palavra.
Criando o jogo para aprender tkinter, web scrape e data storage com xlsx e sql. 
'''

#Importa funções que eu criei em outro arquivo python
from functions import func 
from tkinter import *
from tkinter import ttk
import pandas as pd


def limparlista():
    lista = []
    palavras = pd.Series(lista, name='Palavras')
    palavras.to_excel('palavras.xlsx')


def novojogo(*args):
    pass


def preencherlista():
    lista = list()
    palavras = pd.read_excel('palavras.xlsx')
    for c in palavras['Palavras']:
        lista.append(str(c))
    return lista


def adicionarpalavra(lista, word):
    from urllib3 import PoolManager, exceptions

    try:
        site = PoolManager().request('GET', f'https://www.dicio.com.br/{word.lower()}/')
        if 'Ops' in str(site.data):
            raise exceptions.SSLError
    except exceptions.SSLError:
        pass
    else:
        lista.append(word.capitalize())
        palavras = pd.Series(lista, name='Palavras')
        palavras.to_excel('.palavras.xlsx')


def trocartema(temas, escolhido, atual):
    if temas[escolhido] in temas:
        return temas[escolhido]
    else:
        for c in temas:
            if c == atual:
                continue
            return temas 


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

# Botão de 
algo_rect = Canvas(baixo, bg=tema[temaatual]['Fundo'], width=300, height=55, relief='flat', bd=-1, border=-2)
algo_rect.pack(side='left')
btn = algo_rect.create_rectangle(300, 50, 0, 0, fill=tema[temaatual]['Fundo'], outline=tema[temaatual]['Fundo'])
btn_txt = algo_rect.create_text(150, 25, text='Alguma Coisa', fill=tema[temaatual]['Letra'], font='Times 17 bold', activefill=tema[temaatual]['Fback'])
algo_rect.tag_bind(btn_txt, '<Button-1>') # adicionar função

# Botão de novo jogo
novojogo_rect = Canvas(baixo, bg=tema[temaatual]['Fundo'], width=300, height=55, relief='flat', bd=-1, border=-2)
novojogo_rect.pack(side='left')
njbtn = novojogo_rect.create_rectangle(300, 50, 0, 0, fill=tema[temaatual]['Fundo'], outline=tema[temaatual]['Fundo'])
njbtn_txt = novojogo_rect.create_text(150, 25, text='Novo Jogo', fill=tema[temaatual]['Letra'], font='Times 17 bold', activefill=tema[temaatual]['Fback'])
novojogo_rect.tag_bind(njbtn_txt, '<Button-1>', func.novojogo)

# Botão de Mudar tema
mudartema_rect = Canvas(baixo, bg=tema[temaatual]['Fundo'], width=300, height=55, relief='flat', bd=-1, border=-2)
mudartema_rect.pack(side='left')
mtbtn = mudartema_rect.create_rectangle(300, 50, 0, 0, fill=tema[temaatual]['Fundo'], outline=tema[temaatual]['Fundo'])
mtbtn_txt = mudartema_rect.create_text(150, 25, text='Mudar Tema', fill=tema[temaatual]['Letra'], font='Times 17 bold', activefill=tema[temaatual]['Fback'])
mudartema_rect.tag_bind(mtbtn_txt, '<Button-1>', func.trocartema)


meio = Frame(root)
meio.pack(side='bottom')

lbl = ttk.Label(meio, text='A')
lbl.pack(side='bottom')

if __name__ == '__main__':
    myapp.mainloop()
