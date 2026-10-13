from tkinter import *

window = Tk()  #creating the window object
window.title('My first GUI app')
window.minsize(600, 500)
# Graphical User Interface vs CLI = Command Line Interface
# label
# adding text to the middle of the window
my_label = Label(text="I am a Label" , font=("Arial", 24, "bold"))
# my_label.pack()
my_label.grid(column=0, row=0)

# Updating the text of label
my_label['text'] = " Rachit "
my_label.config(text= "RNtejas" , font=("Arial", 48, "bold"))

def got_clicked():
    print("I got clicked")
    my_label.config(text=f"hello , {name.get()}")

# creating a button

button = Button(text = "Click me", command = got_clicked)
button.grid(column=1, row=1)

# taking input
name= Entry()
name.grid(column=0, row=1)

label_2 = Label(text="WelCome to my app" , font=("Arial", 24, "bold"))
label_2.place(x=150 , y=250)


window.mainloop()