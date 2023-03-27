class cardHolder():
    def __init__(self, cardNum, pin, firstName, lastName, balance):
        self.cardNum = cardNum
        self.pin = pin
        self.lastName = lastName
        self.firstName = firstName
        self.balance = balance

    # Get methods
    def get_cardNum(self):
        return self.cardNum

    def get_pin(self):
        return self.pin

    def get_firstName(self):
        return self.firstName

    def get_lastName(self):
        return self.lastName

    def get_balance(self):
        return self.balance

    # Set methods
    def set_cardNum(self, newVal):
        self.cardNum = newVal

    def set_pin(self, newVal):
        self.pin = newVal

    def set_firstName(self, newVal):
        self.firstName = newVal

    def set_lastName(self, newVal):
        self.lastName = newVal

    def set_balance(self, newVal):
        self.balance = newVal

    def print_out(self):
        print("Card #: ", self.cardNum)
        print("Pin: ", self.pin)
        print("First name: ", self.firstName)
        print("Last name: ", self.lastName)
        print("Balance: ", self.balance)
