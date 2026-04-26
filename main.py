from tkinter import *

def button_clicked():
    my_label.config(text="I got clicked")
    print("I got clicked")

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)
new_button = Button(text="Click me next!", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
user_input = Entry(width=10)
print(user_input.get())
user_input.grid(column=8, row=8)

window.mainloop()