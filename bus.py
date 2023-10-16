def display_menu():
    print("Welcome to the Bus Management System!")
    print("1. View Available Tickets")
    print("2. Select Ticket")
    print("3. Exit")

def view_tickets():
    print("Available Tickets:")
    print("1. Route A - $10")
    print("2. Route B - $15")
    print("3. Route C - $20")

def select_ticket():
    ticket = input("Enter ticket number: ")
    if ticket == "1":
        print("You have selected Route A.")
        print("Your ticket costs $10.")
    elif ticket == "2":
        print("You have selected Route B.")
        print("Your ticket costs $15.")
    elif ticket == "3":
        print("You have selected Route C.")
        print("Your ticket costs $20.")
    else:
        print("Invalid ticket number. Please try again.")

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        view_tickets()
    elif choice == "2":
        select_ticket()
    elif choice == "3":
        print("Thank you for using the Bus Management System!")
        break
    else:
        print("Invalid choice. Please try again.")

class BusManagementSystem:
    def __init__(self):
        self.tickets = []
        self.blocked_cards = []
        self.tracker = None

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def cancel_ticket(self, ticket):
        self.tickets.remove(ticket)

    def block_card(self, card):
        self.blocked_cards.append(card)

    def unblock_card(self, card):
        self.blocked_cards.remove(card)

    def set_tracker(self, tracker):
        self.tracker = tracker

    def remove_tracker(self):
        self.tracker = None

    def display_tickets(self):
        for ticket in self.tickets:
            print(ticket)

    def display_blocked_cards(self):
        for card in self.blocked_cards:
            print(card)

    def display_tracker(self):
        print(self.tracker)

if __name__ == '__main__':
    bus_system = BusManagementSystem()

    while True:
        print("Welcome to the Bus Management System!")
        print("1. Add Ticket")
        print("2. Cancel Ticket")
        print("3. Block Card")
        print("4. Unblock Card")
        print("5. Set Tracker")
        print("6. Remove Tracker")
        print("7. Display Tickets")
        print("8. Display Blocked Cards")
        print("9. Display Tracker")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            ticket = input("Enter ticket details: ")
            bus_system.add_ticket(ticket)
        elif choice == 2:
            ticket = input("Enter ticket details: ")
            bus_system.cancel_ticket(ticket)
        elif choice == 3:
            card = input("Enter card number: ")
            bus_system.block_card(card)
        elif choice == 4:
            card = input("Enter card number: ")
            bus_system.unblock_card(card)
        elif choice == 5:
            tracker = input("Enter tracker details: ")
            bus_system.set_tracker(tracker)
        elif choice == 6:
            bus_system.remove_tracker()
        elif choice == 7:
            bus_system.display_tickets()
        elif choice == 8:
            bus_system.display_blocked_cards()
        elif choice == 9:
            bus_system.display_tracker()
        elif choice == 10:
            break
        else:
            print("Invalid choice. Please try again.")
