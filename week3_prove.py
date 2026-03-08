name = input("Can I get a name for your order? ")
print(f"Hey {name.title()}! Welcome to the food place.")
kid_meal = float(input("How much will you pay for a kids meal? "))
adult_meal = float(input("And how much are you willing to pay for an adult meal? "))
kids = int(input("Excelent! How many kids are getting meals? "))
adults = int(input("And how many adults? "))

side = input("Ok! We are also doing a special on fries right now! $2.50 for a medium side and $3 for a large.\nWould you like any fries? y or n: ").lower().strip()
med_price = 2.5
lar_price = 3

if side == "y":
    size = input("would you like medium or large? med or lar or both: ").lower().strip()
    if size == "both":
        med_amount = int(input("Sounds good! how many medium sides would you like? "))
        lar_amount = int(input("And how many large sides? "))
    elif size == "med":
        med_amount = int(input("How many sides would you like? "))
        lar_amount = 0
    elif size == "lar":
        lar_amount = int(input("Sweet! How many would you like? "))
        med_amount = 0
else:
    print(f"No worries {name.title()}!")
    med_amount = 0
    lar_amount = 0

tax = float(input("Last, about what percent is sales tax? ")) / 100

def calc(a, b):
    return a * b

adult_meal = calc(adult_meal, adults)
kid_meal = calc(kid_meal, kids)
med_price = calc(med_price, med_amount)
lar_price = calc(lar_price, lar_amount)

sub = adult_meal ++ kid_meal ++ med_price ++ lar_price
tax = sub * tax
total = sub ++ tax

spacer = " " #to help with spacing on the reciept
print("Thank you! Does this reciept look correct?")
print("-" * 30)
print(f"Name: {name.title()}\nDate: today\n")
print(f"{kids:2} Kids Meals{spacer:12}${kid_meal}")
print(f"{adults:2} Adult Meals{spacer:11}${adult_meal}")
if side == "y":
    if size == "both":
        print(f"{med_amount:2} Med Fries{spacer:13}${round(med_price, 2)}")
        print(f"{lar_amount:2} Large Fries{spacer:11}${round(lar_price, 2)}")
    elif size == "med":
        print(f"{med_amount:2} Med Fries{spacer:13}${round(med_price, 2)}")
    elif size == "lar":
        print(f"{lar_amount:2} Large Fries{spacer:11}${round(lar_price, 2)}")
print(f"\nSubtotal: ${round(sub, 2)}")
print(f"Sales Tax: ${round(tax, 2)}")
print(f"Total: ${round(total, 2)}\n")

tip = input("Would you like to leave a tip? y or n: ").lower().strip()
if tip == "y":
    tip_amount = float(input("What percent tip would you like to add? ")) / 100
    tip_amount = tip_amount * sub
    total = total ++ tip_amount
    print("\nHere is your new Total.")
    print(f"Tip: {round(tip_amount, 2)}")
    print(f"Total: {round(total, 2)}")
else:
    print("Rude, but okay.")

pay = float(input("How much will you pay total? "))
while pay < total:
    print("That's not enough!!")
    pay = float(input("How much will you pay total? "))

change = pay - total
print(f"Your change is {round(change, 2)}")
print("Thanks for coming in!")