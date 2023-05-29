#! /usr/bin/python3

import click
from user import User ,UserRole
from extra import get_object, delete, save
from ..bank_account.bank_account import BankAccount
from ..cinema.cinema import ticket

@click.group
def mycommands():
    pass

@click.command()
@click.option('-u', '--username', prompt='Username', help='Define a username for new staff.')
@click.option('-p', '--password', prompt='Password', hide_input=True, help='Define a password for new staff.')
@click.option('-b', '--birthdate', prompt='Birthdate', help='Birthdate of the new staff.')
@click.option('-P', '--phone-number', help='Enter phone number of new staff.(optional)')
def signup(username: str, password: str, birthdate: str, phone_number: str) -> None:
    """
    Sign up new staff.
    Staff have access to cinema settings.
    """
    User.create_user(username, password, birthdate, phone_number).promote_to_staff()


@click.command()
@click.argument('account_number')
def cinema_bank_account(account_number: str) -> None:
    '''
    Bank account number for depositing the cinema income.
    '''
    if BankAccount.is_serial(account_number):
        ticket.change_cinema_account(account_number)
    else:
        click.echo('Entered serial number is incorrect.')

ACCESS = {
    'D': 'Delete',
    'p': 'Promote',
    'd': 'Demote'
}

@click.command()
@click.argument('username')
@click.option('-a', '--access', type=click.Choice(ACCESS.keys()) , prompt='',help=f'{ACCESS}')
def edit_user_access(username: str, access: str):
    """
    Change user access level or delete him.
    """
    user = get_object(username)
    if user is None:
        click.echo('Username not found!')
    else:
        match access:
            case 'D':
                delete(username)
            case 'p':
                user['user_role'] = UserRole.STAFF.value
                delete(username)
                save(user)
            case 'd':
                user['user_role'] = UserRole.PUBLIC.value
                delete(username)
                save(user)
        click.echo(f'Successfully {ACCESS[access]}ed.')


mycommands.add_command(signup)
mycommands.add_command(cinema_bank_account)
mycommands.add_command(edit_user_access)

if __name__ == '__main__':
    mycommands()