# Display welcome message
print("Welcome to the Grocery Store Calculator!")

# Initialize an empty cart and subtotal
cart = []
subtotal = 0

# Set discount threshold and rate
discount_threshold = 50
discount_rate = 0.10

# Loop to continuously ask for item details until 'done' is entered
while True:
    # Get item name from user input
    name = input("Enter item name (or type 'done' to finish): ")
    
    # If user types 'done', break the loop
    if name.lower() == 'done':
        break

    # Get price and quantity from user input
    price = input("Enter price per unit: ")
    quantity = input("Enter quantity: ")

    # Check if price and quantity are valid numerical values
    if not price.replace('.', '', 1).isdigit() or not quantity.isdigit():
        print("Invalid input! Please enter numerical values for price and quantity.")
        continue

    # Convert price to float and quantity to integer
    price = float(price)
    quantity = int(quantity)

    # Check if price and quantity are positive
    if price < 0 or quantity < 0:
        print("Price and quantity must be positive numbers!")
        continue

    # Add the item to the cart and update the subtotal
    cart.append((name, price, quantity))
    subtotal += price * quantity

# Display the receipt header
print("\n--- Grocery Store Receipt ---")

# Loop through the cart and print each item's details
for item in cart:
    name, price, quantity = item
    total_price = price * quantity
    print(f"{name}   {quantity} x Rs.{price:.2f} = Rs.{total_price:.2f}")

# Print the subtotal
print("----------------------------")
print(f"Subtotal: Rs.{subtotal:.2f}")

# Check if the subtotal exceeds the discount threshold
discount_applied = 0
if subtotal > discount_threshold:
    # Apply the discount and adjust the subtotal
    discount_applied = subtotal * discount_rate
    subtotal -= discount_applied
    print(f"Discount Applied: -Rs.{discount_applied:.2f}")

# Display the final total after discount
print(f"Total: Rs.{subtotal:.2f}")

# Print the receipt footer
print("----------------------------")
print("Thank you for shopping with us!")
