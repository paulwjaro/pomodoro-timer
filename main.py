from tkinter import *

window = Tk()
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
CHECK = "✔"
COUNT_SPEED = 50
checks = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global checks
    global turn
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    checks = 0
    turn = 0
    check_mark.config(text=CHECK * checks)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
turn = 0
global states
turns = [WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, LONG_BREAK_MIN]


def start_timer():
    global turns
    global turn
    global timer_text
    global checks
    if turn == 0:
        title.config(text="Work")
    if turn < len(turns):
        count_down(minutes=turns[turn], seconds=0)
    else:
        title.config(text="Timer")
        canvas.itemconfig(timer_text, text="00:00")
        turn = 0
        checks = 0
        check_mark.config(text=CHECK * checks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(minutes=5, seconds=0):
    global turn
    global timer
    global timer_text
    global checks
    if minutes > 0:
        if seconds < 0:
            seconds = 59
            minutes = minutes - 1
        canvas.itemconfig(timer_text, text=f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
        timer = window.after(COUNT_SPEED, count_down, minutes, seconds - 1)
    else:
        if seconds > 0:
            canvas.itemconfig(timer_text, text=f"00:{str(seconds).zfill(2)}")
            timer = window.after(COUNT_SPEED, count_down, minutes, seconds - 1)
        else:
            turn += 1
            if turn % 2 == 0:
                checks += 1
                check_mark.config(text=CHECK * checks)
                title.config(text="Work")
            else:
                if turn != 7:
                    title.config(text="Short Break")
                else:
                    title.config(text="Long Break")
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window.title("Pomodoro Timer")
window.config(padx=40, pady=40, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "normal"), fill="white")
canvas.grid(row=2, column=2)

title = Label(text="Timer")
title.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "normal"), pady=10)
title.grid(row=1, column=2)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=1, pady=40)
start_button.config(font=(FONT_NAME, 12, "normal"), padx=20, pady=5)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=3, column=3, pady=40)
reset_button.config(font=(FONT_NAME, 12, "normal"), padx=20, pady=5)

check_mark = Label(text=CHECK * checks)
check_mark.grid(row=3, column=2)
check_mark.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "normal"))


window.mainloop()
