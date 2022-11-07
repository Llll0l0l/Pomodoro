from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
REPS = 1
tmr = None
txt=""
checkmark = "✓"

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global txt, REPS
    window.after_cancel(tmr)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    txt = ""
    REPS = 0
    checkmarks.config(text=txt, fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global REPS

    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS%8 == 0:
        count_down(long_break_sec)
    elif REPS%2 == 0:
        count_down(short_break_sec)
    else:
        count_down(work_sec)
    

    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    global REPS, txt, checkmark, tmr
    

    if count > 0:
        count_min = count//60
        count_sec = count%60

        if count_sec<10:
            count_sec = f"0{count_sec}"


        if count_min<10:
            count_min = f"0{count_min}"

        if count > 0:
            canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
            tmr = window.after(100, count_down, count-1)
    
    if count==0:
        if (REPS)%8 == 0:
            canvas.itemconfig(timer_text, text="20:00")
            timer.config(text="Break", fg=RED)
            txt += checkmark
            checkmarks.config(text=txt)

        elif (REPS)%2 == 0:
            canvas.itemconfig(timer_text, text="05:00")
            timer.config(text="Break", fg=PINK)
            txt += checkmark
            checkmarks.config(text=txt)
        else:
            canvas.itemconfig(timer_text, text="25:00")
            timer.config(text="Timer", fg=GREEN)
        
        



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=150, pady=70, bg=YELLOW)
window.title("Pomodoro")



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


# timer label
timer = Label(text="Timer", foreground=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
timer.grid(row=1, column=2)
# start button
start = Button(text="Start", foreground=GREEN, font=(FONT_NAME, 25), bg=YELLOW, command=start_timer)
start.grid(row=3, column=1)
# reset button
reset = Button(text="Reset", foreground=GREEN, font=(FONT_NAME, 25), bg=YELLOW, command=reset)
reset.grid(row=3, column=3)


# checkmark label
checkmarks = Label(text='', foreground=GREEN, font=(FONT_NAME, 25), bg=YELLOW)
checkmarks.grid(row=4, column=2)


window.mainloop()