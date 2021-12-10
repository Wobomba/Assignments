#prompting the user to enter the name and pin
name = input('Enter your name: ')
pin = 0000
usr_pin = int(input('Enter the pin: '))

#function to compute the balance after withdraw
def withdraw():
    bal = 5000000
    amount = int(input("Enter the desired amount that you want to withdraw: "))
    if amount > bal:
        print('Insufficient amount')
    elif amount < bal:
        bal-=amount
        #displaying the new account balance
        print('Your account balance is: '+str(bal))
    else:
        print('You cannot withdraw this amount')

if usr_pin == pin:
   withdraw()

#pin validation 
else:
    attempts = 1
    print('Incorrect pin. Try again')
    usr_pin = int(input('Enter the pin: '))

    while attempts > 0:
        print('You have '+str(attempts)+' left')
        attempts+=-1
        usr_pin = int(input('Enter the pin: '))
        if usr_pin == pin:
            withdraw()
        elif attempts == 0:
            print('Your card has been swallowed')
        else:
            continue
        



   