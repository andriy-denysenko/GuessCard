#!/usr/bin/env python3
import os

import tkinter
from tkinter import ttk

from deck import *

if __name__ == '__main__':

    script_dir = os.path.dirname(os.path.abspath(__file__))

    d = Deck()
     
    root = tkinter.Tk()
     
    # создаем рабочую область
    frame = tkinter.Frame(root, bg = '#ffffff')
    frame.grid()
     
    #Добавим изображение
    canvas = tkinter.Canvas(root, height=300, width=200, bg = '#ffffff')
    # img = tkinter.PhotoImage(file = f'./img/{d.pick()}.png') 
    img = tkinter.PhotoImage(file = os.path.join(script_dir, 'img', 'back.png'))
    image = canvas.create_image(0, 0, anchor='nw',image=img)
    canvas.grid(row=0,column=0, columnspan=2)

    d.shuffle()

    cbo_ranks = ttk.Combobox(root, height = 13)
    rank_list = []
    for r in RANKS:
        rank_list.append(r)
    cbo_ranks['values'] = rank_list

    cbo_ranks.grid(row = 1, column = 0)

    # btn_reset = tkinter.Button(root, text = 'Reset')
    # btn_reset.grid(row=1, column=0)

    # btn_try = tkinter.Button(root, text = 'Try')
    # btn_try.grid(row=1, column=1)



    root.mainloop()