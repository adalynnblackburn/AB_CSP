# AB 7th Financial Calculator

income = float(input("What is your monthly income: "))
rent = float(input("What is your monthly rent/mortgage: "))
utilities = float(input("What is your monthly utilities: "))
groceries = float(input("What is your monthly groceries: "))
transportation = float(input("What is your monthly transportation: "))

rent_percent = (rent / income) * 100
utilities_percent = (utilities / income) * 100
groceries_percent = (groceries / income) * 100
transportation_percent = (transportation / income) * 100

savings = income * 0.10
savings_percent = (savings / income) * 100
spending_money = income - (rent + utilities + groceries + transportation + savings)

print(f"\nYour rent is ${rent:.2f} and that is {rent_percent: .0f}% of your income.")
print(f"Your utilities are ${utilities:.2f} and that is {utilities_percent:.0f}% of your income.")
print(f"Your groceries are ${groceries:.2f} and that is {groceries_percent:.0f}% of your income.")
print(f"Your transportation is ${transportation:.2f} and that is {transportation_percent:.0f}% of your income.")
print(f"\nYou should save ${savings:.2f} a month, that is {savings_percent:.0f}% of your income.")
print(f"\nYou have ${spending_money:.2f} of spending money each month!")