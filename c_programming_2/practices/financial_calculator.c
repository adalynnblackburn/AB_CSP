// AB 7th Financial Calculator

#include <stdio.h>

int main(){
    float monthly_income;
    float rent;
    float utilities;
    float groceries;
    float transportation;

    printf("What is your monthly income: ");
    scanf("%f", &monthly_income);

    printf("\nWhat is your monthly rent: ");
    scanf("%f", &rent);

    printf("\nWhat is your monthly utilities cost: ");
    scanf("%f", &utilities);

    printf("\nWhat is your monthly groceries cost: ");
    scanf("%f", &groceries);

    printf("\nWhat is you monthly transportation cost: ");
    scanf("%f", &transportation);

    float total_expenses = rent + utilities + groceries + transportation;
    float savings = monthly_income* 0.10;
    float spending_money = monthly_income - total_expenses - savings;

    float rent_percent = (rent/monthly_income)*100;
    printf("Your rent is %.2f and that is %.0f percent of your income.\n", rent, rent_percent);

    float utilities_percent = (utilities/monthly_income)*100;
    printf("Your utilities are %.2f and that is %.0f percent of your income.\n", utilities, utilities_percent);

    float groceries_percent = (groceries/monthly_income)*100;
    printf("Your groceries are %.2f and that is %.0f percent of your income.\n", groceries, groceries_percent);

    float transportation_percent = (transportation/monthly_income)*100;
    printf("Your transportation is %.2f and that is %.0f percent of your income.\n", transportation, transportation_percent);

    float savings_percent = (savings/monthly_income)*100;
    printf("\nYou should save %.2f a month, this is %.0f percent of your income.\n", savings, savings_percent);
    //I couldn't figure out how to use the % sign in the printf statement so I spelt it instead?
    
    printf("\nYou have %.2f of spending money each month\n", spending_money);
    
return 0;
}