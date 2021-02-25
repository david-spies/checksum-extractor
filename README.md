## Checksum Hash Extractor

Written in python and utilizing Tkinter for the GUI, the Checksum Hash Extractor provides an easy and seamless way to extract the hash from .exe, .msi, and .iso files.
The hash extracted can then be compared to the hash provided by software developer's to verify a legitimate signature match.


## Prerequisites

The Checksum Hash Extractor code should run on most Windows machines with very few dependencies. 
*Note - this program has not been tested outside the Windows environment.


## Installing / Running

* Download or Clone.
* Run code in your favorite IDE.
* Click on 'Get SHA-256', 'Get SHA-512', or Get MD5 Hash.
* Explorer window will populate.
* Navigate to the directory where your file is located. 
* Highlight the selected file ("msi file", ".msi"), ("iso file", ".iso"), ("exe files", ".exe")
* Click on 'Open' to process
* The hexadecimal hash extracted will display on the GUI when retrieved.

    - (2GB and larger files may take 30 seconds - 1 minute to process)
    - Example: latest kali release (.iso file) took 35 seconds to retrieve the hash
    - Smaller files such as the latest Git for Windows release took less than 5 seconds to retrieve the hash.

* A save as window will populate with an option to name and save the hash retrieved to a text file.
  - Example "extracted.txt"

Be sure to save the hash retrieved to the same directory as the text file containing the hash copied
from the developer website. The auto-comparison function will run and look for the hash in compare.txt

    This text file must be named "compare.txt"

* A window prompt will display "File Compare Processing"
* Click "OK"

If the Hash extracted matches to the hash copied from the developer's website, "Success"
will be displayed.

If the hash extracted does NOT match the hash copied from the developer's website, "Fail" will be displayed

## Source Modules & Packages

* import tkinter as tk
* from tkinter import *
* from tkinter import filedialog
* from tkinter import messagebox
* from tkinter.ttk import Progressbar
* import hashlib
* from PIL import Image, ImageTk

## Dependencies

* Python 3.8

Built with python and Tkinter GUI library.


Authors

    David Spies
