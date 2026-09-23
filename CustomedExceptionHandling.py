def withdraw(balance , ammount):
    if ammount <= 0:
        raise ValueError("balance must be greater then zero")
    elif ammount > balance:
        raise ValueError("Issuficient balance")
    else:
        return balance-ammount


try:
    balance = int(input("enter balance in your accaunt"))
    amount = int(input("enter amount you want to withdraw"))
    current_balance = withdraw(balance,amount)
    print(current_balance)
except ValueError as e:
    print("error: ",e)
    
