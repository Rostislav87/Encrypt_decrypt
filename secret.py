from tkinter import *
from tkinter import messagebox, simpledialog

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for letter in range(0, len(message)):
        if is_even(letter):
            even_letters.append(message[letter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for letter in range(0, len(message)):
        if not is_even(letter):
            odd_letters.append(message[letter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + "x"
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for letter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[letter])
        letter_list.append(even_letters[letter])
    new_message = "".join(letter_list)    
    return new_message

def get_task():
    task = simpledialog.askstring(title="Task", prompt="Do you want to encrypt or decrypt?")
    return task

def get_message():
    message = simpledialog.askstring(title="Message", prompt="Enter the secret message: ")
    return message

window = Tk()
while True:
    task = get_task()
    if task == "encrypt":
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo(title="Ciphertext of the secret message is:", message=encrypted)

    elif task == "decrypt":
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo(title="Plaintext of the secret message is:", message=decrypted)

    else:
        break

window.mainloop()
