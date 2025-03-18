# Q5. Duplicate File Finder and Cleaner
# Write a Python script to find duplicate files within a specified directory and its subdirectories. The script should:
# Scan the directory for all files and calculate a checksum (e.g., sha256sum) for each file. - DOne
# Identify and list duplicate files by comparing their checksums. - Done
# Optionally, give the user the option to delete or move duplicate files. 
# Bonus:
# Allow the user to specify the minimum file size for duplication detection (e.g., only consider files larger than 1MB).
# Create a report listing the duplicate files and their checksums.

# Notes:
# Two different files could have the same name in different directories, but completely different content. Using filename-based comparison would incorrectly flag them as duplicates.
# Two files with identical content but different names are true duplicates. Using content-based checksums (SHA-256, MD5, etc.) will accurately identify these.

# print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

import hashlib
import os

# Current Working Directory
cwd = os.getcwd()

print("\nCurrent Working Directory: ", cwd, "\n")

file_path = []
name_path = {}

# Create a dictionary to group files with identical hashes
duplicate_group = {}

print("All the files: \n")

# os.walk gives 3-tuples (dirpath, dirnames, filenames). it basically generate the file names in a directory tree by walking the tree
for (dirpath, dirname, filenames) in os.walk(cwd):
    for file in filenames:
        file_path.append(os.path.join(dirpath, file))

for i in file_path:
    # store the name from the path
    name = i.split("/")[-1]

    # logic to generate the hash of a file
    try:
        with open(i, "rb") as file:
            content = file.read()
            readable_hash = hashlib.sha256(content).hexdigest()

            # Initialize with a list for each hash

            # insert hashes (and file) if not exist in hashes group
            # if hash already exists add in assicaited value list
            # if new hash make a new pair

            if readable_hash in duplicate_group:
                duplicate_group[readable_hash].append(i)
            else:
                duplicate_group[readable_hash] = [i]  # Initialize with a list containing the path

            name_path[name] = i

            print(f"{file_path.index(i)+1}. '{name}', Hash = {readable_hash}, Path: {i}")
    except Exception as e:
        print(f"Error processing file {i}: {e}")

print("\nDuplicate files found:")
for hash_value, paths in duplicate_group.items():
    if len(paths) > 1:
        print("Checksum: ", hash_value)
        for path in paths:
            print("Path: ", path)
        print("\n")