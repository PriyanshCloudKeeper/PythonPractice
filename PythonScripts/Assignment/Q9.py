# Write a Python program to simulate a basic version control system for a directory of files. The script should:
# Accept a directory path as input and store versions of files whenever changes are made.
# Each time a file is modified, the script should create a new version and save it in a separate folder (e.g., ./versions).
# Keep track of file versions by naming them with a version number or timestamp (e.g., file_v1.txt, file_v2.txt).
# When a file is restored to a previous version, it should be copied from the version folder back to the original directory.
# Bonus:
# Implement the ability to compare file versions and show differences (similar to diff).
# Add an option to automatically clean up old versions, keeping only the last n versions of each file.

# AI Generated, Working Under Progress For Self Version.....

import os
import shutil
import time
import difflib
import argparse
from datetime import datetime

def create_version_folder():
    """Create a versions folder if it doesn't exist."""
    if not os.path.exists("./versions"):
        os.makedirs("./versions")
        print("Created versions folder.")

def get_file_versions(file_name):
    """Get all versions of a file."""
    versions = []
    version_folder = "./versions"
    
    if not os.path.exists(version_folder):
        return versions
    
    for file in os.listdir(version_folder):
        if file.startswith(os.path.basename(file_name) + "_v"):
            versions.append(file)
    
    versions.sort()  # Sort by version number
    return versions

def get_next_version_number(file_name):
    """Get the next version number for a file."""
    versions = get_file_versions(file_name)
    
    if not versions:
        return 1
    
    # Extract version number from last file
    last_version = versions[-1]
    version_str = last_version.split("_v")[1].split(".")[0]
    return int(version_str) + 1

def save_version(file_path):
    """Save a new version of a file."""
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        return
    
    create_version_folder()
    
    file_name = os.path.basename(file_path)
    version_num = get_next_version_number(file_path)
    
    # Create new version name (e.g., file_v1.txt)
    file_name_parts = file_name.split(".")
    if len(file_name_parts) > 1:
        extension = file_name_parts[-1]
        name_without_ext = ".".join(file_name_parts[:-1])
        version_name = f"{name_without_ext}_v{version_num}.{extension}"
    else:
        version_name = f"{file_name}_v{version_num}"
    
    version_path = os.path.join("./versions", version_name)
    
    # Copy the file to versions folder
    shutil.copy2(file_path, version_path)
    print(f"Saved version {version_num} of {file_name}")

def restore_version(file_path, version_num):
    """Restore a file to a previous version."""
    file_name = os.path.basename(file_path)
    
    # Get the version file name
    file_name_parts = file_name.split(".")
    if len(file_name_parts) > 1:
        extension = file_name_parts[-1]
        name_without_ext = ".".join(file_name_parts[:-1])
        version_name = f"{name_without_ext}_v{version_num}.{extension}"
    else:
        version_name = f"{file_name}_v{version_num}"
    
    version_path = os.path.join("./versions", version_name)
    
    if not os.path.exists(version_path):
        print(f"Error: Version {version_num} of {file_name} does not exist.")
        return
    
    # Make a backup of the current file before restoring
    save_version(file_path)
    
    # Copy the version file back to the original location
    shutil.copy2(version_path, file_path)
    print(f"Restored {file_name} to version {version_num}")

def monitor_directory(directory_path):
    """Monitor a directory for changes and save versions."""
    print(f"Monitoring directory: {directory_path}")
    print("Press Ctrl+C to stop monitoring.")
    
    # Track file modification times
    file_mtimes = {}
    
    try:
        while True:
            for root, _, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    
                    # Skip version control files
                    if "./versions" in file_path:
                        continue
                    
                    # Check if file has been modified
                    current_mtime = os.path.getmtime(file_path)
                    if file_path in file_mtimes and current_mtime > file_mtimes[file_path]:
                        print(f"File {file} has been modified.")
                        save_version(file_path)
                    
                    # Update modification time
                    file_mtimes[file_path] = current_mtime
            
            time.sleep(1)  # Check every second
    except KeyboardInterrupt:
        print("Monitoring stopped.")

def compare_versions(file_path, version1, version2):
    """Compare two versions of a file and show differences."""
    file_name = os.path.basename(file_path)
    
    # Get the version file names
    file_name_parts = file_name.split(".")
    if len(file_name_parts) > 1:
        extension = file_name_parts[-1]
        name_without_ext = ".".join(file_name_parts[:-1])
        version1_name = f"{name_without_ext}_v{version1}.{extension}"
        version2_name = f"{name_without_ext}_v{version2}.{extension}"
    else:
        version1_name = f"{file_name}_v{version1}"
        version2_name = f"{file_name}_v{version2}"
    
    version1_path = os.path.join("./versions", version1_name)
    version2_path = os.path.join("./versions", version2_name)
    
    if not os.path.exists(version1_path) or not os.path.exists(version2_path):
        print(f"Error: One or both versions do not exist.")
        return
    
    # Read file contents
    with open(version1_path, 'r') as f1, open(version2_path, 'r') as f2:
        v1_lines = f1.readlines()
        v2_lines = f2.readlines()
    
    # Compare files
    diff = difflib.unified_diff(
        v1_lines, v2_lines,
        fromfile=f'version {version1}',
        tofile=f'version {version2}'
    )
    
    # Print differences
    print(f"Differences between version {version1} and version {version2} of {file_name}:")
    diff_output = list(diff)
    if diff_output:
        for line in diff_output:
            print(line, end='')
    else:
        print("No differences found.")

def clean_up_versions(file_path, keep_n):
    """Keep only the last n versions of a file."""
    versions = get_file_versions(file_path)
    
    if len(versions) <= keep_n:
        print(f"Only {len(versions)} versions exist. No cleanup needed.")
        return
    
    # Delete older versions
    versions_to_delete = versions[:-keep_n]
    for version in versions_to_delete:
        os.remove(os.path.join("./versions", version))
        print(f"Deleted old version: {version}")

def list_versions(file_path):
    """List all versions of a file."""
    versions = get_file_versions(file_path)
    
    if not versions:
        print(f"No versions found for {os.path.basename(file_path)}.")
        return
    
    print(f"Versions of {os.path.basename(file_path)}:")
    for version in versions:
        version_path = os.path.join("./versions", version)
        timestamp = datetime.fromtimestamp(os.path.getmtime(version_path))
        print(f"  {version} - {timestamp}")

def main():
    parser = argparse.ArgumentParser(description="Simple Version Control System")
    parser.add_argument("action", choices=["monitor", "save", "restore", "list", "compare", "cleanup"],
                        help="Action to perform")
    parser.add_argument("--path", help="File or directory path")
    parser.add_argument("--version", type=int, help="Version number")
    parser.add_argument("--compare-with", type=int, help="Version number to compare with")
    parser.add_argument("--keep", type=int, help="Number of versions to keep")
    
    args = parser.parse_args()
    
    if args.action == "monitor":
        if not args.path:
            print("Error: Please provide a directory path to monitor.")
            return
        monitor_directory(args.path)
    
    elif args.action == "save":
        if not args.path:
            print("Error: Please provide a file path to save.")
            return
        save_version(args.path)
    
    elif args.action == "restore":
        if not args.path or not args.version:
            print("Error: Please provide a file path and version number.")
            return
        restore_version(args.path, args.version)
    
    elif args.action == "list":
        if not args.path:
            print("Error: Please provide a file path.")
            return
        list_versions(args.path)
    
    elif args.action == "compare":
        if not args.path or not args.version or not args.compare_with:
            print("Error: Please provide a file path, version number, and version to compare with.")
            return
        compare_versions(args.path, args.version, args.compare_with)
    
    elif args.action == "cleanup":
        if not args.path or not args.keep:
            print("Error: Please provide a file path and number of versions to keep.")
            return
        clean_up_versions(args.path, args.keep)

if __name__ == "__main__":
    main()