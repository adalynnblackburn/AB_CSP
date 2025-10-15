// AB Update Financial Calculator

#include <stdio.h>

float money(char*sum){
    float value;
    printf("What is your monthly %d:\n", sum);
    scanf("%d", &sum);
    return value;
}

int main(void){
    float income = money("income");
    float rent = money("rent");
    float utilities = money("utilities");
    float gorceries = money("grocries");
    float transportation = money("transportation");

    return 0;
}