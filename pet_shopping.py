# Creating a shopping cart without using classes or functions

# Initialize an empty dictionary to represent the shopping cart
cart = {}

# Add items to the cart
cart["Dog Food"] = 20
cart["Cat Toy"] = 5
cart["Fish Tank"] = 35

# View items in the cart
print("Items in your cart:")
for item, price in cart.items():
    print(f"{item}: ${price}")

# Remove an item from the cart
del cart["Cat Toy"]

# View items after removal
print("\nItems in your cart after removal:")
for item, price in cart.items():
    print(f"{item}: ${price}")

# Calculate total cost
total_cost = sum(cart.values())
print(f"\nTotal Cost: ${total_cost}")