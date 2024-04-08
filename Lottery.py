# Lottery class

# Following Powerball rules
# First 5 numbers 1 -69 last number (Powerball) 1 - 26
# Each play cost $2
import random


# Will need to include:
# Winning lottery number
# Generate lottery numbers
# The winning $ amount
# Cost to buy a lottery ticket

class Lottery:
    cost = 2
    def __init__(self):
        self.ticket = []

    def create_ticket(self):
        for i in range(6):
            # Creates the Powerball Number
            if i == 5:
                self.ticket.append(random.randrange(1, 26))
            # Creates 5 lottery number
            else:
                self.ticket.append(random.randrange(1, 69))



winning_ticket = Lottery()
winning_ticket.create_ticket()
print(winning_ticket.ticket)
