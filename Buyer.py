# Buyer class

# Goal is to simulate a person buying lottery ticket(s) each day
# Person will need a salary national average = $59,384
# Dictionary to hold their tickets key = day, value = tickets bought
# Way to track how much money the person has at any given time

from Lottery import Lottery


class Buyer:
    def __init__(self, salary=60000):
        self.salary = salary
        # TODO: Make into dictionary to keep track of date purchased
        self.bought_tickets = []

    def buy_ticket(self, buy_amount):
        for i in range(buy_amount):
            ticket = Lottery()
            # TODO: Adjust so money comes out of available money
            self.salary -= ticket.cost
            ticket.create_ticket()
            self.bought_tickets.append(ticket.ticket)


alex = Buyer()

num_to_buy = int(input("How many tickets would you like to buy?"))

alex.buy_ticket(num_to_buy)

print(alex.bought_tickets)

