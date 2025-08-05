import os

# Specify the directory path
directory_path = '/2024 capture'

# Get the list of files and directories
entries = os.listdir(directory_path)

# Print the list
for entry in entries:
    print(entry)
