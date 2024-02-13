# Module3Lab.py
"""Coffee Shop Simulator"""

print("Hello! Welcome to Rydahn's Coffee 'n' Books Café!")

# Deffine prices
price_coffee = 5
price_muffin = 4

# Ask user for quantity of items
value1 = int(input('Number of coffees bought: '))
value2 = int(input('Number of muffins bought: '))

# Multiply number of coffee times price of coffee and vice versa
subtotal_coffee = value1 * price_coffee
subtotal_muffin = value2 * price_muffin

# Add subtotals before tax
subtotal = subtotal_coffee + subtotal_muffin

# Add tax
tax = 0.06
total_tax = subtotal * tax
total = subtotal + total_tax

# Display total
print("Rydahn's Coffee 'n' Books Café Receipt")
print(str(value1) + " coffees at $5 each: $" + str(subtotal_coffee))
print(str(value2) +  " muffins at $4 each: $" + str(subtotal_muffin))
print("6% tax: $" + str(total_tax))
print("Total: $" + str(total))
