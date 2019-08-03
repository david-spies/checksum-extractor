<b>SHA-256 Hash Extractor</b>

Written in python and utilizing Tkinter for the GUI, the SHA-256 Hash Extractor provides an easy and seamless way to extract the hash from .exe and .iso files.
The hash generated can then be compared to the SHA-256 hash provided by software companies to ensure a legitimate program has been downloaded.


<b>Prerequisites</b>

The SHA-256 Hash Extractor.exe file should run on most Windows machines with very few dependancies. 
*Note - this program has not been tested outside of the Windows environment.


<b>Installing</b>

Download the SHA-256_Hash_Extractor.exe file and execute.

Click on 'Get file'.

Explorer window will populate.

Select file type from drop down menu i.e. (text files", ".txt"), ("python files", ".py"), ("iso files", ".iso"), ("exe files", ".exe")

Navigate to the directory where your file is located.

Highlight the selected file.

Click on 'Open' to process - (2GB and larger files may take 30 seconds - 1 minute to process)

Example: latest kali release (.iso file) took 35 seconds to retrieve the hash.

Smaller files such as the latest Git for Windows release took less than 5 seconds to retrieve the hash.

The SHA-256 hash will populate on the GUI screen when retrieved.

A save as window will populate with an option to name and save the hash retrieved to a text file.

Currently working on additional automation within the code to incude a progress bar and built-in hash comparison.

Built with python and Tkinter GUI library.

Executable compiled with pyinstaller.


Authors

    David Spies
