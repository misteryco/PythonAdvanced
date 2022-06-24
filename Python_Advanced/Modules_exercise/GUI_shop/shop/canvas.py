import tkinter
from tkinter import *

from authentication import *


def clean_screen():
    for el in tk.pack_slaves():
        el.destroy()
    for el in tk.grid_slaves():
        el.destroy()


def login_screen():
    clean_screen()

    # username label and field
    tkinter.Label(tk, text="Username").pack(ipadx=10, ipady=5, fill='x')
    username = tkinter.Entry(tk)
    username.pack(ipadx=10, ipady=5, fill='x')

    # password label and field
    tkinter.Label(tk, text="Password").pack(ipadx=10, ipady=5, fill='x')
    password = tkinter.Entry(tk)
    password.pack(ipadx=10, ipady=5, fill='x')

    # login button with username and password .get()
    login_button = tkinter.Button(tk, text="Login",
                                  command=lambda: products_screen() if(login_check(username.get(),
                                                                                   password.get())) else None)
    login_button.pack(ipadx=10, ipady=5, fill='x')


def register_screen():
    clean_screen()
    # so in register screen is possible to add new data field in the future.
    # to improve usability we define data fields with loop. To add additional data fields add, another item in
    # [register_fields]
    register_fields = ["Username", "Password", "Name", "Family"]
    fields = []

    for field in register_fields:
        tkinter.Label(tk, text=field).pack(ipadx=10, ipady=5, fill='x')
        this_field = tkinter.Entry(tk)
        this_field.pack(ipadx=10, ipady=5, fill='x')
        fields.append(this_field)

    login_button = tkinter.Button(tk, text="Register", command=lambda: user_registration(
        [[register_fields[idx], fields[idx].get()] for idx in range(len(register_fields))]))
    login_button.pack(ipadx=10, ipady=5, fill='x')
    back_button = tkinter.Button(tk, text=" < - back to start screen", bg="green", command=login_screen)
    back_button.pack(ipadx=10, ipady=5, fill='x')


def create_app():
    tk = Tk()
    tk.geometry("500x300")
    tk.title("GUI Product Shop - IMN")
    return tk


def start_screen():
    register = tkinter.Button(tk, text="Register", bg="yellow", command=register_screen)
    register.pack(ipadx=10, ipady=10, fill='x')
    login = tkinter.Button(tk, text="Login", bg="green", command=login_screen)
    login.pack(ipadx=10, ipady=10, fill='x')
    # register.grid(row=0, column=0)


def products_screen():
    clean_screen()



tk = create_app()
start_screen()

