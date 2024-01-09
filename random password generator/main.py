import tkinter as tk
from tkinter import Label, Entry, Button, IntVar
import string
import random

def generate_password():
    length = length_var.get()
    
    if length < 8:
        result_label.config(text="Password length should be at least 8 characters.")
        return
    
    uppercase = uppercase_var.get()
    lowercase = lowercase_var.get()
    numbers = numbers_var.get()
    symbols = symbols_var.get()
    
    characters = ""
    
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    
    if not characters:
        result_label.config(text="Select at least one option (uppercase, lowercase, numbers, symbols).")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Generated Password: {password}")

# GUI setup
app = tk.Tk()
app.title("Random Password Generator")
length_var = IntVar()
length_var.set(12)  # Default password length

length_label = Label(app, text="Password Length:")
length_label.pack(pady=25)

length_entry = Entry(app, textvariable=length_var,width=30,bg='grey')
length_entry.pack(pady=25)

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(app, text="Include Uppercase", variable=uppercase_var,width=30,bg='orange',)
uppercase_checkbox.pack()

lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(app, text="Include Lowercase", variable=lowercase_var,width=30,bg='pink')
lowercase_checkbox.pack()

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(app, text="Include Numbers", variable=numbers_var,width=30,bg='green')
numbers_checkbox.pack()

symbols_var = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(app, text="Include Symbols", variable=symbols_var,width=30,bg='brown')
symbols_checkbox.pack()

generate_button = Button(app, text="Generate Password", command=generate_password,width=30,bg='skyblue')
generate_button.pack(pady=10)

result_label = Label(app, text="")
result_label.pack(pady=25)

app.mainloop()
