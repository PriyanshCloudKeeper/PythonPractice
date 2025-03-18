# Q6. CSV to Table Visualizer
# Write a Python script which reads a csv file and Visualizes a table with proper indentations and borders. (make sure to don’t use any table making module or package)	
# Example : CSV file like this
# Name,Age,Department
# Alice,30,HR
# Bob,25,Engineering
# Charlie,35,Marketing
# Diana,28,Sales

import csv

file_path = "/home/priyansh/Learning/Python/Basics/Assignment/sampledataQ6.csv"

data = []

with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    data.append(header)
    for row in csvreader:
        data.append(row)
        
col_widths = []
# Number of Column
for i in range(len(data[0])):
    max_len = 0
    # All rows in the data
    for row in data: 
        # row[i] = element for row according to the column number
        length_element = len(str(row[i])) 
        # Get max length and append max to column length
        if length_element > max_len:
            max_len = length_element
    col_widths.append(max_len)

def print_row(row, col_widths):
    print("|", end="")
    for i, cell in enumerate(row):
        print(f" {cell:{col_widths[i]}} |", end="")
    print()

def print_line(col_widths):
    print("+", end="")
    for width in col_widths:
        print("-" * (width + 2) + "+", end="")
    print()

# Print the table
print_line(col_widths)
print_row(data[0], col_widths)
print_line(col_widths)

for row in data[1:]:
    print_row(row, col_widths)

print_line(col_widths)
