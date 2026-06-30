# Password Manager (Python Tkinter)

A simple desktop Password Manager application built using Python and Tkinter.

This project allows users to generate secure passwords, save website login credentials, and search previously saved credentials.

## Features

- Generate strong random passwords
- Automatically copy generated password to clipboard
- Save website, email, and password details
- Store data permanently using JSON file
- Search saved credentials by website name
- Error handling for missing files and missing records
- Simple GUI built with Tkinter

---

## Technologies Used

- Python
- Tkinter (GUI)
- JSON (Data Storage)
- Pyperclip (Clipboard Support)
- Random Module

---

## Project Structure

```text
password-manager/
│
├── main.py
├── password.json
├── logo.png
└── README.md
```

---

## How It Works

### 1. Generate Password

Click **Generate Password**

- Creates random password using:
  - Letters
  - Numbers
  - Symbols
- Automatically copies password to clipboard

### 2. Save Password

Enter:

- Website
- Email
- Password

Click **Add**

- Stores data inside `password.json`

Example:

```json
{
  "Github": {
    "email": "example@gmail.com",
    "password": "Abc@123"
  }
}
```

### 3. Search Password

Enter website name and click **Search**

- Shows saved email and password if record exists
- Shows error message if record not found

---

## What I Learned

While building this project I practiced:

- Building GUI applications with Tkinter
- Working with JSON files
- Reading and writing files
- Exception handling using:
  - try
  - except
  - else
  - finally
- Organizing code using functions
- Using external Python libraries

---

## Future Improvements

Possible improvements:

- Delete saved passwords
- Update existing passwords
- Add password encryption
- Add login authentication
- Better UI design

---
