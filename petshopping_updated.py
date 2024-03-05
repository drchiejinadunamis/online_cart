class ShoppingCart:
    def __init__(self):
        self.items = {}  # Store items as a dictionary with 'item_name': price

    def add_item(self, item_name, price):
        """Add an item to the cart."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Remove an item from the cart."""
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Item {item_name} not found in the cart.")

    def view_cart(self):
        """Display the items in the cart."""
        if self.items:
            print("Items in your cart:")
            for item, price in self.items.items():
                print(f"{item}: ${price}")
        else:
            print("Your cart is empty.")

    def total_cost(self):
        """Calculate the total cost of items in the cart."""
        return sum(self.items.values())

# Example usage
cart = ShoppingCart()
cart.add_item("Dog Food", 20)
cart.add_item("Cat Toy", 5)
cart.add_item("Fish Tank", 35)

# Viewing items in the cart
cart.view_cart()

# Removing an item
cart.remove_item("Cat Toy")

# Viewing items after removal
cart.view_cart()

# Displaying total cost
print(f"Total Cost: ${cart.total_cost()}")
