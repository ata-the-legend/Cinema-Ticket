from user import User
import pwinput
import os

def clear_screan():
    if os.name == 'posix':
        os.system('clear')
    else:
        # os.name = 'nt'
        os.system('cls')

def sign_up():
    clear_screan()
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
    clear_screan()
    print('---------------------------------- Login ----------------------------------\n\n'
        'hint: The length of the password must be more than 4 characters\n')
    username = input('Username: ')
    password = pwinput.pwinput(prompt='Password: ', mask='*')
    try:
        return(True , User.login(username, password))
    except Exception as e:
        print(str(e))
        return (False , None)


def main():
    while True:
        clear_screan()
        input_order = input('\n---------------------------------Welcome to P.A.R.A app-------------------------------\n'
                            'Signup ----> enter number 1 \n'
                            'Login ----> enter number 2 \n'
                            'Exit ----> enter number 0 \n'
                            'Please insert your choice : ')

        match input_order:
            case "1":
                sign_in_flag = sign_up()
                while not sign_in_flag:
                    if input("Try again?(y/n): ").lower() == 'n':
                        break 
                    sign_in_flag = sign_up()

            case "2":
                (login_flag, username) = login()
                while not login_flag:
                    print('Wrong username, password')
                    if input("Try again?(y/n): ").lower() == 'n':
                        break 
                    (login_flag, username) = login()
                else:               
                    while True:
                        input_order = input(f'\n------------------------ Welcome {username} ----------------------'
                                            f'\n\n'
                                            f'Information ----> enter number 1\n'
                                            f'Change username and phone number ----> enter number 2\n'
                                            f'Change password ----> enter number 3\n'
                                            f'Logout ----> enter number 4\n'
                                            f'Bank accounts ----> enter number 5\n'
                                            f'Cinema ----> enter number 6\n'
                                            f'please insert your choice : ')
                        match input_order:
                            case '1':
                                print('---------------------------- Information -------------------------------')
                                print(user)
                            case '2':
                                print('------------------------- Change information ---------------------------')
                                try:
                                    new_username = input('new username (if you want update it): ')
                                    new_phone_number = input('new phone_number (if you want update it): ')
                                    if new_username == '':
                                        new_username = user.username
                                    if new_phone_number == '':
                                        new_phone_number = user.phone_number
                                    user.change_info(new_username, new_phone_number)
                                    # if user is not str: ##??
                                    print('\n--- your account is updated successfully ---')
                                except Exception as e:
                                    print(str(e))
                            case '3':
                                print('------------------------- Change Password ---------------------------')
                                try:
                                    old_password = pwinput.pwinput('old_password : ')
                                    new_password = pwinput.pwinput('new_password : ')
                                    confirm_new_password = pwinput.pwinput('confirm_new_password : ')
                                    user.change_password(old_password, new_password,
                                                                confirm_new_password)
                                    print('--- your password updated successfully ---')
                                except Exception as e:
                                    print(str(e))
                            case '4':
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
