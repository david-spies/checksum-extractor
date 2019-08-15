# Checksum Hash Extractor

Written in python and utilizing Tkinter for the GUI, the Checksum Hash Extractor provides an easy and seamless way to extract the hash from .exe, .iso, or .msi files.
The hash extracted can then be compared to the SHA-256, SHA-512, or MD5 hash provided by software companies to verify a legitimate signature match.

## Prerequisites

The Checksum Hash Extractor.exe file should run on most Windows machines with very few dependencies.

## Easy Installation

* Download the Checksum_Hash_Extractor.exe file and execute.
* Click on 'Get SHA-256', 'Get SHA-512' or 'Get MD5 Hash'.
* Explorer window will populate.
* Select file type from drop down menu i.e. (text files", ".txt"), ("python files", ".py"), ("iso files", ".iso"), ("exe files", ".exe")
* Navigate to the directory where your file is located.
* Highlight the selected file.
* Click on 'Open' to process - (2GB and larger files may take 30 seconds or longer to process)
* The SHA-256 or SHA-512 hash will populate on the GUI screen when retrieved.
* A 'save as' window will populate with an option to name and save the hash retrieved to a text file.

## Installation from Source

* Download the Checksum_Hash_Extractor.py file.
* Run from terminal, IDLE, or your favorite IDE

## Source Modules & Packages

* import tkinter as tk
* from tkinter import *
* from tkinter import filedialog
* import hashlib

## Dependencies

* Python 3.7

Built with python and Tkinter GUI library.

Executable compiled with pyinstaller.


Authors

    David Spies
