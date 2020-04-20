# Prompt the user for information

age = int(input("Please enter the age of your child: "))
children = int(input("Please enter the number of children in your family: "))
income = int(input("Please enter the family annual income: $"))

if age < 8 or age > 16:
    # No calculations if they can't attend
    print("N/A - They can't attend")
else:

    # Determine their base price
    # Note that we already know the age is 8-16
    if age <= 10:
        base_price = 1000
    elif age <= 12:
        base_price = 1500
    else:
        base_price = 2000
    
    # Determine discount based on income and 
    # children in the family
    if income < 25000:
        if children == 1:
            discount = 0.70
        elif children == 2:
            discount = 0.80
        else:
            discount = 0.90
    elif income < 50000:
        if children == 1:
            discount = 0.40
        elif children == 2:
            discount = 0.50
        else:
            discount = 0.60
    elif income < 75000:
        if children == 1:
            discount = 0.10
        elif children == 2:
            discount = 0.20
        else:
            discount = 0.30
    else:
        # Family size does not matter for 
        # the higher income bracket
        discount = 0

    # Calculate the updated price and display it.
    price = base_price * (1 - discount)
    print("Price for child is: ${}".format(price))

