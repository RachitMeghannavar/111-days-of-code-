from tkinter import *

window = Tk()
window.title("Miles to Km")
window.minsize(width=250 , height=150)
window.config(padx=30 , pady=30)
number = Entry(width=10)
number.grid(row = 0, column = 1)
equal_label = Label(text="Is equal to ")
equal_label.grid(row = 1, column =0 )
miles_label = Label(text="Miles")
miles_label.grid(row = 0, column = 2)
result_label = Label(text = " ")
result_label.grid(row = 1, column = 1)
km_label = Label(text="Km")
km_label.grid(row = 1, column = 2)

def calculate_kms():
    output = float(number.get()) * 1.6
    output = round(output,2)
    result_label.config(text = output)

calculate_button = Button(text="Calculate", command=calculate_kms)
calculate_button.grid(row = 2, column = 1)



window.mainloop()
