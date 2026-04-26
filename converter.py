from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 250, height = 125)
window.config(padx=30, pady=30)

#Labels
# blank_label = Label()
# blank_label.grid(column = 0, row = 0)
mile_label = Label(text="Miles")
mile_label.grid(column = 2, row = 0)
equal_label = Label(text="is equal to")
equal_label.grid(column = 0, row = 1)
number_label = Label(text="0")
number_label.grid(column = 1, row = 1)
km_label = Label(text="Km")
km_label.grid(column = 2, row = 1)

#Entry
entry = Entry(width=5)
#Add some text to begin with
entry.insert(END, string="")
entry.grid(column = 1, row = 0)

#Button
#Buttons
def convert_miles():
   # print(entry.get())
   user_number = int(entry.get())
   user_number *= 1.609344
   # print(user_number)
   number_label.configure(text=f"{round(user_number, 1)}")

#calls action() when pressed
button = Button(text="Calculate", command=convert_miles)
button.grid(column = 1, row = 2)


window.mainloop()
