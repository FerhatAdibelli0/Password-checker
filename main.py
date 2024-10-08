from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

window = Tk()
window.title("Password GUI")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

canvas.grid(row=0, column=1)


def generate_password():
    letter = [choice(letters) for _ in range(randint(8, 10))]
    symbol = [choice(symbols) for _ in range(randint(2, 4))]
    number = [choice(numbers) for _ in range(randint(2, 4))]

    combined = letter + symbol + number
    shuffle(combined)
    hashed = ("".join(combined))
    password_input.delete(0, END)
    password_input.insert(0, hashed)
    pyperclip.copy(hashed)


def save():
    website = website_input.get().capitalize()
    passw = password_input.get()
    email = email_input.get()

    new_data = {
        website: {
            "email": email,
            "password": passw
        }
    }

    if passw == "" or website == "":
        return messagebox.showerror(message="Empty input. Please check your all inputs")
    # is_ok = messagebox.askokcancel(title="Confirmation", message="Do you really agree with your written input data ?")
    # if is_ok:
    try:
        with open("data.json", "r") as my_file:
            data = json.load(my_file)
            data.update(new_data)
    except FileNotFoundError:
        with open("data.json", "w") as my_file:
            json.dump(new_data, my_file, indent=4)
    else:
        with open("data.json", "w") as my_file:
            json.dump(data, my_file, indent=4)
    finally:
        website_input.delete(0, END)
        password_input.delete(0, END)


def search_command():
    website = website_input.get().capitalize()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title=website, message="There is no such file")
    else:
        try:
            print(data)
            popup_data = data[website]
            messagebox.showinfo(title=website, message=f"Email :{popup_data["email"]} \n Password :{popup_data["password"]}")
        except KeyError:
            messagebox.showerror(title=website, message="There is no such website stored in database")


website_label = Label(text="Website :")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username :")
email_label.grid(row=2, column=0)
password = Label(text="Password :")
password.grid(row=3, column=0)

website_input = Entry(width=21)
website_input.focus()
website_input.grid(row=1, column=1)
email_input = Entry(width=38)
email_input.insert(END, "ferhat@gmail.com")
email_input.grid(row=2, column=1, columnspan=3)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2)
add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)
search = Button(text="Search", command=search_command, width=12)
search.grid(row=1, column=2)

window.mainloop()
