import random
from tkinter import *
import pandas as pd

# creating pandas dataframe to dict
file_data = pd.read_csv('data/french_words.csv')
# new_data = file_data.to_dict() # in this you will get the data in wrong manner
new_data = file_data.to_dict(orient='records')
# print(new_data)

current_card = {}

# -----------------------------------------------------------
def next_card():
    # global current_card
    global current_card, flip_timer
    screen.after_cancel(flip_timer) # Switch off the fliper
    current_card = random.choice(new_data)
    canvas.itemconfig(title, text="French", fill='black')
    canvas.itemconfig(word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = screen.after(3000, func=flip_card) #Switch on the fliper again


def flip_card():
    canvas.itemconfig(title, text="English", fill='white')
    canvas.itemconfig(word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_bg, image=card_back_img)

# ----------------------------------------------------------

def known_word():
    new_data.remove(current_card)
    # print(len(new_data))
    learn_data = pd.DataFrame(new_data)
    learn_data.to_csv("data/words_to_learn.csv",  index=False)
    next_card()




# ----------------------Screen------------------------
BACKGROUND_COLOR = "#B1DDC6"

screen = Tk()
screen.title("Flash capstone")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# screen.after(3000, func=flip_card)
flip_timer = screen.after(3000, func=flip_card)


# ----------------------Canvas creation------------------
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400,263, image=card_front_img)



# -----------------------Text on canvas------------------
title = canvas.create_text(400, 150, text="", font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text="", font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
# canvas.grid(row=0, column=0)
canvas.grid(row=0, column=0, columnspan=2) # to adjust the misalignment of buttons



# ------------------------Buttons------------------------------
wrong_img = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_img, borderwidth=0,highlightthickness=0, command=next_card)
wrong.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right = Button(image=right_img, borderwidth=0,highlightthickness=0, command=known_word)
right.grid(row=1, column=1)

next_card()

screen.mainloop()
