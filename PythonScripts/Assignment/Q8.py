# Q8. File Restructuring and JSON Formating

# You are given a large dataset in JSON format representing an e-commerce platform's order history, which includes orders from multiple customers. Each order has multiple items, with detailed attributes such as price, quantity, and shipping cost. Additionally, you need to extract specific information, perform calculations like the total cost, apply discounts, and sort the data based on various criteria like the total amount spent by each customer.
# The goal is to:
# Extract and restructure the data into a tabular format. - Done
# Perform calculations such as:
# Total order value (price * quantity). - Done
# Apply a discount based on the total value of an order (e.g., 10% discount if the order exceeds $100). - DOne
# Calculate shipping cost based on the number of items ordered (e.g., $5 per item). - Done
# Sort the data by the total amount spent by each customer.
# Format the output so that it can be easily saved into a CSV file.

# So Write a Python program that:
# Extract and restructure the data to create a flat list of each product purchased by each customer, containing:
# Order ID
# Customer Name
# Product Name
# Product Price
# Quantity Purchased
# Total Value (price * quantity)
# Discount (10% if the total order value > $100)
# Shipping Cost (based on the number of items ordered)
# Final Total (after discount + shipping)
# Shipping Address
# Country Code
# - Done

# Calculate:
# For each order, apply a 10% discount to the total value if the total order value is over $100.
# Calculate the total shipping cost (e.g., $5 per item).
# Compute the final total by adding the shipping cost and applying the discount (if any).
# Sort the list of orders by the final total amount spent by each customer.
# Output the data in CSV format with the following columns:
# Order ID, Customer Name, Product Name, Product Price, Quantity Purchased, Total Value, Discount, Shipping Cost, Final Total, Shipping Address, Country Code
# 

# Constraints:
# The JSON file can contain a variable number of orders.
# Each order contains a variable number of items.
# Handle missing fields or unexpected values gracefully.
# Copy this given JSON and save it as a sales.json file and take it as an input (read file)
# {'orders': [{'order_id': 'O001', 'customer': {'id': 'C001', 'name': 'John Doe', 'email': 'john@example.com'}, 'items': [{'product_id': 'P001', 'name': 'Laptop', 'price': 999.99, 'quantity': 1}, {'product_id': 'P002', 'name': 'Mouse', 'price': 25.99, 'quantity': 2}], 'shipping_address': '123 Main St, Springfield, IL'}, {'order_id': 'O002', 'customer': {'id': 'C002', 'name': 'Jane Smith', 'email': 'jane@example.com'}, 'items': [{'product_id': 'P003', 'name': 'Phone', 'price': 599.99, 'quantity': 1}], 'shipping_address': '456 Oak St, Seattle, WA'}, {'order_id': 'O003', 'customer': {'id': 'C001', 'name': 'John Doe', 'email': 'john@example.com'}, 'items': [{'product_id': 'P004', 'name': 'Headphones', 'price': 149.99, 'quantity': 1}, {'product_id': 'P005', 'name': 'Keyboard', 'price': 99.99, 'quantity': 1}], 'shipping_address': '123 Main St, Springfield, IL'}]}

import json
import csv
from collections import defaultdict

with open ("/home/priyansh/Learning/Python/Basics/Assignment/salsesQ8.json", "r") as file:
    content = json.load(file)
    # content is a dict, key: orders, value(s) = list of dictionary
    
# List for CSV
# We need a list that represents each product purchase in a separate row, which is needed for CSV output.
flat_data = []

# Use to sort later and handle missing keys, using default dict (does not throw key error)
customer_totals = defaultdict(float)

# First order processing:
# Calculate final_total = 904.99
# Execute customer_totals["John Doe"] += 904.99
# Since "John Doe" doesn't exist in customer_totals yet, defaultdict automatically creates it with default value 0.0
# Then adds 904.99 to it, so now customer_totals["John Doe"] = 904.99

# Second order processing:
# Calculate final_total = 134.99
# Execute customer_totals["John Doe"] += 134.99
# "John Doe" already exists, so it adds 134.99 to 904.99
# Now customer_totals["John Doe"] = 1039.98

# customer_totals = {}  # Regular dictionary

# First order processing:
# Calculate final_total = 904.99
# Execute:
# if "John Doe" in customer_totals:
#     customer_totals["John Doe"] += 904.99
# else:
#     customer_totals["John Doe"] = 904.99
# Since "John Doe" doesn't exist yet, it takes the else branch
# Sets customer_totals["John Doe"] = 904.99

# Second order processing:
# Calculate final_total = 134.99
# Execute the same if-else block:
# This time, "John Doe" does exist, so it takes the if branch
# Adds 134.99 to 904.99, so now customer_totals["John Doe"] = 1039.98

for order in content["orders"]:
    # order is evalue of the dict content
    # print(order, "\n")

    # OrderID in the order dict (Key = ordser_id, value = orderid)
    OrderID = order.get("order_id")

    # Customer Details Dict that is in the order dict (Key = customer, value = a dict)
    Customer_Name = order["customer"].get("name")

    # Shipping_Addr in the order dict (Key = Shipping_Addr, value = address)
    Shipping_Addr = order.get("shipping_address")
    
    # County Code extracted from Shipping Address
    Country_Code = Shipping_Addr.split(' ')[-1]

    # Calculate order total to determine if discount applies
    order_total = sum(item["price"] * item["quantity"] for item in order["items"])
    discount_rate = 0.1 if order_total > 100 else 0

    for items in order["items"]:
        # items is a dict containing info of each individual product in items
        # print(items, "\n")

        p_name = items.get("name")
        p_price = items.get("price")
        p_quantity = items.get("quantity")

        # Product_Name = list(product_details.keys())
        # Product_Price = [details.get("price") for details in product_details.values()]
        # Product_Quantity = [details.get("quantity") for details in product_details.values()]
        # Product_TotalValue = [details.get("total_value") for details in product_details.values()]

        # Calculate values
        total_value = p_price * p_quantity
        discount = total_value * discount_rate
        shipping_cost = 5 * p_quantity
        final_total = total_value - discount + shipping_cost

        customer_totals[Customer_Name] += final_total

        # # Add to customer's total spending
        # if customer_name in customer_totals:
        #     customer_totals[customer_name] += final_total
        # else:
        #     customer_totals[customer_name] = final_total

        # When "John Doe" doesn't exist yet, you'll get a KeyError. The if-else statement is there to handle this situation
        # if the key exists, update its value; if not, create it with an initial value.

        Product_Entry = {
            "Order ID": OrderID,
            "Customer Name": Customer_Name,
            "Product Name": p_name,
            "Product Price": p_price,
            "Quantity Purchased": p_quantity,
            "Total Value": total_value,
            "Discount": discount,
            "Shipping Cost": shipping_cost,
            "Final Total": final_total,
            "Shipping Address": Shipping_Addr,
            "Country Code": Country_Code
        }

        flat_data.append(Product_Entry)

        # flat_data = [
        #     {'Order ID': 'O001', 'Customer Name': 'John Doe', 'Product Name': 'Laptop', 'Product Price': 999.99, 'Quantity Purchased': 1, 'Total Value': 999.99, 'Discount': 99.99900000000001, 'Shipping Cost': 5, 'Final Total': 904.991, 'Shipping Address': '123 Main St, Springfield, IL', 'Country Code': 'IL'},
        #     {'Order ID': 'O001', 'Customer Name': 'John Doe', 'Product Name': 'Mouse', 'Product Price': 25.99, 'Quantity Purchased': 2, 'Total Value': 51.98, 'Discount': 5.198, 'Shipping Cost': 10, 'Final Total': 56.782, 'Shipping Address': '123 Main St, Springfield, IL', 'Country Code': 'IL'},
        #     {'Order ID': 'O002', 'Customer Name': 'Jane Smith', 'Product Name': 'Phone', 'Product Price': 599.99, 'Quantity Purchased': 1, 'Total Value': 599.99, 'Discount': 59.999, 'Shipping Cost': 5, 'Final Total': 544.991, 'Shipping Address': '456 Oak St, Seattle, WA', 'Country Code': 'WA'},
        #     {'Order ID': 'O003', 'Customer Name': 'John Doe', 'Product Name': 'Headphones', 'Product Price': 149.99, 'Quantity Purchased': 1, 'Total Value': 149.99, 'Discount': 14.999000000000002, 'Shipping Cost': 5, 'Final Total': 139.991, 'Shipping Address': '123 Main St, Springfield, IL', 'Country Code': 'IL'},
        #     {'Order ID': 'O003', 'Customer Name': 'John Doe', 'Product Name': 'Keyboard', 'Product Price': 99.99, 'Quantity Purchased': 1, 'Total Value': 99.99, 'Discount': 9.999, 'Shipping Cost': 5, 'Final Total': 94.991, 'Shipping Address': '123 Main St, Springfield, IL', 'Country Code': 'IL'}
        # ]


        # customer_totals = {
        #     "John Doe": 1196.755,  # Total of Laptop, Mouse + Headphones, Keyboard
        #     "Jane Smith": 544.991   # Total of Phone
        # }
        
flat_data.sort(key=lambda spend: customer_totals[spend["Customer Name"]], reverse = True)

# Write data to CSV
csv_columns = [
    "Order ID", "Customer Name", "Product Name", "Product Price", 
    "Quantity Purchased", "Total Value", "Discount", "Shipping Cost", 
    "Final Total", "Shipping Address", "Country Code"
]

with open("order_data_Q8.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(flat_data)

# Print summary for verification
for record in flat_data:
    print(f"Order: {record['Order ID']}, Customer: {record['Customer Name']}, " +
          f"Product: {record['Product Name']}, Final Total: ${record['Final Total']:.2f}")

print("\nCustomer Totals:")
for customer, total in sorted(customer_totals.items(), key=lambda x: x[1], reverse=True):
    print(f"{customer}: ${total:.2f}")



        

