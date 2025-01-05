import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import string

# Initialize GUI
gui = Tk()
gui.title('Password Generator')
gui.geometry('400x400')
gui.resizable(0, 0)

# Variables
string_pass = StringVar()
password_var = StringVar()
password_history = []  # To store password history
is_dark_mode = False  # To track the theme

# Toggle Dark Mode
def toggle_theme():
    global is_dark_mode
    if not is_dark_mode:
        gui.config(bg="black")
        label_length.config(bg="black", fg="white")
        label_password.config(bg="black", fg="white")
        password_entry.config(bg="gray", fg="black", insertbackground="white")
        toggle_button.config(bg="gray", fg="white")
        dark_mode_button.config(text="Light Mode", bg="gray", fg="white")
        generate_button.config(bg="gray", fg="white")
        history_button.config(bg="gray", fg="white")
        exit_button.config(bg="gray", fg="white")
        is_dark_mode = True
    else:
        gui.config(bg="white")
        label_length.config(bg="white", fg="black")
        label_password.config(bg="white", fg="black")
        password_entry.config(bg="white", fg="black", insertbackground="black")
        toggle_button.config(bg="white", fg="black")
        dark_mode_button.config(text="Dark Mode", bg="white", fg="black")
        generate_button.config(bg="white", fg="black")
        history_button.config(bg="white", fg="black")
        exit_button.config(bg="white", fg="black")
        is_dark_mode = False

# Password Visibility Toggle
def toggle_visibility():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        toggle_button.config(text="Hide")
    else:
        password_entry.config(show="*")
        toggle_button.config(text="Show")

# Generate Password
def process():
    try:
        length = int(string_pass.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for password length.")
        return
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    num = list(string.digits)
    special = list("@#$%&*")
    all = lower + upper + num + special
    if length > len(all):
        messagebox.showerror("Error", "Length exceeds the pool of unique characters.")
        return
    password = "".join(random.choices(all, k=length))
    password_var.set(password)
    password_history.append(password)  # Add password to history
    pyperclip.copy(password)
    messagebox.showinfo('Result', 'Password Copied to Clipboard!')

# Show Password History
def show_history():
    if password_history:
        history_window = Toplevel(gui)
        history_window.title("Password History")
        history_window.geometry("300x200")
        history_window.resizable(0, 0)
        history_window.config(bg="black" if is_dark_mode else "white")
        Label(history_window, text="Password History:", bg="black" if is_dark_mode else "white",
              fg="white" if is_dark_mode else "black").pack(pady=10)    
        for pwd in password_history:
            Label(history_window, text=pwd, bg="black" if is_dark_mode else "white",
                  fg="white" if is_dark_mode else "black").pack(anchor="w", padx=20)
        Button(history_window, text="Close", command=history_window.destroy,
               bg="gray" if is_dark_mode else "white",
               fg="white" if is_dark_mode else "black").pack(pady=10)
    else:
        messagebox.showinfo("History", "No passwords generated yet.")

# UI Elements
label_length = Label(text="Password Length:")
label_length.pack(pady=10)
Entry(textvariable=string_pass).pack()
label_password = Label(text="Generated Password:")
label_password.pack(pady=10)
password_entry = Entry(textvariable=password_var, state='readonly', show="*")
password_entry.pack()

# Buttons
toggle_button = Button(text="Show", command=toggle_visibility)
toggle_button.pack(pady=5)
generate_button = Button(text="Generate", command=process)
generate_button.pack(pady=10)
history_button = Button(text="View History", command=show_history)
history_button.pack(pady=5)
dark_mode_button = Button(text="Dark Mode", command=toggle_theme)
dark_mode_button.pack(pady=5)
exit_button = Button(text="Exit", command=gui.quit)
exit_button.pack(pady=10)
gui.mainloop()


