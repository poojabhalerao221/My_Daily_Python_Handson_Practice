class Railway:
    def __init__(self):
        self.trains = {
            101: ("express", 5),
            102: ("Superfast", 3),
            103: ("passenger", 4)
        }
        self.reservation = []

    def view_trains(self):
        print("\nAvailable trains:")
        for train_no, info in self.trains.items():
            name, seat = info
            print(f"Train No: {train_no}, Name: {name}, Seats Available: {seat}")
    print()


class ReservationSystem(Railway):

    def book_ticket(self):
        name = input("Enter the Passenger name: ")
        train_no = int(input("Enter the Train number: "))

        if train_no in self.trains:
            train_name, seats = self.trains[train_no]

            if seats > 0:
                self.trains[train_no] = (train_name, seats - 1)

                ticket = {
                    "name": name,
                    "train_no": train_no,
                    "train_name": train_name
                }

                self.reservation.append(ticket)
                print("Ticket booked successfully")
            else:
                print("No seats available")
        else:
            print("Train not found")

    def cancel_ticket(self):
        name = input("Enter the passenger name to cancel ticket: ")

        for ticket in self.reservation:
            if ticket['name'] == name:
                train_no = ticket['train_no']
                train_name, seats = self.trains[train_no]

                self.trains[train_no] = (train_name, seats + 1)
                self.reservation.remove(ticket)

                print("Ticket cancelled")
                return

        print("Reservation not found")   # ✅ moved outside loop

    def view_reservations(self):
        if not self.reservation:
            print("No Reservation found")
            return

        print("\nReservation list:")
        for ticket in self.reservation:
            print("Passenger:", ticket['name'])
            print("Train number:", ticket['train_no'])
            print("Train Name:", ticket['train_name'])
            print()


def main():
    system = ReservationSystem()

    while True:
        print("===== Railway Reservation =======")
        print("1. View Trains")
        print("2. Book Tickets")
        print("3. Cancel Tickets")
        print("4. View Reservations")
        print("5. Exit")

        choice = int(input("Enter the choice: "))

        if choice == 1:
            system.view_trains()
        elif choice == 2:
            system.book_ticket()
        elif choice == 3:
            system.cancel_ticket()
        elif choice == 4:
            system.view_reservations()
        elif choice == 5:
            print("Thank you for using this app")
            break
        else:
            print("Invalid choice")


main()