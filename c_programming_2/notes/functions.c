// AB 7th Functions Notes

#include <stdio.h>
void birthday(char*name, int age){
    printf("Happy Birthday to you!\n");
    printf("Happy Birthday to you!\n");
    printf("Happy Birthday dear %s!\n", name);
    printf("Happy Birthday to you!\n");
    printf("Happy Birthday %s you are %d!\n", name, age);
}

int mul(int x, int y){


    return x*y;
}

float get_number(char*type){
    float value;
    printf("How many %s do you have: ", type);
    scanf("%f", &value);
    return value;
}

int main(void){

    birthday("Tia", 15);
    birthday("Qwen", 14);
    birthday("Cecily", 16);
    int product = mul(8,5);
    printf("%d\n", product);
    printf("%d\n", mul(35,76));
    float pencils = get_number("pencils");
    float notebooks = get_number("notebooks");
    printf("You have %.2f pencils and %.2f notebooks", pencils, notebooks);

    return 0;
}