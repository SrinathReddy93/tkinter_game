import tkinter as tk
import random

counter = 1
matchCount = 0
totalSec = 21


def main_function(label):

    def getusercount():
        e.pack()
        e.focus_set()
        submit.pack()

    def count():
        global counter
        counter += 1
        if counter == totalSec:
            label.destroy()
            getusercount()
            return

        fg = random.randint(0, 8)
        txt = random.randint(0, 8)
        global matchCount
        if fg == txt:
            matchCount += 1
        label.config(fg=str(colours[fg]), text=str(colours[txt]))
        label.after(1000, count)

    count()


def calculate_result():
    global matchCount
    if int(matchCount) == int(e.get()):
        txt = 'You won!!!'
    else:
        txt = 'You lost, System count {}, Your count {}'.format(matchCount, e.get())
    submit.destroy()
    tk.Label(root, text=txt).pack()


colours = ['Red', 'Blue', 'Yellow', 'Orange', 'Purple', 'Brown', 'Green', 'Pink', 'Black']
root = tk.Tk()
instructions = """1)This game is run for 21 seconds.
2)If color of the text and text is same make count.
3)After 21 seconds type your total count and press submit.
4)If your count match with system code, your won or sorry try again."""

tk.Label(root, text=instructions).pack()
root.title("Match color")
label = tk.Label(root, fg="green")
label.pack()
startButton = tk.Button(root, text='Start', width=25, command=main_function(label))
submit = tk.Button(root, text='submit', width=25, command=calculate_result)
button = tk.Button(root, text='Quite', width=25, command=root.destroy)
button.pack()
e = tk.Entry(root, width=50, justify=tk.CENTER)
root.mainloop()
