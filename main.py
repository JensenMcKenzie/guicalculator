'''
DEVELOPER: Jensen McKenzie
COLLABORATORS: No one
DATE: 5.17.22
'''

"""A basic calculator application using tkinter.

This basic calculator is modeled after the iPhone's calculator. It can perform multiplication, division, subtraction and addition. It can also clear data, perform operation chains (repeatedly hitting equals), calcualte percents, and deal with both positive and negative numbers. It is equipped with an error system, which will engage if the entered number is too large.
"""

##########################################
# IMPORTS:
# Tkinter is used to generate the ui
# The button and value class stores a button and a value associated with it
# The calculation class uses python's eval() function to evaluate and return strings
##########################################
from tkinter import *
import button_and_value
import calculation

##########################################
# FUNCTIONS:
##########################################
# Storage for previous number and operators, the active operator and the operator down status
previous_number = ""
active_operator = ""
previous_operator = ""
operator_down = False


# The main UI function
def generate_window():
    window = Tk()
    window.geometry("480x751")
    window.title("Calculator")

    display_text = StringVar()
    display_text.set("0")
    display = Label(textvariable=display_text, background="gainsboro", anchor="se", font=("Arial", 50))
    display.place(x=0, y=0, width=480, height=150)

    # When any number button is pressed, pass the button and value object
    # This function checks the input and screen state for validity, then adds the number to the screen
    def button_action(button):
        global active_operator
        if len(display_text.get()) < 12 or operator_down:
            clear.config(text="C")
            if active_operator != "" and operator_down:
                next_number()
            if display_text.get() == '0' or (active_operator == "" and previous_number != ""):
                display_text.set(button.symbol)
            else:
                display_text.set(display_text.get() + button.symbol)

    # When any operator button is pressed, pass the button and value object
    # This function checks the input and screen state for validity, then sets the active operator and updates the
    # button's pressed state
    def operator_action(button):
        global active_operator, operator_down
        if display_text.get() == "ERROR":
            return
        temp = button.button.cget('relief')
        raise_operators()
        if temp == SUNKEN:
            active_operator = ""
            button.button.config(relief=RAISED)
        else:
            operator_down = True
            active_operator = button.symbol
            button.button.config(relief=SUNKEN)

    # Resets the operator down status, and raises all operator buttons
    def raise_operators():
        global operator_down
        operator_down = False
        divide.button.config(relief=RAISED)
        multiply.button.config(relief=RAISED)
        subtract.button.config(relief=RAISED)
        add.button.config(relief=RAISED)

    # Raises all operator buttons, stores the previous number, and sets the display to 0
    def next_number():
        global previous_number, active_operator
        raise_operators()
        previous_number = display_text.get()
        display_text.set("0")

    # Clears the current number if pressed once, then clears the current operator if pressed again. Will also reset
    # the error status and operator pressed state
    def clear_action():
        global active_operator, previous_operator, previous_number
        if display_text.get() != "0":
            if active_operator == "":
                clear.config(text="AC")
            else:
                if active_operator == "+":
                    add.button.config(relief=SUNKEN)
                elif active_operator == "-":
                    subtract.button.config(relief=SUNKEN)
                elif active_operator == "*":
                    multiply.button.config(relief=SUNKEN)
                elif active_operator == "/":
                    divide.button.config(relief=SUNKEN)
            display_text.set("0")
        else:
            if active_operator != "":
                raise_operators()
                active_operator = ""
            previous_operator = ""
            previous_number = ""

    clear = Button(text="AC", background='white', font=("Arial", 50), command=clear_action)
    clear.place(x=0, y=150, width=120, height=120)

    # Makes the current number + or -
    def change_sign_action():
        if display_text.get() != '0' and display_text.get() != "ERROR":
            if display_text.get()[0] != '-':
                display_text.set('-' + display_text.get())
            else:
                display_text.set(display_text.get()[1:])

    change_sign = Button(text="+/-", background='white', font=("Arial", 50), command=change_sign_action)
    change_sign.place(x=120, y=150, width=120, height=120)

    # Calculates the current number divided by 100
    def percent_action():
        if display_text.get() != '0' and display_text.get() != "ERROR":
            calc.setString(display_text.get() + "/100")
            display_text.set(calc.evalString())
            print(calc)

    percent = Button(text="%", background='white', font=("Arial", 50), command=percent_action)
    percent.place(x=240, y=150, width=120, height=120)

    # Adds a division operator to the calculator
    def divide_action():
        operator_action(divide)

    divide = button_and_value.button_and_value(
        Button(text="/", background='white', font=("Arial", 50), command=divide_action))
    divide.button.place(x=360, y=150, width=120, height=120)

    # Adds the number 7 to the screen, after checking for validity
    def seven_action():
        button_action(seven)

    seven = button_and_value.button_and_value(
        Button(text="7", background='white', font=("Arial", 50), command=seven_action))
    seven.button.place(x=0, y=270, width=120, height=120)

    # Adds the number 8 to the screen, after checking for validity
    def eight_action():
        button_action(eight)

    eight = button_and_value.button_and_value(
        Button(text="8", background='white', font=("Arial", 50), command=eight_action))
    eight.button.place(x=120, y=270, width=120, height=120)

    # Adds the number 9 to the screen, after checking for validity
    def nine_action():
        button_action(nine)

    nine = button_and_value.button_and_value(
        Button(text="9", background='white', font=("Arial", 50), command=nine_action))
    nine.button.place(x=240, y=270, width=120, height=120)

    # Adds a multiplication operator to the calculator
    def multiply_action():
        operator_action(multiply)

    multiply = button_and_value.button_and_value(
        Button(text="*", background='white', font=("Arial", 50), command=multiply_action))
    multiply.button.place(x=360, y=270, width=120, height=120)

    # Adds the number 4 to the screen, after checking for validity
    def four_action():
        button_action(four)

    four = button_and_value.button_and_value(
        Button(text="4", background='white', font=("Arial", 50), command=four_action))
    four.button.place(x=0, y=390, width=120, height=120)

    # Adds the number 5 to the screen, after checking for validity
    def five_action():
        button_action(five)

    five = button_and_value.button_and_value(
        Button(text="5", background='white', font=("Arial", 50), command=five_action))
    five.button.place(x=120, y=390, width=120, height=120)

    # Adds the number 6 to the screen, after checking for validity
    def six_action():
        button_action(six)

    six = button_and_value.button_and_value(
        Button(text="6", background='white', font=("Arial", 50), command=six_action))
    six.button.place(x=240, y=390, width=120, height=120)

    # Adds a subtraction operator to the calculator
    def subtract_action():
        operator_action(subtract)

    subtract = button_and_value.button_and_value(
        Button(text="-", background='white', font=("Arial", 50), command=subtract_action))
    subtract.button.place(x=360, y=390, width=120, height=120)

    # Adds the number 1 to the screen, after checking for validity
    def one_action():
        button_action(one)

    one = button_and_value.button_and_value(
        Button(text="1", background='white', font=("Arial", 50), command=one_action))
    one.button.place(x=0, y=510, width=120, height=120)

    # Adds the number 2 to the screen, after checking for validity
    def two_action():
        button_action(two)

    two = button_and_value.button_and_value(
        Button(text="2", background='white', font=("Arial", 50), command=two_action))
    two.button.place(x=120, y=510, width=120, height=120)

    # Adds the number 3 to the screen, after checking for validity
    def three_action():
        button_action(three)

    three = button_and_value.button_and_value(
        Button(text="3", background='white', font=("Arial", 50), command=three_action))
    three.button.place(x=240, y=510, width=120, height=120)

    # Adds an addition operator to the calculator
    def add_action():
        operator_action(add)

    add = button_and_value.button_and_value(
        Button(text="+", background='white', font=("Arial", 50), command=add_action))
    add.button.place(x=360, y=510, width=120, height=120)

    # Adds the number 0 to the screen, after checking for validity
    def zero_action():
        if display_text.get() == "ERROR":
            clear.config(text="AC")
            display_text.set('0')
        elif display_text.get() != '0':
            clear.config(text="C")
            display_text.set(display_text.get() + '0')

    zero = Button(text="0", background='white', font=("Arial", 50), command=zero_action)
    zero.place(x=0, y=630, width=240, height=120)

    # Adds a decimal point to the screen, after checking for validity
    def decimal_action():
        if display_text.get()[len(display_text.get()) - 1] != '.' and display_text.get() != "ERROR":
            display_text.set(display_text.get() + '.')

    decimal = Button(text=".", background='white', font=("Arial", 50), command=decimal_action)
    decimal.place(x=240, y=630, width=120, height=120)

    # Calculates the current operation, given the current number, current operator and previous number
    # If equals is pressed repeatedly, it will continue to calculate using the previous number and previous operator
    # Sets the screen to an error message if the length of the number is greater than or equal to 12
    def equal_action():
        global active_operator, previous_number, previous_operator
        if display_text.get() == "ERROR":
            return
        if active_operator != "" and previous_number != "":
            calc.setString(previous_number + active_operator + display_text.get())
            previous_number = display_text.get()
            previous_operator = active_operator
            if len(str(calc.evalString())) < 12:
                display_text.set(calc.evalString())
            else:
                display_text.set("ERROR")
                previous_operator = ""
                previous_number = ""
            raise_operators()
            active_operator = ""
            print(calc)
        elif previous_operator != "":
            calc.setString(display_text.get() + previous_operator + previous_number)
            if len(str(calc.evalString())) < 12:
                display_text.set(calc.evalString())
            else:
                display_text.set("ERROR")
                previous_operator = ""
                previous_number = ""
            print(calc)

    equal = Button(text="=", background='white', font=("Arial", 50), command=equal_action)
    equal.place(x=360, y=630, width=120, height=120)

    calc = calculation.calculation()
    window.mainloop()


##########################################
# MAIN PROGRAM:
##########################################
def main():
    generate_window()


if __name__ == "__main__":
    main()
