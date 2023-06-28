# Your parking garage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

class MyGarage():
    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.parkingSpaces = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'D3']
        self.currentTicket = {
            'paid': False,
            'ticket number': '',
            'parking space': ''
        }

# Give the user a ticket and adjust the spots/tickets by -1.  If no additional spaces are available will inform the user and end the program.

    def takeTicket(self):
        if self.tickets and len(self.parkingSpaces) > 0:
            print('Please wait while your ticket prints...')
            print('Garage fee is $1.00 per hour.')
            self.currentTicket['ticket number'] = self.tickets.pop(0)
            self.currentTicket['parking space'] = self.parkingSpaces.pop(0)
            print(f"You have ticket number {self.currentTicket['ticket number']}")
            print(f"Thank you. Please take your ticket and proceed to your parking spot {self.currentTicket['parking space']}.\n")
            

        elif self.tickets or len(self.parkingSpaces) == 0:
            print('There are no additional parking spaces at this time.')
            print('Please return at a later time.  Sorry for the inconvenience.')


# Will ask the user for time spent in the garage and multiply it by the rate, then ask the user to pay.  If payment no equal to the fee, will ask for the correct amount.

    def payForParking(self):

        print('\nPlease input your ticket.')
        self.payment = input('\nPlease tell me how long you have been parked (to the nearest hour, min of 1 hour): ')
        pay_me = input(f'Your total is: ${self.payment} dollars.  Please input the total for payment: ')
        
        if self.payment == pay_me:
            print('Thank you for your patronage, please leave the parking garage within 15 minutes.')
            self.currentTicket['paid'] = True
            return self.currentTicket['paid']
        else:
            print('You did not put in the correct amount. Please input the correct amount.')
            input(f'Your total is: ${self.payment} dollars.  Please input the total for payment: ')
            if self.payment == pay_me:
                self.currentTicket['paid'] = True
                return self.currentTicket['paid']

# Checks if 'paid' is True and allows the driver to leave if it is.

    def leaveGarage(self):
        print('\nPlease insert your ticket to confirm payment.')

        if self.currentTicket['paid'] == True:
            print('Thank you, please come back soon and have a nice day!')
            self.tickets.append(self.currentTicket['ticket number'])
            self.currentTicket['ticket number'] = ''
            self.parkingSpaces.append(self.currentTicket['parking space'])
            self.currentTicket['parking space'] = ''

        elif self.currentTicket['paid'] == False:
            self.payment = input('Please tell me how long you have been parked (to the nearest hour, min of 1 hour): ')
            pay_me = input(f'Your total is: ${self.payment} dollars.  Please input the total for payment: ')
            if self.payment == pay_me:
                print('Thank you, please come back soon and have a nice day!')
                self.currentTicket['paid'] = True
                self.tickets.append(self.currentTicket['ticket number'])
                self.currentTicket['ticket number'] = ''
                self.parkingSpaces.append(self.currentTicket['parking space'])
                self.currentTicket['parking space'] = ''
                return self.currentTicket['paid']
            
            else:
                print('You did not put in the correct amount. Please input the correct amount.')
                pay_me = input(f'Your total is: ${self.payment} dollars.  Please input the total for payment: ')
                if self.payment == pay_me:
                    print('Thank you, please come back soon and have a nice day!')


my_garage = MyGarage()
my_garage.takeTicket()
my_garage.payForParking()
my_garage.leaveGarage()




