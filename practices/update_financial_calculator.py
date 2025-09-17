# AB 7th Update Financial Calculator

def get_expense(name, income):
    amount = float(input(f"What is your monthly {name}: "))
    percent = (amount / income) * 100
    print(f"Your {name} is ${amount:.2f} and that is {percent:.0f}% of your income.")
    return amount

def main():
    income = float(input("What is your monthly income: "))

    rent = get_expense("rent/mortgage", income)
    utilities = get_expense("utilities", income)
    groceries = get_expense("groceries", income)
    transportation = get_expense("transportation", income)

    savings = income * 0.10
    print(f"\nYou should save ${savings:.2f} a month, that is 10% of your income.")

    total_expenses = rent + utilities + groceries + transportation + savings
    leftover = income - total_expenses
    print(f"You have ${leftover:.2f} of spending money each month!")

main()