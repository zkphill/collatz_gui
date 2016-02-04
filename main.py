from tkinter import *
from tkinter import messagebox

collatz_numbers = [0]


''' print '''

def my_print():
    my_text = my_Entry.get()
    print_label = Label(app_gui, text = my_text)
    print_label.grid(row = 2, column = 1)

def collatz_calculator():

    num = my_Entry.get()

    if num.isdigit():
        num1 = int(num)
        if num1 % 2 == 0:
            print (num1 // 2)
        else:
            print (num1 * 3 + 1)

    return

def collatz_test(lower_bound, upper_bound):
    num_steps = 0
    for num in range(lower_bound, upper_bound):

        while num > 1:
            num = collatz_calculator(num)
            num_steps += 1
    return num_steps

''' create window '''
app_gui = Tk()

''' create input variables '''
my_entry = StringVar()

''' window formating '''
app_gui.geometry('800x400+300+400')
app_gui.title('Collatz Calculator')

''' labels '''
my_label_1 = Label(app_gui, text = "Enter a number:")
my_label_1.grid(row = 0, column = 0, sticky = W)

''' buttons '''
my_button = Button(app_gui, text = 'Calculate', command = collatz_calculator)
my_button.grid(row = 1, column = 1)

''' input fields '''
my_Entry = Entry(app_gui, textvariable = my_entry)
my_Entry.grid(row = 1, column = 0)

app_gui.mainloop()
