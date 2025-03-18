import json
import csv
from collections import defaultdict

# Step 1: Read JSON data
with open("sales.json", "r") as file:
    content = json.load(file)

# Step 2: Create a flat list structure for CSV output
flat_data = []

# Customer totals for sorting later
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

# Process each order
for order in content["orders"]:
    order_id = order.get("order_id")
    customer_name = order["customer"].get("name")
    shipping_address = order.get("shipping_address")
    country_code = shipping_address.split(' ')[-1]
    
    # Calculate order total to determine if discount applies
    order_total = sum(item["price"] * item["quantity"] for item in order["items"])
    discount_rate = 0.1 if order_total > 100 else 0
    
    # Process each item in the order
    for item in order["items"]:
        product_name = item.get("name")
        price = item.get("price")
        quantity = item.get("quantity")
        
        # Calculate values
        total_value = price * quantity
        discount = total_value * discount_rate
        shipping_cost = 5 * quantity
        final_total = total_value - discount + shipping_cost
        
        # Add to customer's total spending
        customer_totals[customer_name] += final_total

        # # Add to customer's total spending
        # if customer_name in customer_totals:
        #     customer_totals[customer_name] += final_total
        # else:
        #     customer_totals[customer_name] = final_total

        # When "John Doe" doesn't exist yet, you'll get a KeyError. The if-else statement is there to handle this situation
        # if the key exists, update its value; if not, create it with an initial value.
        
        # Create a flat record for this item
        flat_record = {
            "Order ID": order_id,
            "Customer Name": customer_name,
            "Product Name": product_name,
            "Product Price": price,
            "Quantity Purchased": quantity,
            "Total Value": total_value,
            "Discount": discount,
            "Shipping Cost": shipping_cost,
            "Final Total": final_total,
            "Shipping Address": shipping_address,
            "Country Code": country_code
        }
        
        # Add to flat data list
        flat_data.append(flat_record)

# Sort data by customer total spending
flat_data.sort(key=lambda x: customer_totals[x["Customer Name"]], reverse=True)

# Write data to CSV
csv_columns = [
    "Order ID", "Customer Name", "Product Name", "Product Price", 
    "Quantity Purchased", "Total Value", "Discount", "Shipping Cost", 
    "Final Total", "Shipping Address", "Country Code"
]

with open("order_data.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(flat_data)

# Print summary for verification
for record in flat_data:
    print(f"Order: {record['Order ID']}, Customer: {record['Customer Name']}, " +
          f"Product: {record['Product Name']}, Final Total: ${record['Final Total']:.2f}")

print("\nCustomer Totals (for sorting):")
for customer, total in sorted(customer_totals.items(), key=lambda x: x[1], reverse=True):
    print(f"{customer}: ${total:.2f}")