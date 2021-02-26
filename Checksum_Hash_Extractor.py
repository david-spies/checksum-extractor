import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Progressbar
import hashlib
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width=900, height=360, bg="#dedcdc")
canvas.grid(columnspan=3, rowspan=6)

# instructions
instructions = tk.Label(root, text="Select a file on your computer to extract the hash", relief=SUNKEN, font="arial")
instructions.grid(columnspan=5, rowspan=2, padx=4, pady=4)

# logo
logo = Image.open('logo.png')
# resize image
resized = logo.resize((600, 160), Image.ANTIALIAS)

logo = ImageTk.PhotoImage(resized)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=1, padx=4, pady=4)


def open_file():
    result = filedialog.askopenfilename(initialdir="/", title="select file", filetypes=(
        ("executables", "*.exe"), ("All files", "*.*")))
    hasher = hashlib.sha256()
    with open(result, 'rb') as check_sum:
        content = check_sum.read()
        hasher.update(content)
    print(hasher.hexdigest())

    textbox = Label(root, text=(hasher.hexdigest()), font=('arial', 10), bd=6, relief=SUNKEN, anchor=CENTER)
    textbox.grid(column=1, row=2)

    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(hasher.hexdigest())
    f.write(text2save)

    messagebox.showinfo("File Compare", "File Compare processing...")

    progress = Progressbar(root, length=200, mode="determinate", maximum=1, value=1)

    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100

    progress.grid(column=1, row=5, padx=10, pady=10)

    if str(hasher.hexdigest()) == open('compare.txt').read():
        textbox = Label(root, text='  Success  ', font=('arial', 10), fg="green", bd=6, relief=RAISED,
                        anchor=CENTER)
        textbox.grid(column=1, row=4)
        print('Success')
    else:
        textbox = Label(root, text='  Fail  ', font=('arial', 10), fg="white", bg="red", bd=6, relief=RAISED,
                        anchor=CENTER)
        textbox.grid(column=1, row=4)
        print('Fail')
        f.close()


def get_file():
    result = filedialog.askopenfilename(initialdir="/", title="select file", filetypes=(
        ("executables", "*.exe"), ("All files", "*.*")))
    hasher = hashlib.sha512()
    with open(result, 'rb') as check_sum:
        content = check_sum.read()
        hasher.update(content)
    print(hasher.hexdigest())

    textbox = Label(root, text=(hasher.hexdigest()), font=('arial', 10), bd=6, relief=SUNKEN, anchor=CENTER)
    textbox.grid(column=1, row=2)

    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(hasher.hexdigest())
    f.write(text2save)

    messagebox.showinfo("File Compare", "File Compare processing...")

    progress = Progressbar(root, length=200, mode="determinate", maximum=1, value=1)

    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100

    progress.grid(column=1, row=5, padx=10, pady=10)

    if str(hasher.hexdigest()) == open('compare.txt').read():
        textbox = Label(root, text='  Success  ', font=('arial', 10), fg="green", bd=6, relief=RAISED, anchor=CENTER)
        textbox.grid(column=1, row=4)
        print('Success')
    else:
        textbox = Label(root, text='  Fail  ', font=('arial', 10), fg="white", bg="red", bd=6, relief=RAISED,
                        anchor=CENTER)
        textbox.grid(column=1, row=4)
        print('Fail')
        f.close()


def fetch_file():
    result = filedialog.askopenfilename(initialdir="/", title="select file", filetypes=(
        ("executables", "*.exe"), ("All files", "*.*")))
    hasher = hashlib.md5()
    with open(result, 'rb') as check_sum:
        content = check_sum.read()
        hasher.update(content)
    print(hasher.hexdigest())

    textbox = Label(root, text=(hasher.hexdigest()), font=('arial', 10), bd=6, relief=SUNKEN, anchor=CENTER)
    textbox.grid(column=1, row=2)

    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(hasher.hexdigest())
    f.write(text2save)

    messagebox.showinfo("File Compare", "File Compare processing...")

    progress = Progressbar(root, length=200, mode="determinate", maximum=1, value=1)

    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100

    progress.grid(column=1, row=5, padx=10, pady=10)

    if str(hasher.hexdigest()) == open('compare.txt').read():
        textbox = Label(root, text='  Success  ', font=('arial', 10), fg="green", bd=6, relief=RAISED, anchor=CENTER)
        textbox.grid(column=1, row=4)
        print('Success')
    else:
        textbox = Label(root, text='  Fail  ', font=('arial', 10), fg="white", bg="red", bd=6, relief=RAISED,
                        anchor=CENTER)
        textbox.grid(column=1, row=4)
        print('Fail')
        f.close()


Label(root, padx=4, pady=4)

# browse buttons

frame = LabelFrame(root, text="", relief=RAISED, padx=40, pady=10, bg='#bbbbbb')
frame.grid(column=1, row=3, padx=12, pady=10)

button1 = tk.Button(frame, text="Get SHA-256", fg="green", command=open_file)
button1.config()
button1.grid(column=0, row=3, padx=5, pady=5)

button2 = tk.Button(frame, text="Get SHA-512", fg="green", command=get_file)
button2.config()
button2.grid(column=1, row=3, padx=5, pady=5)

button3 = tk.Button(frame, text="Get MD5 Hash", fg="green", command=fetch_file)
button3.config()
button3.grid(column=2, row=3)

Label(root, text="Checksum SHA-256, SHA-512, & MD5", fg="blue", bg="#dedcdc").grid(column=1, row=0, padx=4, pady=4)

root.title('Checksum Hash Extractor')
root.configure(background='#dedcdc')

status = Label(root, text='Checksum Hash Extractor by: David Spies', bd=1, relief=SUNKEN, anchor=W)
status.grid(column=1, rowspan=4, padx=8, pady=8)

root.mainloop()
