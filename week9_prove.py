print("Welcome to Walmart!")
cart = []
costs = []
amounts = []
exit = False
i = 0

while not exit:
    print("\nSelect an option:")
    print("1. View cart")
    print("2. Add to cart")
    print("3. Remove from cart")
    print("4. Checkout")
    print("5. Exit")
    action = input("Please enter an action: ")
    if action == "1":
        print("Your cart:")
        for i in range(len(cart)):
            print(f"{i + 1}: ({amounts[i]}) {cart[i]:20} - ${costs[i]:.2f}")
    elif action == "2":
        print("Adding to cart...")
        i = i + 1
        item = input("What would you like to add? ")
        cart.append(item.title())
        cost = float(input(f"How much does '{item.title()}' cost? "))
        amt = int(input(f"How many '{item.title()}' do you want? "))
        cost = cost * amt
        amounts.append(amt)
        costs.append(cost)
        print(f"{amt} '{item.title()}' added to cart.")
    elif action == "3":
        print("Your cart:")
        for i in range(len(cart)):
            print(f"{i + 1}: ({amounts[i]}) {cart[i]:20} - ${costs[i]:.2f}")
        item = int(input("Enter the number of the item you want to remove: "))
        if 1 <= item <= len(cart):
            cart.remove(cart[item - 1])
            costs.remove(costs[item - 1])
            amounts.remove(amounts[item - 1])
            print("item removed from cart.")
        else:
            print("Item not in cart.")
    elif action == "4":
        print("Your cart:")
        for i in range(len(cart)):
            print(f"{i + 1}: ({amounts[i]}) {cart[i]:20} - ${costs[i]:.2f}")
        total = sum(costs)
        print(f"Your total is: ${total:.2f}")
    elif action == "5":
        print("Goodbye!")
        exit = True
    else:
        print("Invalid option, please try again.")