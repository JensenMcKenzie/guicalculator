# The calculation class is used to evaluate a string into an answer
class calculation:
    # Constructor
    def __init__(self):
        # The string is the string to calculate, example: 5*235 or 9/12
        self.string = ""
        # The result is the integer representation of the answer to the string, after it is evaluated
        self.result = 0

    def getString(self):
        return self.string
    def getResult(self):
        return self.result

    def setString(self, string):
        self.string = string
    def setResult(self, result):
        self.result = result

    # Evaluates the current string, and returns the result, rounded to 6 decimals
    def evalString(self):
        self.result = eval(self.string)
        if str(self.result).endswith('.0'):
            return int(self.result)
        return self.result.__round__(6)

    # After each calculation, the result will be printed to the console
    def __str__(self):
        if self.string != "":
            return self.string + " evaluates to: " + str(eval(self.string))
