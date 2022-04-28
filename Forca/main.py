'''
Jogo Da Forca by Hanatiel Vargas
Jogo clássico da forca com letras e boneco sendo enforcado caso erre a letra e a palavra.
Criando o jogo para aprender tkinter, web scrape e data storage com xlsx e sql. 
'''

from doctest import master
from functions import func
from tkinter import *

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

temas = list(tema.keys())
temaatual = 'Roxo'


#Preenche a lista que, inicialmente vazia, vai disponibilizar as palavras para o jogo
lista = func.preencherlista()
palavra = 'meio' 
palavra_adv = ('_ ' * len(palavra))[:-1]
letras = list()


class View(Frame):
    def __init__(self, root):
        super().__init__(root)

        # Parte de baixo da interface do jogo 
        self.baixo = Frame(root)
        self.baixo.pack(side='bottom')
        self.baixo.configure(background=tema[temaatual]['Fundo'])

        # Botão de sair
        self.sair_rect = Canvas(self.baixo, bg=tema[temaatual]['Fundo'], width=300, height=55, relief='flat', bd=-1, border=-2)
        self.sair_rect.pack(side='left')
        self.sbtn = self.sair_rect.create_rectangle(300, 55, 0, 0, fill=tema[temaatual]['Fundo'], outline=tema[temaatual]['Fundo'])
        self.sbtn_txt = self.sair_rect.create_text(150, 25, text='Sair', fill=tema[temaatual]['Letra'], font='Times 17 bold', activefill=tema[temaatual]['Fback'])
        self.sair_rect.tag_bind(self.sbtn_txt, '<Button-1>', quit) # adicionar função

        # Botão de novo jogo
        self.novojogo_rect = Canvas(self.baixo, bg=tema[temaatual]['Fundo'], width=300, height=55, relief='flat', bd=-1, border=-2)
        self.novojogo_rect.pack(side='left')
        self.njbtn = self.novojogo_rect.create_rectangle(300, 55, 0, 0, fill=tema[temaatual]['Fundo'], outline=tema[temaatual]['Fundo'])
        self.njbtn_txt = self.novojogo_rect.create_text(150, 25, text='Novo Jogo', fill=tema[temaatual]['Letra'], font='Times 17 bold', activefill=tema[temaatual]['Fback'])
        self.novojogo_rect.tag_bind(self.njbtn_txt, '<Button-1>', func.novojogo)

        # Botão de Mudar tema
        self.mudartema_rect = Canvas(self.baixo, bg=tema[temaatual]['Fundo'], width=300, height=55, relief='flat', bd=-1, border=-2)
        self.mudartema_rect.pack(side='left')
        self.mtbtn = self.mudartema_rect.create_rectangle(300, 55, 0, 0, fill=tema[temaatual]['Fundo'], outline=tema[temaatual]['Fundo'])
        self.mtbtn_txt = self.mudartema_rect.create_text(150, 25, text='Mudar Tema', fill=tema[temaatual]['Letra'], font='Times 17 bold', activefill=tema[temaatual]['Fback'])
        self.mudartema_rect.tag_bind(self.mtbtn_txt, '<Button-1>', func.trocartema(temaatual, temas))


        # Parte do meio da interface do jogo
        self.meio = Frame(root)
        self.meio.pack(side='bottom')
        self.meio.configure(background=tema[temaatual]['Fundo'])

        # Área de input
        self.input_area = Entry(self.meio, bg=tema[temaatual]['Fundo'], fg=tema[temaatual]['Letra'], font='Times 17 bold', justify='center', selectborderwidth=1, bd=1, exportselection=0)
        self.input_area.pack(pady=30)


        # Parte de cima da interface do jogo
        self.cima = Frame(root)
        self.cima.pack()
        self.cima.configure(background=tema[temaatual]['Fundo'])

        # Área das imagens da forca

        # Área da palavra e as letras acertadas
        self.palavra_lbl = Canvas(self.cima, bg=tema[temaatual]['Fundo'], height=600, width=300, relief='flat', bd=-1, border=-2)
        self.palavra_lbl.pack(side='left')
        self.pllbl = self.palavra_lbl.create_rectangle(300, 600, 0, 0, fill=tema[temaatual]['Fundo'], outline=tema[temaatual]['Fundo'])
        self.pllbl_txt = self.palavra_lbl.create_text(150, 300, text=palavra_adv, fill=tema[temaatual]['Letra'], font='Times 17 bold')

        # Área das letras erradas


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Forca')
        self.iconphoto(False, PhotoImage(file='Forca/images/favicon.png'))
        self.title('Forca')
        self.minsize(900, 500)
        self.geometry('900x500+225+150')
        self.configure(background=tema[temaatual]['Fundo'])

        view = View(self)
        view.pack()


if __name__ == '__main__':
    app = App()
    app.mainloop()
