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
        self.lista = list()
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
                               'Fback': '#777777'},
                     'padrao':{'Letra': '#000000',
                               'Fundo': '#F0F0F0',
                               'Fback': '#E396FF'}} 

        self.temas = list(self.tema.keys())
        self.temaatual = self.temas[-1]

        self.imagematual = 'Forca/images/forca_6vidas.png'
        self.status = ['', self.tema[self.temaatual]['Letra']]

        self.preencherlista()


    def preencherlista(self, *args):
        self.lista = list()
        self.palavras = pd.read_excel('Forca/database/palavras.xlsx')
        for c in self.palavras['Palavras']:
            self.lista.append(str(c))
    
    
    def trocartema(self, *args):
        self.temaatual = self.temas[(self.temas.index(self.temaatual))+1]
        print(self.temaatual)


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

        # Parte de baixo da interface do jogo 
        self.baixo = Frame(root)
        self.baixo.pack(side='bottom')
        self.baixo.configure(background=Controller().fundo)

        # Botão de sair
        self.sair_rect = Canvas(self.baixo, bg=Controller().fundo, width=300, height=55, relief='flat', bd=-1, border=-2)
        self.sair_rect.pack(side='left')
        self.sbtn = self.sair_rect.create_rectangle(300, 55, 0, 0, fill=Controller().fundo, outline=Controller().fundo)
        self.sbtn_txt = self.sair_rect.create_text(150, 25, text='Sair', fill=Controller().letra, font='Times 17 bold', activefill=Controller().actfl)
        self.sair_rect.tag_bind(self.sbtn_txt, '<Button-1>', Controller.sair) # adicionar função

        # Botão de novo jogo
        self.novojogo_rect = Canvas(self.baixo, bg=Controller().fundo, width=300, height=55, relief='flat', bd=-1, border=-2)
        self.novojogo_rect.pack(side='left')
        self.njbtn = self.novojogo_rect.create_rectangle(300, 55, 0, 0, fill=Controller().fundo, outline=Controller().fundo)
        self.njbtn_txt = self.novojogo_rect.create_text(150, 25, text='Novo Jogo', fill=Controller().letra, font='Times 17 bold', activefill=Controller().actfl)
        self.novojogo_rect.tag_bind(self.njbtn_txt, '<Button-1>', Controller.novojogo)

        # Botão de Mudar tema
        self.mudartema_rect = Canvas(self.baixo, bg=Controller().fundo, width=300, height=55, relief='flat', bd=-1, border=-2)
        self.mudartema_rect.pack(side='left')
        self.mtbtn = self.mudartema_rect.create_rectangle(300, 55, 0, 0, fill=Controller().fundo, outline=Controller().fundo)
        self.mtbtn_txt = self.mudartema_rect.create_text(150, 25, text='Mudar Tema', fill=Controller().letra, font='Times 17 bold', activefill=Controller().actfl)
        self.mudartema_rect.tag_bind(self.mtbtn_txt, '<Button-1>', Controller.trocartemac)


        # Parte do meio da interface do jogo
        self.meio = Frame(root)
        self.meio.pack(side='bottom')
        self.meio.configure(background=Controller().fundo)

        self.meioinp = Frame(self.meio)
        self.meioinp.pack(side='left')
        self.meioinp.configure(background=Controller().fundo)

        # Área de input
        self.input_area = Entry(self.meio, bg=Controller().fundo, fg=Controller().letra, font='Times 17 bold', justify='center', selectborderwidth=1, bd=1, exportselection=0)
        self.input_area.pack(pady=30, side='left')

        # Botão de verificar letra
        self.checkbutton = Canvas(self.meio, bg=Controller().fundo, width=70, height=50, relief='flat', bd=-1, border=-2)
        self.checkbutton.pack(side='left')
        self.chbtn = self.checkbutton.create_rectangle(50, 50, 0, 0, fill=Controller().fundo, outline=Controller().fundo)
        self.chtn_txt = self.checkbutton.create_text(35, 25, text='Add', fill=Controller().letra, font='Times 17 bold', activefill=Controller().actfl)
        self.checkbutton.tag_bind(self.chtn_txt, '<Button-1>', Controller.verifica)


        # Parte de cima da interface do jogo
        self.cima = Frame(root)
        self.cima.pack(side='bottom', pady=50)
        self.cima.configure(background=Controller().fundo)

        # Área das imagens da forca
        self.imagem = PhotoImage(file=Controller().imagem) 
        self.img = Label(self.cima, image=self.imagem, width=300)
        self.img.imagem = self.imagem
        self.img.pack(side='left')

        # Área do meio da parte de cima
        self.meiocima = Frame(self.cima)
        self.meiocima.pack(side='left')
        self.meiocima.configure(background=Controller().fundo)

        # Área da palavra e as letras acertadas
        self.palavra_lbl = Canvas(self.meiocima, bg=Controller().fundo, height=55, width=300, relief='flat', bd=-1, border=-2)
        self.palavra_lbl.pack(side='bottom')
        self.palavra_lbl.configure(background=Controller().fundo)
        self.pllbl = self.palavra_lbl.create_rectangle(300, 55, 0, 0, fill=Controller().fundo, outline=Controller().fundo)
        self.pllbl_txt = self.palavra_lbl.create_text(150, 25, text=Model().palavra_adv, fill=Controller().letra, font='Times 17 bold')

        # Área de mostrar se ganhou ou perdeu
        self.status = Canvas(self.meiocima, bg=Controller().fundo, height=55, width=300, relief='flat', bd=-1, border=-2)
        self.status.pack(side='bottom', pady=70)
        self.stts = self.status.create_rectangle(300, 55, 0, 0, fill=Controller().fundo, outline=Controller().fundo)
        self.stts_txt = self.status.create_text(150, 25, text=Controller().status[0], fill=Controller().status[1], font='Times 17 bold')

        # Área das letras erradas
        self.letrase = Label(self.cima, background=Controller().fundo, foreground=Controller().letra, text=Controller().letraserradas, justify='center', width=300, font='Times 12 bold')
        self.letrase.pack(side='left')

        self.controller = None

    
    def set_controller(self, controller):
        self.controller = controller


class Controller:
    def __init__(self):
        
        self.fundo = Model().tema[Model().temaatual]['Fundo']
        self.letra = Model().tema[Model().temaatual]['Letra']
        self.actfl = Model().tema[Model().temaatual]['Fback']

        self.imagem = str(Model().imagematual)
        self.status = Model().status
        self.letraserr = ''
        self.letrasace = ''
        self.letraserradas = self.letrase()


    def novojogo(self, *args):
        pass


    def trocartemac(self, *args):
        pass


    def sair(self, *args):
        exit()

    
    def letrase(self):
        string = ''
        for i, c in enumerate(self.letraserr):
            if (i)%5 == 0:
                string += '\n'

            string += f'{c.upper()}'

            if self.letraserr[-1] != self.letraserr[i]:
                string += ' '*4

        return string


    def verifica(self):
        pass


class App(Tk):
    def __init__(self):
        super().__init__()

        view = View(self)
        view.pack()
        self.configure(background=Controller().fundo)

        self.title('Forca')
        self.iconphoto(False, PhotoImage(file='Forca/images/favicon.png'))
        self.title('Forca')
        self.minsize(900, 500)
        self.maxsize(900, 500)
        self.geometry('900x500+225+150')

    
    def atualizar(self):
        pass


if __name__ == '__main__':
    app = App()
    app.mainloop()
