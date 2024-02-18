products = {}  # Dictionary to store product names and prices

    # Input loop to add products and prices
while True:
    product_name = input("Enter product name: ")
    price = float(input("Enter price: "))

    products[product_name] = price

    cont = input("Do you want to enter another product? (y/n): ").strip().lower()
    if cont != 'y':
        break

    # Searching for a product
search_product = input("Enter a product name to get its price: ")
if search_product in products:
    print(f"The price of {search_product} is ${products[search_product]:.2f}")
else:
    print("Product not found.")
