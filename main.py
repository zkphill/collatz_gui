from tkinter import *
from tkinter import messagebox

collatz_numbers = []
output_string = ""
counter = 0
flag = False


''' create window '''
app_gui = Tk()
string = StringVar()

def collatz_calculator():
    ''' implements collatz conjecture algorithm '''

    global counter, flag
    collatz_reset()
    num = my_Entry.get()
    if num.isdigit():
        flag = True
        num1 = int(num)
        collatz_numbers.append(num1)
        while num1 > 1:
            if num1 % 2 == 0:
                num1 = num1 // 2
                collatz_numbers.append(num1)
                counter += 1
            else:
                num1 = num1*3 + 1
                collatz_numbers.append(num1)
                counter += 1

def collatz_format():
    global output_string

    if flag:
        for num in range(0, counter + 1 ):
            output_string = output_string + str(collatz_numbers[num]) + ", "
            string.set(output_string)

def collatz_print():
    ''' displays all the numbers and the step count '''
    collatz_format()
    print_label = Label(app_gui, textvariable = string)
    print_label.grid(row = 4, column = 0)

def collatz_reset():
    ''' resets global variables '''
    global counter, collatz_numbers, output_string
    counter = 0
    collatz_numbers = []
    output_string = ""

    ''' make the reset function print a blank label '''


''' create input variables '''
my_entry = StringVar()

''' window formating '''
app_gui.geometry('800x400+300+400')
app_gui.title('Collatz Calculator')

''' labels '''


''' buttons '''
calc_button = Button(app_gui, text = 'Calculate', command = collatz_calculator)
print_button = Button(app_gui, text = 'Print Results', command = collatz_print)
reset_button = Button(app_gui, text = 'reset', command = collatz_reset)
calc_button.grid(row = 1, column = 1)
print_button.grid(row = 1, column = 2)
reset_button.grid(row = 1, column = 3)

''' input fields '''
my_Entry = Entry(app_gui, textvariable = my_entry)
my_Entry.grid(row = 1, column = 0)

app_gui.mainloop()
