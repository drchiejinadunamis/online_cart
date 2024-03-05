def shopping_cart_program():
    # Initialize the cart as an empty string
    cart = ""

    while True:
        # Display the welcome message and options
        print("\nWelcome to Paws n Cart!")
        print("1. Add an item to cart")
        print("2. Remove an item from cart")
        print("3. View the total cost of the cart")
        print("4. View items in the cart")
        print("5. Checkout (Exit)")

        # Get user choice
        choice = input("Enter your choice (1-5): ")

        # Add an item to the cart
        if choice == '1':
            item = input("Enter the item name and price (e.g., 'Dog Food 20'): ")
            cart += item + "; "  # Append the item to the cart string

        # Remove an item from the cart
        elif choice == '2':
            item_to_remove = input("Enter the item name to remove: ")

            if item_to_remove in cart:
                # Replace the first occurrence of the item with an empty string
                cart = cart.replace(item_to_remove + "; ", "", 1)
            else:
                print("Item not found in the cart.")

        # View the total cost of the cart
        elif choice == '3':
            total_cost = 0
            if cart:
                # Split the cart string into items and calculate the total cost
                items = cart.split("; ")
                for item in items:
                    if item:
                        total_cost += int(item.split()[-1])  # The price is the last element after splitting
            print(f"Total Cost: ${total_cost}")

        # View items in the cart
        elif choice == '4':
            print("Items in your cart:")
            if cart:
                print(cart)
            else:
                print("Your cart is empty.")

        # Checkout and exit the program
        elif choice == '5':
            print("Thank you for shopping with Paws n Cart!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Running the shopping cart program
shopping_cart_program()
