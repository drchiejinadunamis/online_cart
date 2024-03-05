class ShoppingCart:
    """
    A simple shopping cart class that allows adding, removing, viewing, and calculating the total cost of items.
    Items are stored as a dictionary where the key is the item name and the value is its price.
    """

    def __init__(self):
        # Initialize an empty dictionary to store cart items
        self.items = {}  # Format: 'item_name': price

    def add_item(self, item_name, price):
        """Add an item to the cart with its name and price."""
        self.items[item_name] = price  # Add or update the item in the cart

    def remove_item(self, item_name):
        """Remove an item from the cart."""
        if item_name in self.items:
            del self.items[item_name]  # Remove the item if it exists
        else:
            print(f"Item {item_name} not found in the cart.")  # Notify if the item is not in the cart

    def view_cart(self):
        """Display the items in the cart."""
        if self.items:
            print("Items in your cart:")
            for item, price in self.items.items():
                print(f"{item}: ${price}")  # Display each item and its price
        else:
            print("Your cart is empty.")  # Notify if the cart is empty

    def total_cost(self):
        """Calculate and return the total cost of items in the cart."""
        return sum(self.items.values())  # Sum up the prices of all items
