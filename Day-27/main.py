from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


def button_click():
    print("Calculating")
    km = int(input.get())
    km *= 1.61
    conversion_label.config(text=km)


# Calculate Button
button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)

#label text for Miles
label = Label()
label.config(text="Miles")
label.grid(column=2, row=0)
# label.config(padx=50, pady=50) #helps put padding around item


"""Conversion line labels"""

# conversion label
text_label = Label(text='is equal to ')
text_label.grid(column=0, row=1)

conversion_label = Label(text="0")
conversion_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


#Input
input = Entry(width=10)
input.insert(END, string='0')
input.get()
input.grid(column=1, row=0)




window.mainloop()