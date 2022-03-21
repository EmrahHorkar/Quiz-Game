from tkinter import *
import pandas
import turtle
from PIL import ImageTk, Image


FONT_NAME = "Courier"
BLUE = "#313552"
RED = "#B8405E"
YELLOW = "#2EB086"
LIGHT = "#EEE6CE"




def state_game():
    landing_window.destroy()
    screen = turtle.Screen()
    screen.title("U.S States Game")
    image = "blank_states_img.gif"

    screen.addshape(image)

    turtle.shape(image)
    guessed_states = []

    data = pandas.read_csv("./us-states-game-start/50_states.csv")
    all_states = data.state.to_list()

    while (len(guessed_states) < 50):
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                        prompt="What's another states name").title()
        if answer_state == "Exit":
            missing_states = [state for state in all_states if state not in guessed_states]

            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break

        if answer_state in all_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)

    screen.exitonclick()

def europe_countries():
    landing_window.destroy()
    screen = turtle.Screen()
    screen.title("Europe Countries Game")
    image = "europe.gif"

    screen.addshape(image)

    turtle.shape(image)
    guessed_countries = []

    data = pandas.read_csv("./europe._countries.csv")
    all_countries = data.state.to_list()

    while (len(guessed_countries) < 50):
        answer_state = screen.textinput(title=f"{len(guessed_countries)}/34 Countries Correct",
                                        prompt="What's another country name").title()
        if answer_state == "Exit":
            missing_countries = [country for country in all_countries if country not in guessed_countries]

            new_data = pandas.DataFrame(missing_countries)
            new_data.to_csv("countries_to_learn.csv")
            break

        if answer_state in all_countries:
            guessed_countries.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)

    screen.exitonclick()



landing_window = Tk()
landing_window.title("Quiz App")
landing_window.config(padx= 50, pady=30,bg=RED)
landing_window.geometry("780x500")


title_label = Label(text="Quiz Game",fg=BLUE,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(column=2, row=0)

canvas = Canvas(height=200,width=200)
logo_img = ImageTk.PhotoImage(Image.open("killua.png"))
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=2,row=1)

state_game_button = Button(text="State Game",bg=LIGHT,height= 2, width = 20,highlightthickness=0,command=state_game)
state_game_button.grid(column=0,row=3)

country_button =Button(text="Europe Countries Game",bg=LIGHT,height= 2, width = 20,highlightthickness=0,command=europe_countries)
country_button.grid(column=3,row=3)

title_label = Label(text="Choose The Game",fg=YELLOW,bg=BLUE,font=(FONT_NAME,30))
title_label.grid(column=2, row=2)



landing_window.mainloop()
