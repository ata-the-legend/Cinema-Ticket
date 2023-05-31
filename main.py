from user.user import User
import pwinput
import os
from time import sleep
from bank_account.bank_account import BankAccount
from cinema.cinema import Movie, Cinema, Salon, Session, Ticket, Subscription
from cinema.cinema_extra import get_user_subscription_object

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
        if User.validate_phone_number(phone_number):
            User.create_user(username, password, birthdate, phone_number)
        else: 
            User.create_user(username, password, birthdate)
            print('Phone number did not saved: invalid phone number')
        print('\n--- Your registration was successful ---\n')
        input("continue? ")
        return True
    except Exception as e:
        print(str(e))
        return False


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
    elif not User.validate_phone_number(new_phone_number):
        print('Phone number did not changed: invalid phone number')
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
                        password = pwinput.pwinput(prompt='Password for this account: ', mask='*')
                        cvv2 = pwinput.pwinput(prompt='CVV2 for this account: ', mask='*')
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
 

def cinema(user):
    while True:
        clear_screen()
        cinema_order = input(f'\n------------------------- Cinema ---------------------------\n'
                             f'hint : before select movies and buy ticket you must charge your Debit card!\n\n'
                             f'View and select movies and buy tickets ---------------> enter number (1)\n'
                             f'Debit card--------------> enter number (2)\n'
                             f'Management -------> enter number (3)\n'
                             f'Back to main menu --------------> enter number (0)\n'
                             f'\nPlease insert your choice : ')
        match cinema_order:
            case '0':
                clear_screen()
                break
            case '1':
                clear_screen()
                while True:
                    print(f'\n------------------------- Movies ---------------------------\n')
                    if Movie.show_movie():
                        print(Movie.show_movie())
                        movie_id = input('\nPlease insert your selected movie id: ')
                        try:
                            print(Cinema.show_which_cinema(movie_id, user.username))
                            cinema_id = input('\nPlease insert your selected cinema id: ')
                            print(Salon.show_which_salon(movie_id, cinema_id))
                            salon_id = input('\nPlease insert your selected salon id: ')
                            print(Session.show_which_session(movie_id, cinema_id, salon_id))
                            session_id = input('\nPlease insert your selected session id: ')
                            print(Ticket.show_ticket(user.username, session_id))
                            sure = input('are you sure to buy this ticket?(y/n)')
                            if sure == 'y':
                                Ticket.buy_ticket(user.username, session_id)
                                print('your ticket reserved successfully')
                                break
                            else:
                                print('operation canceled...!')

                        except ValueError as e:
                            print(e)
                    else:
                        print(' Movies list is empty ! ')
            case '2':
                clear_screen()
                while True:
                    debit_order = input(f'\n------------------------- Debit card ---------------------------\n'
                                        f'your subscription level: {get_user_subscription_object(user.username)["level"]}\n'
                                        f'Debit card inventory: {user.cinema_debit_card}\n\n'
                                         f'Charge your debit card---------------> enter number (1)\n'
                                         f'Buy subscription-------------> enter number (2)\n'
                                         f'Back to main menu --------------> enter number (0)\n'
                                         f'\nPlease insert your choice : ')
                    match debit_order:
                        case '1':
                            print('--------------------------------charge debit card-------------------------------')
                            amount = input('amount cash: ')
                            serial_number = input('your bank account serial number: ')
                            password = pwinput.pwinput('bank account password: ')
                            cvv2 = pwinput.pwinput('your bank account cvv2')
                            try:
                                Cinema.charge_debit_card(user.username, amount, serial_number, password, cvv2)
                            except Exception as e:
                                print(e)
                        case '2':
                            print('------------------------------- Buy Subscription -------------------------------\n')
                            print('-----------------------silver------------------------ \n'
                                  'name : silver'
                                  'price : 50,000\n'
                                  'description : This service returns 20% \n'
                                  'of the amount of each transaction to her wallet up\n'
                                  ' to three future purchases.\n')
                            print('------------------------gold------------------------ \n'
                                  'name : Gold'
                                  'price : 130,000\n'
                                  'description : This service pays 50% of the amount plus \n'
                                  ' a free energy drink for the next month\n')
                            choices_level = input('please insert your choice (gold/silver):')
                            try:
                                Subscription.buy_subscription(choices_level, user.username)
                            except Exception as e:
                                print(e)
                        case '0':
                            break
                        case _:
                            print('invalid choice')
            case '3':
                clear_screen()
                while True:
                    if user.user_role == 1:
                        management_order =\
                            input(f'\n------------------------- Management Cinema ---------------------------\n'
                                             f'Movie---------------> enter number (1)\n'
                                             f'Cinema-------------> enter number (2)\n'
                                             f'Salon--------------> enter number (3)\n'
                                             f'Session--------------> enter number (4)\n'
                                             f'Back to main menu --------------> enter number (0)\n'
                                             f'\nPlease insert your choice : ')
                        match management_order:
                            case '1':
                                clear_screen()
                                while True:
                                    movie_order = \
                                        input(f'\n-------------------------  movie  ---------------------------\n'
                                              f'Show Movie---------------> enter number (1)\n'
                                              f'Add movie---------------> enter number (2)\n'
                                              f'Edit Movie-------------> enter number (3)\n'
                                              f'Delete Movie--------------> enter number (4)\n'
                                              f'Back to main menu --------------> enter number (0)\n'
                                              f'\nPlease insert your choice : ')
                                    match movie_order:
                                        case '1':
                                            print(Movie.show_movie())
                                        case '2':
                                            name = input('name:')
                                            director = input('director:')
                                            duration_time = input('duration_time:')
                                            product_year = input('product_year:')
                                            age_limit = input('age limit:')
                                            description = input('description:')
                                            try:
                                                Movie.add_movie(name, director,
                                                                duration_time, product_year,
                                                                age_limit, description)
                                            except Exception as e:
                                                print(e)
                                        case '3':
                                            movie_id = input('movie_id:')
                                            name = input('name:')
                                            director = input('director:')
                                            duration_time = input('duration_time:')
                                            product_year = input('product_year:')
                                            age_limit = input('age limit:')
                                            description = input('description:')
                                            try:
                                                Movie.edit_movie(movie_id, name, director,
                                                                 duration_time, product_year,
                                                                 age_limit, description)
                                            except Exception as e:
                                                print(e)
                                        case '4':
                                            movie_id = input('movie_id')
                                            Movie.delete_movie(movie_id)
                                        case '0':
                                            break
                            case '2':
                                clear_screen()
                                while True:
                                    cinema_order = \
                                        input(f'\n-------------------------  cinema  ---------------------------\n'
                                              f'Show cinema---------------> enter number (1)\n'
                                              f'Add cinema---------------> enter number (2)\n'
                                              f'Edit cinema-------------> enter number (3)\n'
                                              f'Delete cinema--------------> enter number (4)\n'
                                              f'Back to main menu --------------> enter number (0)\n'
                                              f'\nPlease insert your choice : ')
                                    match cinema_order:
                                        case '1':
                                            print(Cinema.show_cinema())
                                        case '2':
                                            name = input('name:')
                                            location = input('location')
                                            working_hours = input('working_hours')
                                            try:
                                                Cinema.cinema_add(name, location,
                                                                  working_hours)
                                            except Exception as e:
                                                print(e)
                                        case '3':
                                            cinema_id = input('cinema_id')
                                            movie_id = input('movie_id:')
                                            location = input('location')
                                            working_hours = input('working_hours')
                                            try:
                                                Cinema.cinema_edit(cinema_id,movie_id,location, working_hours)
                                            except Exception as e:
                                                print(e)
                                        case '4':
                                            cinema_id = input('cinema_id')
                                            Cinema.delete_cinema(cinema_id)
                                        case '0':
                                            break

                            case '3':
                                clear_screen()
                                while True:
                                    cinema_order = \
                                        input(f'\n-------------------------  salon  ---------------------------\n'
                                              f'Show salon---------------> enter number (1)\n'
                                              f'Add salon---------------> enter number (2)\n'
                                              f'Edit salon-------------> enter number (3)\n'
                                              f'Delete salon--------------> enter number (4)\n'
                                              f'Back to main menu --------------> enter number (0)\n'
                                              f'\nPlease insert your choice : ')
                                    match cinema_order:
                                        case '1':
                                            print(Cinema.show_cinema())
                                        case '2':
                                            name = input('name:')
                                            location = input('location')
                                            working_hours = input('working_hours')
                                            try:
                                                Cinema.cinema_add(name, location,
                                                                  working_hours)
                                            except Exception as e:
                                                print(e)
                                        case '3':
                                            cinema_id = input('cinema_id')
                                            movie_id = input('movie_id:')
                                            location = input('location')
                                            working_hours = input('working_hours')
                                            try:
                                                Cinema.cinema_edit(cinema_id, movie_id, location, working_hours)
                                            except Exception as e:
                                                print(e)
                                        case '4':
                                            cinema_id = input('cinema_id')
                                            Cinema.delete_cinema(cinema_id)
                                        case '0':
                                            break
                            case '4':
                                ...
                            case '0':
                                break
                            case _:
                                print('invalid choice')
                    else:
                        print('you dont have access to this menu ! just Staff...')
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
                                cinema(user)
                                
                            case _:
                                print('invalid choice!')

            case "0":
                break
            case _:
                print('invalid choice!')


if __name__ == '__main__':
    main()
