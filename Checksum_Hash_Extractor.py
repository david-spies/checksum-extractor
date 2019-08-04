import tkinter as tk
from tkinter import *
from tkinter import filedialog
import hashlib


def open_file():
    result = filedialog.askopenfilename(initialdir="/", title="select file", filetypes=(
    ("text files", ".txt"), ("python files", ".py"), ("iso files", ".iso"), ("exe files", ".exe")))
    hasher = hashlib.sha256()
    with open(result, 'rb') as check_sum:
        content = check_sum.read()
        hasher.update(content)
    print(hasher.hexdigest())

    textbox = Label(root, text=(hasher.hexdigest()), font=('arial', 10), bd=4, relief=SUNKEN, anchor=CENTER)
    textbox.pack(side=TOP, fill=X)

    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(hasher.hexdigest())
    f.write(text2save)
    f.close()


def get_file():
    result = filedialog.askopenfilename(initialdir="/", title="select file", filetypes=(
    ("text files", ".txt"), ("python files", ".py"), ("iso files", ".iso"), ("exe files", ".exe")))
    hasher = hashlib.sha512()
    with open(result, 'rb') as check_sum:
        content = check_sum.read()
        hasher.update(content)
    print(hasher.hexdigest())

    textbox = Label(root, text=(hasher.hexdigest()), font=('arial', 10), bd=4, relief=SUNKEN, anchor=CENTER)
    textbox.pack(side=TOP, fill=X)

    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(hasher.hexdigest())
    f.write(text2save)
    f.close()


root = tk.Tk()


button = Button(root, text="Get SHA-256", fg="green", command=open_file)
button.pack()

button = Button(root, text="Get SHA-512", fg="green", command=get_file)
button.pack()

Label(root, text="Checksum SHA-256 & SHA-512", fg="blue", bg="#dedcdc").pack()
root.title('Checksum Hash Extractor')
root.configure(background='#dedcdc')
root.geometry("900x180")

shaFrame = tk.Frame(root)
shaFrame.pack()

tk.Label(shaFrame, text="Locate & open file to process", relief=SUNKEN).pack()

status = Label(root, text='Checksum Hash Extractor by: David Spies', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
