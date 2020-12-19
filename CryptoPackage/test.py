import tkinter as tk
from tkinter import *
from tkinter import messagebox

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def center_window(w=300, h=200):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root = Tk()
root.title('Mono-Alphabet Cipher Algorithm')
center_window(600, 300)
root.option_add("*Font", "calibri")


Label(root, padx=15, pady=10, text='Enter Message:').grid(row=1, column=0, sticky=W)
Label(root, padx=15, pady=10, text='Enter Key:', ).grid(row=2, column=0, sticky=W)
Label(root, padx=15, pady=10, text='Output:').grid(row=3, column=0, sticky=W)

plaintext = Entry(root, width=40, relief=FLAT)
plaintext.grid(row=1, column=1, ipady=2)

cipher = Entry(root, width=40, relief=FLAT)
cipher.grid(row=2, column=1, ipady=2)

output_text = Entry(root, width=40, relief=FLAT)
output_text.grid(row=3, column=1, ipady=2)


def encrypt():
    myMessage = plaintext.get()
    myMessage = str(myMessage)
    myMessage = myMessage

    myKey = cipher.get()
    myKey = str(myKey)
    myKey = myKey

    outputtext = ''
    charsA = LETTERS
    charsB = myKey

    for symbol in myMessage:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                outputtext += charsB[symIndex].upper()
            else:
                outputtext += charsB[symIndex].lower()
        else:
            outputtext += symbol
    output_text.insert(0, outputtext)
    return outputtext

def decrypt():
    myMessage = plaintext.get()
    myMessage = str(myMessage)
    myMessage = myMessage

    myKey = cipher.get()
    myKey = str(myKey)
    myKey = myKey.upper()

    outputtext = ''
    charsA = LETTERS
    charsB = myKey


    charsA, charsB = charsB, charsA
    for symbol in myMessage:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                outputtext += charsB[symIndex].upper()
            else:
                outputtext += charsB[symIndex].lower()
        else:
            outputtext += symbol


    output_text.insert(0, outputtext)
    return outputtext

def guide():
    lines = ['[Encryption]',
             'Step 1. Enter message or plaintext into the Enter Message Input Box',
             'Step 2. Enter your desired key number into the Enter Key Input Box. Enter any number from 1 to 26.',
             'Step 3. Press the Encrypt Button to generate the Encrypted text into the Output Box.',
              '======================================',
             '[Decryption]',
             'Step 1. Enter Encrypted Message into the Enter Message Input Box',
             'Step 2. Enter key number into the Enter Key Input Box.',
             'Step 3. Enter the Decrypt Button to generate the Decrypted text into the Output Box.']

    tk.messagebox.showinfo("How To Use Shift Cipher Tool?", "\n".join(lines))

# button
encrypt_button =Button(root, padx=10, pady=5, bg="red", borderwidth=4, text='Encrypt', relief=FLAT, command=lambda: encrypt())
decrypt_button = Button(root, padx=10, pady=5, text='Decrypt', borderwidth=4, bg="blue", relief=FLAT, command=lambda: decrypt())
guide_button = Button(root, padx=10, pady=5, text='Guide', borderwidth=4, bg="green", relief=FLAT, command=guide)

# grid
encrypt_button.grid(row=5, column=0, padx=15, pady=15, sticky=W)
decrypt_button.grid(row=5, column=1, pady=15, sticky=W)
guide_button.grid(row=5, column=1, padx=150, pady=15, sticky=W)


root.mainloop()
