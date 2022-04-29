'''
Jogo Da Forca by Hanatiel Vargas
Jogo clássico da forca com letras e boneco sendo enforcado caso erre a letra e a palavra.
Criando o jogo para aprender tkinter, web scrape e data storage com xlsx e sql. 
'''

import pandas as pd
from tkinter import *


class Model:
    def __init__(self):

        #Preenche a lista que, inicialmente vazia, vai disponibilizar as palavras para o jogo
        self.lista = self.preencherlista()
        self.palavra = 'meio' 
        self.palavra_adv = ('_ ' * len(self.palavra))[:-1]
        self.letras = list()

        # Dicionário com os temas do app
        self.tema = {'Branco':{'Letra': '#000000', 
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

        self.temas = list(self.tema.keys())
        self.temaatual = self.temas[0]


    def preencherlista(*args):
        lista = list()
        palavras = pd.read_excel('Forca/database/palavras.xlsx')
        for c in palavras['Palavras']:
            lista.append(str(c))
        return lista

    
    def atualiza(letra):
        pass
    
    
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
            palavras.to_excel('Forca/database/palavras.xlsx')


class View(Frame):
    def __init__(self, root):
        super().__init__(root)

        self.model = Model()

        # Parte de baixo da interface do jogo 
        self.baixo = Frame(root)
        self.baixo.pack(side='bottom')
        self.baixo.configure(background=self.model.tema[self.model.temaatual]['Fundo'])

        # Botão de sair
        self.sair_rect = Canvas(self.baixo, bg=self.model.tema[self.model.temaatual]['Fundo'], width=300, height=55, relief='flat', bd=-1, border=-2)
        self.sair_rect.pack(side='left')
        self.sbtn = self.sair_rect.create_rectangle(300, 55, 0, 0, fill=self.model.tema[self.model.temaatual]['Fundo'], outline=self.model.tema[self.model.temaatual]['Fundo'])
        self.sbtn_txt = self.sair_rect.create_text(150, 25, text='Sair', fill=self.model.tema[self.model.temaatual]['Letra'], font='Times 17 bold', activefill=self.model.tema[self.model.temaatual]['Fback'])
        self.sair_rect.tag_bind(self.sbtn_txt, '<Button-1>', quit) # adicionar função

        # Botão de novo jogo
        self.novojogo_rect = Canvas(self.baixo, bg=self.model.tema[self.model.temaatual]['Fundo'], width=300, height=55, relief='flat', bd=-1, border=-2)
        self.novojogo_rect.pack(side='left')
        self.njbtn = self.novojogo_rect.create_rectangle(300, 55, 0, 0, fill=self.model.tema[self.model.temaatual]['Fundo'], outline=self.model.tema[self.model.temaatual]['Fundo'])
        self.njbtn_txt = self.novojogo_rect.create_text(150, 25, text='Novo Jogo', fill=self.model.tema[self.model.temaatual]['Letra'], font='Times 17 bold', activefill=self.model.tema[self.model.temaatual]['Fback'])
        self.novojogo_rect.tag_bind(self.njbtn_txt, '<Button-1>', Controller.novojogo)

        # Botão de Mudar tema
        self.mudartema_rect = Canvas(self.baixo, bg=self.model.tema[self.model.temaatual]['Fundo'], width=300, height=55, relief='flat', bd=-1, border=-2)
        self.mudartema_rect.pack(side='left')
        self.mtbtn = self.mudartema_rect.create_rectangle(300, 55, 0, 0, fill=self.model.tema[self.model.temaatual]['Fundo'], outline=self.model.tema[self.model.temaatual]['Fundo'])
        self.mtbtn_txt = self.mudartema_rect.create_text(150, 25, text='Mudar Tema', fill=self.model.tema[self.model.temaatual]['Letra'], font='Times 17 bold', activefill=self.model.tema[self.model.temaatual]['Fback'])
        self.mudartema_rect.tag_bind(self.mtbtn_txt, '<Button-1>', Controller.trocartema(self.model.temaatual, self.model.temas))


        # Parte do meio da interface do jogo
        self.meio = Frame(root)
        self.meio.pack(side='bottom')
        self.meio.configure(background=self.model.tema[self.model.temaatual]['Fundo'])

        # Área de input
        self.input_area = Entry(self.meio, bg=self.model.tema[self.model.temaatual]['Fundo'], fg=self.model.tema[self.model.temaatual]['Letra'], font='Times 17 bold', justify='center', selectborderwidth=1, bd=1, exportselection=0)
        self.input_area.pack(pady=30)


        # Parte de cima da interface do jogo
        self.cima = Frame(root)
        self.cima.pack()
        self.cima.configure(background=self.model.tema[self.model.temaatual]['Fundo'])

        self.imagens()
        self.palavra()
        self.letrase()


    def imagens(self):
        # Área das imagens da forca
        # Não feito
        pass


    def palavra(self):
        # Área da palavra e as letras acertadas
        self.palavra_lbl = Canvas(self.cima, bg=self.model.tema[self.model.temaatual]['Fundo'], height=600, width=300, relief='flat', bd=-1, border=-2)
        self.palavra_lbl.pack(side='left')
        self.pllbl = self.palavra_lbl.create_rectangle(300, 600, 0, 0, fill=self.model.tema[self.model.temaatual]['Fundo'], outline=self.model.tema[self.model.temaatual]['Fundo'])
        self.pllbl_txt = self.palavra_lbl.create_text(150, 300, text=self.model.palavra_adv, fill=self.model.tema[self.model.temaatual]['Letra'], font='Times 17 bold')


    def letrase(self):
        # Área das letras erradas
        # Não feito
        pass


class Controller:
    def __init__(self):
        pass


    def trocartema(temaatual, temas):
        for i, c in enumerate(temas):
            if temas[i-1] == temaatual:
                temaatual = c
                break

    
    def novojogo(*args):
        pass


class App(Tk):
    def __init__(self):
        super().__init__()

        model = Model()

        view = View(self)
        view.pack()

        self.title('Forca')
        self.iconphoto(False, PhotoImage(file='Forca/images/favicon.png'))
        self.title('Forca')
        self.minsize(900, 500)
        self.geometry('900x500+225+150')
        self.configure(background=model.tema[model.temaatual]['Fundo'])


if __name__ == '__main__':
    app = App()
    app.mainloop()
