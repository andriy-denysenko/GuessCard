#!/usr/bin/env python3
import os

import tkinter
from tkinter import ttk

from deck import *

if __name__ == '__main__':

    script_dir = os.path.dirname(os.path.abspath(__file__))

    d = Deck()
     
    root = tkinter.Tk(className='Guess Card Window')
    root.configure(bg='#ffffff')
     
    # Create a space for an image
    # frame = tkinter.Frame(root, bg = '#ffffff')
    # frame.grid()
     
    # Add an image of card back
    canvas = tkinter.Canvas(root, height=300, width=200, bg = '#ffffff')
    img = tkinter.PhotoImage(file = os.path.join(script_dir, 'img', 'back.png'))
    image = canvas.create_image(0, 0, anchor='nw',image=img)
    canvas.grid(row=0, column=0, columnspan=7)

    btn_suit_prev = tkinter.Button(root, text = '<')
    btn_suit = tkinter.Button(root, text = '-')
    btn_suit_next = tkinter.Button(root, text = '>')

    btn_suit_prev.grid(row=1, column=0)
    btn_suit.grid(row=1, column=1)
    btn_suit_next.grid(row=1, column=2)

    btn_rank_prev = tkinter.Button(root, text = '<')
    btn_rank = tkinter.Button(root, text = '-')
    btn_rank_next = tkinter.Button(root, text = '>')

    btn_rank_prev.grid(row=1, column=4)
    btn_rank.grid(row=1, column=5)
    btn_rank_next.grid(row=1, column=6)

    # TODO: we can shuffle the deck or pop a card AFTER a user pressed Go
    d.shuffle()


    root.mainloop()