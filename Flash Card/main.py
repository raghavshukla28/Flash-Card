from tkinter import *
import pandas
import random
import textwrap

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
score = 0
answer_revealed = False


try:
    data = pandas.read_csv("data/unknown_questions.csv")
except FileNotFoundError as Stupid:
    original_data = pandas.read_csv("data/french_words.csv")
    quiz = original_data.to_dict(orient = "records")
else:
    quiz = data.to_dict(orient="records")


def wrap_text(text, width):
    return '\n'.join(textwrap.wrap(text, width))

def next_card():
    global current_card, flip_timer, answer_revealed
    answer_revealed = False
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_bg, image=card_front_img)
    current_card = random.choice(quiz)
    wrapped_question = wrap_text(current_card["Question"], 50)  # Adjust the width as needed
    canvas.itemconfig(card_title, text="Question", fill="black")
    canvas.itemconfig(card_word, text=wrapped_question, fill="black")
    flip_timer = window.after(4000, func=flip_card)

def flip_card():
    global answer_revealed
    wrapped_answer = wrap_text(current_card["Answer"], 50)  # Adjust the width as needed
    canvas.itemconfig(card_bg, image=card_back_img)
    canvas.itemconfig(card_title, text="Answer", fill="white")
    canvas.itemconfig(card_word, text=wrapped_answer, fill="white")
    answer_revealed = True

def known_answer():
    global score
    if answer_revealed:
        score += 1
        score_label.config(text=f"Score: {score}")
        next_card()
        is_known()


def unknown_answer():
    global score
    if answer_revealed:
        score -= 1
        score_label.config(text=f"Score: {score}")
        next_card()

def is_known():
    quiz.remove(current_card)
    data = pandas.DataFrame(quiz)
    data.to_csv("data/unknown_questions.csv",index = False)

window = Tk()
window.title("UPSC Quiz")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(10000, func=flip_card)

canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Question", font=("Ariel", 20, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=unknown_answer)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=known_answer)
known_button.grid(row=1, column=1)

score_label = Label(window, text="Score: 0", bg=BACKGROUND_COLOR, font=("Ariel", 24))
score_label.grid(row=2, column=0, columnspan=2)

next_card()

window.mainloop()
