# Write a Python program to automate the checking and updating of installed software packages on a Linux server. 
# The script should:
# Function to check for available updates using the system’s package manager (e.g., apt, yum). and list all available updates. - Done
# Ask user to Update all at once or provide any specific package name to update (take package index number for ease) - Done
# Install the available updates based on user input. - Done
# If any updates fail to install, log the error and send an alert (e.g., console log). 
# Optionally, schedule the script to run at a certain cron. - Done

import subprocess # allows us to execute external commands.

import time
import schedule

def check_updates():

    # Function to update the system
    def update_fix():
        print("\nChecking and fixing broken package installations...\n")
        subprocess.run(["sudo", "dpkg", "--configure", "-a"], capture_output=True, text=True)
        print("Update in progress....")

        try:
            sys_update = subprocess.run(["sudo", "apt-get", "update"], capture_output=True, timeout=120)
            if sys_update.returncode !=0:
                print("\nError updating system")
                print(sys_update.stderr.decode())
                return
            else:
                print("System Updated")
        except subprocess.TimeoutExpired:
            print("Timeout Occured")

    # Get a list of all packages that can be upgraded
    try:
        result = subprocess.run(["apt-get", "list", "--upgradable"], capture_output=True, timeout=60)
    
        if (result.returncode!=0):
            print("Error checking for updates")
        else:
            output = result.stdout.decode()

            # print(output) raw output
            # print(output.split('\n')) make a list of the output by splliting one the basis of new line
            # print((output.split('\n'))[1:]) # list starts from 2nd element

            # making a list of all packages that can be upgraded
            packages = []
            for i in output.split('\n')[1:]:
                if i.strip():
                    pkg_info = (i.split('/'))[0]
                    print(f"{len(packages)+1}.{pkg_info}")
                    packages.append(pkg_info)

    except subprocess.TimeoutExpired:
        print("There is a timeout")

    ask = input("\nWould you like to update all or specific packages?: All(ALL) or Specific Packages(SP)?\n")

    try:   
        match ask.lower():

            #Upgrade all packages
            case "all":

                update_fix()

                try:
                    
                    output = subprocess.run(["sudo", "apt-get", "upgrade", "-y"], capture_output=True, timeout=120)
                    if output.returncode == 0:
                        print("All packages updated successfully!")
                        print(output.stdout.decode())
                    else:
                        print("Error updating packages:")
                        print(output.stderr.decode())

                except subprocess.TimeoutExpired:
                    print("Update process timed out")

            #Update specific packages
            case "sp":

                update_fix()
                
                try:
                    try:
                        pkg_index = int(input(f"Enter the package number 1-{len(packages)}: "))-1
                        if 0 <= pkg_index < len(packages):
                            pkg_name = packages[pkg_index]
                            print("Your package is:", pkg_name)
                            output = subprocess.run(["sudo", "apt-get", "install", "--only-upgrade", pkg_name, "-y"], capture_output=True, timeout=120)
                            if output.returncode != 0:
                                print("Error upgrading package")
                                print(output.stderr.decode())
                            else:
                                print("Upgrade Successful")
                                print(output.stdout.decode())
                        else:
                            print("Invalid package number. Please choose a number between 1 and", len(packages))
                            
                    except ValueError:
                        print("Please enter a valid number")
                        
                except subprocess.TimeoutExpired:
                    print("Timeout occurred")
        
    except subprocess.TimeoutExpired:
        print("There is a timeout")
    

schedule.every().day.at("03:00").do(lambda: check_updates())

try:
    check_updates()
    while True:
        schedule.run_pending()
        time.sleep(60)

except KeyboardInterrupt:
    print("\nProcess Exited")
