print("Time to make a bank:-)")
print('Type "quit" when you are done making accounts.')

accounts = []
balances = []
done = False

while not done:
    name = input("What kind of account do you want to make? ")
    if name.lower() == "quit":
        done = True
    else:
        amt = float(input("How much money do you have in that account: $"))
        accounts.append(name.title())
        balances.append(amt)

print("Account info:")
for i in range(len(accounts)):
    print(f"{accounts[i]} - ${balances[i]:.2f}")

print(f"Total: ${sum(balances):.2f}")
print(f"Average: ${(sum(balances)/len(balances)):.2f}")