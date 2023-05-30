from user import User
import pwinput
import os
from time import sleep

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
                                            f'Show Information ----> enter number 1\n'
                                            f'Change username and phone number ----> enter number 2\n'
                                            f'Change password ----> enter number 3\n'
                                            f'Bank accounts ----> enter number 5\n'
                                            f'Cinema ----> enter number 6\n'
                                            f'Logout ----> enter number 0\n'
                                            f'please insert your choice : ')
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

                            case '5':
                                print('------------------------- Bank ---------------------------')

                            case '6':
                                print('------------------------- Cinema ---------------------------')
                            case _:
                                print('invalid choice!')

            case "0":
                break
            case _:
                print('invalid choice!')


if __name__ == '__main__':
    main()
