# The button and value class stores a tkinter button, and text value of that button
class button_and_value:
    #Constructor
    def __init__(self, button):
        # Set the current button to the button
        self.button = button
        # Set the symbol to the button's text
        self.symbol = button.cget('text')

    def getButton(self):
        return self.button
    def getSymbol(self):
        return self.symbol

    def setButton(self, button):
        self.button = button
    def setSymbol(self, symbol):
        self.symbol = symbol

    # Prints the symbol contained in the current button and value object
    def __str__(self):
        return "This is the " + self.symbol + " button"
