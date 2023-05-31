from user import User
import pwinput
import os
from time import sleep
from ..bank_account.bank_account import BankAccount

def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        # os.name = 'nt'
        os.system('cls')

def sign_up():
    clear_screen()
    print('---------------------------------- Signup ----------------------------------\n\n'
          'hint: The length of the password must be more than 4 characters\n')
    username = input('Username: ')
    password = pwinput.pwinput(prompt='Password: ', mask='*')
    phone_number = input('Phone number (optional): ')
    birthdate = input('Birthdate:(year-month-day) ') 
    try:
        if phone_number.isspace() or not phone_number: 
            User.create_user(username, password, birthdate)
        else:
            User.create_user(username, password, birthdate, phone_number)
        print('\n--- Your registration was successful ---\n')
    except Exception as e:
        print(str(e))


def login():
    clear_screen()
    print('---------------------------------- Login ----------------------------------\n\n'
        'hint: The length of the password must be more than 4 characters\n')
    username = input('Username: ')
    password = pwinput.pwinput(prompt='Password: ', mask='*')
    try:
        return(True , User.login(username, password))
    except Exception as e:
        print(str(e))
        return (False , None)

def edit_prof(user):
    clear_screen()
    print('------------------------- Change information ---------------------------')
    new_username = input('new username (if you want update it): ')
    new_phone_number = input('new phone_number (if you want update it): ')
    if new_username == '':
        new_username = user.username
        # if user is not str: ##??
    if new_phone_number == '':
        new_phone_number = user.phone_number
    try:
        user.change_info(new_username, new_phone_number)
        print('\n--- your account is updated successfully ---')
        return True
    except Exception as e:
        print(str(e))
        return False

def edit_pass(user):
    clear_screen()
    print('------------------------- Change Password ---------------------------')
    old_password = pwinput.pwinput('old_password : ')
    new_password = pwinput.pwinput('new_password : ')
    confirm_new_password = pwinput.pwinput('confirm_new_password : ')
    try:
        user.change_password(old_password, new_password, confirm_new_password)
        print('--- your password updated successfully ---')
        return True
    except Exception as e:
        print(str(e))
        return False
    
def bank_operation(serial: str):
    user_account = BankAccount.show_account(serial)
    while True:
        clear_screen()
        operation_order = input(f'\nSelect your operation:'
                                f'\n\n'
                                f'Deposit ------------> enter number (1)\n' #variz
                                f'Withdraw -----------> enter number (2)\n'
                                f'Transfer -----------> enter number (3)\n'
                                f'Cancel -------------> enter number (0)\n'
                                f'\nPlease insert your choice : ')
        match operation_order:
            case '0':
                break

            case '1':
                clear_screen()
                try:
                    amount = int(input('Amount: '))
                    inventory = user_account.add(amount)
                except ValueError as e:
                    print(str(e))
                    print("Operation was unsuccessful!")
                    sleep(3)
                else:
                    print("Operation was successful!")
                    print(f'Inventory: {inventory}')
                    input('Back to operations menu:(Y) ')

            case '2':
                clear_screen()
                try:
                    amount = int(input('Amount: '))
                    password = pwinput(prompt='Password for this account: ', mask='*')
                    inventory = user_account.sub(amount, password)
                except ValueError as e:
                    print(str(e))
                    print("Operation was unsuccessful!")
                    sleep(3)
                else:
                    print("Operation was successful!")
                    print(f'Inventory: {inventory}')
                    input('Back to operations menu:(Y) ')

            case '3':
                clear_screen()
                destination_account = input('Enter destination account serial: ')
                if BankAccount.is_serial(destination_account):
                    try:
                        amount = int(input('Amount: '))
                        password = pwinput(prompt='Password for this account: ', mask='*')
                        cvv2 = pwinput(prompt='CVV2 for this account: ', mask='*')
                        user_account.transfer_to_another(BankAccount.show_account(destination_account), amount, password, cvv2)
                    except ValueError as e:
                        print(str(e))
                        print("Operation was unsuccessful!")
                        sleep(3)
                    else:
                        print("Operation was successful!")
                        input('Back to operations menu:(Y) ')
                else:
                    print('Invalid account serial!')
                    sleep(3)
    # create account --> serial , pass
        #input --bank name(menu) --balance
        #save in user accounts
    # show account --> for user.accounts print(show account
    # bank oprations
        #input --serial
        #useraccount --> show account
        # add
            #inp --int(ammount
        # sub
            #input --int(amount --pass
        # tranfer
            #input --other account --int(amount) --pass --cvv2 
            #userother --> show account

def bank(user: User):
    while True:
        clear_screen()
        bank_order = input(f'\n------------------------- Bank ---------------------------'
                            f'\n\n'
                            f'Open new account ---------------> enter number (1)\n'
                            f'Show my current accounts -------> enter number (2)\n'
                            f'Banking operations--------------> enter number (3)\n'
                            f'Back to main menu --------------> enter number (0)\n'
                            f'\nPlease insert your choice : ')
        match bank_order:
            case '0':
                break

            case '1':
                banks = {
                    '1': 'Ayande',
                    '2': 'Saman',
                    '3': 'Pasargad',
                }
                while True:
                    clear_screen()
                    bank_name = input(f'\nSelect a bank to open account:'
                                f'\n\n'
                                f'Ayande -----------> enter number (1)\n'
                                f'Saman ------------> enter number (2)\n'
                                f'Pasargad ---------> enter number (3)\n'
                                # f'Cancel ---------> enter number (4)\n'
                                f'\nPlease insert your choice : ')
                    if bank_name in banks.keys():
                        break
                    print('invalid choice!')
                    sleep(3)

                while True:
                    amount = input("\nPrimary deposit amount: ")
                    try:
                        user_account = BankAccount.create_account(user.username, banks[bank_name], int(amount))
                    except ValueError as e:
                        print(str(e))
                    else:
                        user.save_bank_account(user_account.serial_number)
                        clear_screen()
                        print(user_account)
                        input('\nBack to bank menu:(Y) ')
                        break
                    if input('Cancel:(Y) ').lower() == 'y':
                        print("Operation was unsuccessful!")
                        sleep(3)
                        break 
                    
            case '2':
                clear_screen()
                print('Your available accounts:')
                for serial in user.bank_accounts:
                    print('\n')
                    print(BankAccount.show_account(serial))
                input('\nBack to bank menu:(Y) ')

            case '3':
                while True:
                    clear_screen()
                    serial = input('Enter your account number: ')
                    if BankAccount.is_serial(serial):
                        bank_operation(serial)
                        input('\nBack to bank menu:(Y) ')
                        break
                    if input('\nIncorrect serial.\nTry again:(Y/N) ').lower() == 'n':
                        break

            case _:
                print('invalid choice!')
 


def main():
    while True:
        clear_screen()
        input_order = input('\n---------------------------------Welcome to P.A.R.A app-------------------------------\n'
                            'Signup ----> enter number 1 \n'
                            'Login ----> enter number 2 \n'
                            'Exit ----> enter number 0 \n'
                            'Please insert your choice : ')

        match input_order:
            case "1":
                sign_up_flag = sign_up()
                while not sign_up_flag:
                    if input("Try again?(y/n): ").lower() == 'n':
                        break 
                    sign_up_flag = sign_up()

            case "2":
                (login_flag, user) = login()
                while not login_flag:
                    print('Wrong username, password')
                    if input("Try again?(y/n): ").lower() == 'n':
                        break 
                    (login_flag, user) = login()
                else:               
                    while True:
                        clear_screen()
                        input_order = input(f'\n------------------------ Welcome {user.username} ----------------------'
                                            f'\n\n'
                                            f'Show Information -----------------------> enter number (1)\n'
                                            f'Change username and phone number -------> enter number (2)\n'
                                            f'Change password ------------------------> enter number (3)\n'
                                            f'Bank accounts --------------------------> enter number (4)\n'
                                            f'Cinema ---------------------------------> enter number (5)\n'
                                            f'Logout ---------------------------------> enter number (0)\n'
                                            f'\nPlease insert your choice : ')
                        match input_order:
                            case '0':
                                break
                            case '1':
                                clear_screen()
                                print('---------------------------- Information -------------------------------')
                                print(user)
                                while True :
                                    if not input('\nBack to main menu:(Y/N)').lower() == 'n':
                                        break

                            case '2':
                                change_profile = edit_prof(user) # if True --> profile changed 
                                while not change_profile:
                                    if input("Try again?(y/n): ").lower() == 'n':
                                        break 
                                    change_profile = edit_prof(user)
                                while True :
                                    if not input('\nBack to main menu:(Y/N)').lower() == 'n':
                                        break
                       
                            case '3':
                                change_pass = edit_pass(user) # if True --> pass changed 
                                while not change_pass:
                                    if input("Try again?(y/n): ").lower() == 'n':
                                        break 
                                    change_pass = edit_pass(user)
                                if change_pass:
                                    sleep(3)
                                    break

                            case '4':
                                bank(user)

                            case '5':
                                cinema()
                                print('------------------------- Cinema ---------------------------')
                            case _:
                                print('invalid choice!')

            case "0":
                break
            case _:
                print('invalid choice!')


if __name__ == '__main__':
    main()
