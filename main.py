from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH RECORD ------------------------------- #


def search():
    website = website_input.get()
    try:
        with open(
            "password.json",
            "r",
        ) as file:
            file_data = json.load(file)
            email = file_data[website]["email"]
            password = file_data[website]["password"]

    except KeyError:
        messagebox.showwarning(
            title="Error", message=f"No Details For {website} Exists"
        )

    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found")

    else:
        messagebox.showwarning(
            title=website, message=f"Email:  {email} \nPassword:  {password}"
        )


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = [random.choice(letters) for _ in range(random.randint(6, 8))]

    password_list += [random.choice(symbols) for _ in range(random.randint(1, 2))]

    password_list += [random.choice(numbers) for _ in range(random.randint(2, 3))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Saves data to file"""
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {"email": email, "password": password}}

    if len(email) == 0 or len(password) == 0 or len(website) == 0:
        """Check if user has not left any field Empty"""
        messagebox.showwarning(
            title="Alert", message=f"Please don't left any field empty"
        )
    else:
        # Ask for confirmation
        is_ok = messagebox.askokcancel(
            title=f"{website}",
            message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?",
        )
        if is_ok:
            try:
                with open(
                    "password.json",
                    "r",
                ) as file:
                    # Update old data with new data
                    file_data = json.load(file)

            except FileNotFoundError:
                with open(
                    "password.json",
                    "w",
                ) as file:
                    json.dump(new_data, file, indent=4)

            else:
                file_data.update(new_data)
                with open(
                    "password.json",
                    "w",
                ) as file:
                    #  Save updated data
                    json.dump(file_data, file, indent=4)

            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

# Display image
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry(input boxs)
website_input = Entry(width=16)
website_input.grid(column=1, row=1, sticky="ew", pady=5)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="ew", pady=5)
email_input.insert(0, "your_email@gmail.com")

password_input = Entry(width=16)
password_input.grid(column=1, row=3, sticky="ew", pady=5)

# Buttons
generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=2, row=3, sticky="ew", pady=5, padx=(5, 0))

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", pady=5)

search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1, sticky="ew", pady=5, padx=(5, 0))

window.mainloop()
