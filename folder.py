import webbrowser
import os

# Base folder path
base_folder = "file:///E:/Harsh/Web%20Templates/Law-firm"

# Specify the number of folders you want to open
# For example, folders named as '1', '2', ..., '10'
folder_count = 19

# Loop through folder numbers and open 'index.html' in each
for i in range(1, folder_count + 1):
    # Construct the file path for each index.html
    file_path = os.path.join(base_folder, str(i), "index.html")
    # Open the file path in the default web browser
    webbrowser.open(file_path)

print(f"Opened {folder_count} folders in the browser.")
