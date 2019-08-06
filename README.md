<b>Checksum Hash Extractor</b>

Written in python and utilizing Tkinter for the GUI, the Checksum Hash Extractor provides an easy and seamless way to extract the hash from .exe, .iso, and .msi files.
The hash extracted can then be compared to the SHA-256, SHA-512 or MD5 hash provided by software companies to verify a legitimate signature match.


<b>Prerequisites</b>

The Checksum Hash Extractor.exe file should run on most Windows machines with very few dependancies. 
*Note - this program has not been tested outside of the Windows environment.


<b>Installing</b>

Download the Checksum_Hash_Extractor.exe file and execute.

Click on 'Get SHA-256', 'Get SHA-512', or 'Get MD5 Hash'.

Explorer window will populate.

Select file type from drop down menu i.e. (text files", ".txt"), ("python files", ".py"), ("iso files", ".iso"), ("exe files", ".exe"), ("msi files", ".msi")

Navigate to the directory where your file is located.

Highlight the selected file.

Click on 'Open' to process - (2GB and larger files may take 30 seconds - 1 minute to process)

Example: latest kali release (.iso file) took 35 seconds to retrieve the hash on a core i5 

Smaller files such as the latest Git for Windows release took less than 5 seconds to retrieve the hash.

The SHA-256, SHA-512, or MD5 hash will populate on the GUI screen when retrieved.

A save as window will populate with an option to name and save the hash retrieved to a text file.

Currently working on additional automation to include a built-in hash comparison.

Built with python and Tkinter GUI library.

Executable compiled with pyinstaller.


Authors

    David Spies
