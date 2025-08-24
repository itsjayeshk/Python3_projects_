money_owed = float(input("Enter the amount of money: "))
apr = float(input("Enter the annual percentage rate: "))
payment = float(input("Enter the monthly payment: "))
months = int(input("Enter the number of months: "))
monthly_rate = apr/100/12
interest_paid = money_owed*monthly_rate
money_owed = interest_paid + money_owed
money_owed = money_owed - payment
print("Paid ", payment, "of which ", interest_paid, "was interest")
print("After ", months, "months, you owe ", money_owed)
