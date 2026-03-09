cart = []
done = False
print('Welcome! type items you would like to add in your cart. (type "quit" to end)')
while not done:
    item = input("what would you like to add to the cart? ")
    if item.lower() == "quit":
        done = True
    else:
        cart.append(item.title())

print("\nYour shopping cart has:")
for i in range(len(cart)):
    print(cart[i])

print("\nWith indexes your cart is:")
for i in range(len(cart)):
    print(f"{i}. {cart[i]}")

print('\nYou may now change items if you want. (type "quit" to end)')
done = False
while not done:
    index = input("Which index number would you like to change? ")
    if index.lower() == "quit":
        done = True
    else:
        item = input(f"What would you like to replace {cart[int(index)]} with? ")
        cart[int(index)] = item.title()
        print("With indexes your cart is: ")
        for i in range(len(cart)):
            print(f"{i}. {cart[i]}")

