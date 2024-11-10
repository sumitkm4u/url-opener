Open Multiple HTML Files in Browser
This Python script allows you to open multiple index.html files located in separate folders in your default web browser. It’s especially useful when you have a series of HTML templates or web files organized in numbered folders and want to quickly preview them in the browser.

Prerequisites
Python 3.x installed on your system
A set of folders each containing an index.html file
How It Works
The script takes a base folder path and the number of folders you'd like to open. It then constructs the file path to index.html in each folder and opens them all in new tabs in the default web browser.

File Structure
The folders should be organized as follows:

python
Copy code
/Base Folder/
│
├── 1/
│   └── index.html
├── 2/
│   └── index.html
├── 3/
│   └── index.html
...
Usage
Download the Script: Clone this repository or download the open_multiple_html.py file.

Set the Folder Path: Update the base_folder variable in the script with the path to your base folder containing the HTML files.

Run the Script:

bash
Copy code
python open_multiple_html.py
By default, the script is set to open the first 10 folders. You can change this by modifying the folder_count variable in the script.

Example
If your HTML files are located in E:/Harsh/Web Templates/Law-firm/, the script will generate paths such as:

file:///E:/folder/Web%20Templates/Law-firm/1/index.html
file:///E:/folder/Web%20Templates/Law-firm/2/index.html
These paths will be opened in new tabs in your default browser.

Customization
Adjust Folder Count: Change the folder_count variable to the number of folders you need.
Change Base Path: Update base_folder to point to your main folder.
License
This project is licensed under the MIT License. Feel free to use, modify, and distribute.
