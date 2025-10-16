// AB Update Financial Calculator

#include <stdio.h>
float stuff(char *info) {
    float value;
    printf("%s", info);
    scanf("%f", &value);
    return value;
}
int print_expense(char *label, float amount, float income) {
    float percent = (amount / income) * 100;
    printf("%s: %.2f which is %.0f percent of your income\n", label, amount, percent);
}
int main() {
    float monthly_income = stuff("What is your monthly income: ");
    float rent = stuff("What is your monthly rent: ");
    float utilities = stuff("What is your monthly utilities cost: ");
    float groceries = stuff("What is your monthly groceries cost: ");
    float transportation = stuff("What is your monthly transportation cost: ");
    float total_expenses = rent + utilities + groceries + transportation;
    float savings = monthly_income * 0.10;
    float spending_money = monthly_income - total_expenses - savings;
    print_expense("Rent", rent, monthly_income);
    print_expense("Utilities", utilities, monthly_income);
    print_expense("Groceries", groceries, monthly_income);
    print_expense("Transportation", transportation, monthly_income);
    float savings_percent = (savings / monthly_income) * 100;
    printf("\nYou should save %.2f a month which is %.0f percent of your income\n", savings, savings_percent);
    printf("You have %.2f of spending money each month\n", spending_money);
    return 0;
}