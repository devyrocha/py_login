from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from dados import *

# cores ------------------------------------
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha


janela = Tk()
janela.title('Pokedex')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

# criando frame

frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)


def trocar_pokemon(i):
    global imagem_pokemon, poke_id

    frame_pokemon['bg'] = pokemon[i]['tipo'][3] 

    # tipo de pokemon
    poke_name['text'] = i
    poke_name['bg'] = pokemon[i]['tipo'][3]
    poke_tipo['text'] = pokemon[i]['tipo'][1]
    poke_tipo['bg'] = pokemon[i]['tipo'][3]
    # poke_id['text'] = pokemon[i]['tipo'][0]
    # poke_id['bg']=pokemon[i]['tipo'][3]

    imagem_pokemon = pokemon[i]["tipo"][2]

    # Imagem do Pokemon
    imagem_pokemon = Image.open(imagem_pokemon)
    imagem_pokemon = imagem_pokemon.resize((238, 238))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

    poke_imagem = Label(frame_pokemon, image=imagem_pokemon,
        relief='flat', bg=pokemon[i]['tipo'][3], fg=co1)
    poke_imagem.place(x=60, y=50)

    poke_tipo.lift()


# nome
poke_name = Label(frame_pokemon, text='', relief='flat',
                  anchor=CENTER, font=('Fixedsys 20'),fg=co1)
poke_name.place(x=12, y=15)

poke_tipo = Label(frame_pokemon, text='', relief='flat',
                  anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
poke_tipo.place(x=12, y=50)

poke_id = Label(frame_pokemon, text='', relief='flat',
                anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
poke_id.place(x=12, y=75)


# Status
poke_style = Label(janela,  text='Status', relief='flat',
                   anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
poke_style.place(x=12, y=310)
# hp
poke_hp = Label(janela, text='HP 100', relief='flat',
                anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_hp.place(x=12, y=360)
# ataque
poke_atack = Label(janela, text='Ataque 600', relief='flat',
                   anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_atack.place(x=12, y=360)
# defesa
poke_defense = Label(janela, text='Defesa 100', relief='flat',
                     anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_defense.place(x=12, y=385)
# velocidade
poke_velocidade = Label(janela, text='Velocidade 100', relief='flat',
                        anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_velocidade.place(x=12, y=410)
# total
poke_total = Label(janela, text='Total 100', relief='flat',
                   anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_total.place(x=12, y=435)

# Habilidades
poke_habilidade = Label(janela, text='Habilidades', relief='flat',
                        anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co4)
poke_habilidade.place(x=180, y=310)

# Habilidade1
poke_habilidade_1 = Label(janela, text='Soco Elétrico', relief='flat',
                          anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_habilidade_1.place(x=195, y=360)

# Habilidade2
poke_habilidade_2 = Label(janela, text='Chute Elétrico', relief='flat',
                          anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poke_habilidade_2.place(x=195, y=385)

# Criando botoes para pokemon
imagem_pokemon_1 = Image.open('images/cabeca-pikachu.png')
imagem_pokemon_1 = imagem_pokemon_1.resize((40, 40))
imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)

# Criando botoes para pokemon
imagem_pokemon_1 = Image.open('images/cabeca-pikachu.png')
imagem_pokemon_1 = imagem_pokemon_1.resize((40, 40))
imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)

b_poke_1 = Button(janela, command=lambda: trocar_pokemon('Pikachu'), image=imagem_pokemon_1, compound=LEFT, padx=5,
                  text='Pikachu', width=150, relief='raised', font=('Verdana 12'), overrelief=RIDGE, anchor=NW, bg=co1, fg=co0)
b_poke_1.place(x=375, y=10)

# Criando botoes para pokemon
imagem_pokemon_2 = Image.open('images/cabeca-bulbasaur.png')
imagem_pokemon_2 = imagem_pokemon_2.resize((40, 40))
imagem_pokemon_2 = ImageTk.PhotoImage(imagem_pokemon_2)

b_poke_2 = Button(janela, command=lambda: trocar_pokemon('Bulbasaur'), image=imagem_pokemon_2, compound=LEFT, padx=5,
                  text='Bulbasaur', width=150, relief='raised', font=('Verdana 12'), overrelief=RIDGE, anchor=NW, bg=co1, fg=co0)
b_poke_2.place(x=375, y=60)

# Criando botoes para pokemon
imagem_pokemon_3 = Image.open('images/cabeca-charmander.png')
imagem_pokemon_3 = imagem_pokemon_3.resize((40, 40))
imagem_pokemon_3 = ImageTk.PhotoImage(imagem_pokemon_3)

b_poke_3 = Button(janela, command=lambda: trocar_pokemon('Charmander'), image=imagem_pokemon_3, compound=LEFT, padx=5,
                  text='Charmander', width=150, relief='raised', font=('Verdana 12'), overrelief=RIDGE, anchor=NW, bg=co1, fg=co0)
b_poke_3.place(x=375, y=110)


# Criando botoes para pokemon
imagem_pokemon_4 = Image.open('images/cabeca-dragonite.png')
imagem_pokemon_4 = imagem_pokemon_4.resize((40, 40))
imagem_pokemon_4 = ImageTk.PhotoImage(imagem_pokemon_4)

b_poke_4 = Button(janela, command=lambda: trocar_pokemon('Dragonite'), image=imagem_pokemon_4, compound=LEFT, padx=5,
                  text='Dragonite', width=150, relief='raised', font=('Verdana 12'), overrelief=RIDGE, anchor=NW, bg=co1, fg=co0)
b_poke_4.place(x=375, y=160)

# Criando botoes para pokemon
imagem_pokemon_5 = Image.open('images/cabeca-gengar.png')
imagem_pokemon_5 = imagem_pokemon_5.resize((40, 40))
imagem_pokemon_5 = ImageTk.PhotoImage(imagem_pokemon_5)

b_poke_5 = Button(janela, command=lambda: trocar_pokemon('Gengar'), image=imagem_pokemon_5, compound=LEFT, padx=5,
                  text='Gengar', width=150, relief='raised', font=('Verdana 12'), overrelief=RIDGE, anchor=NW, bg=co1, fg=co0)
b_poke_5.place(x=375, y=210)


# Criando botoes para pokemon
imagem_pokemon_6 = Image.open('images/cabeca-gyarados.png')
imagem_pokemon_6 = imagem_pokemon_6.resize((40, 40))
imagem_pokemon_6 = ImageTk.PhotoImage(imagem_pokemon_6)

b_poke_6 = Button(janela, command=lambda: trocar_pokemon('Gyarados'), image=imagem_pokemon_6, compound=LEFT, padx=5,
                  text='Gyarados', width=150, relief='raised', font=('Verdana 12'), overrelief=RIDGE, anchor=NW, bg=co1, fg=co0)
b_poke_6.place(x=375, y=260)


janela.mainloop()
