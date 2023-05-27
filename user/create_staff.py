#! /usr/bin/python3

import click
from user import User
import pwinput

@click.command()
def mycommands():
    pass

@click.option('-u', '--username', prompt='Username', help='Define a username for new staff.')
@click.option('-p', '--password', prompt=pwinput('Password'), help='Define a password for new staff.')
@click.option('-b', '--birthdate', prompt='Birthdate', help='Birthdate of the new staff.')
@click.option('-P', '--phone-number', help='Enter phone number of new staff.(optional)')
def signup(username: str, password: str, birthdate: str, phone_number: str) -> None:
    """
    Sign up new staff.
    Staff have access to cinema settings.
    """
    User.create_user(username, password, birthdate, phone_number).promote_to_staff()



