// AB 7th Variables Practice

#include <stdio.h>

int main(){
    char name[50];
    int lucky_number;
    float decimal_number;
    char breakfast[100];
    char favourite_color[30];
    char school_name[100];
    int year;
    char eye_color[20];
    int age;
    char favourite_subject[50];

    printf("What is your name: ");
    fgets(name, sizeof(name), stdin);

    printf("Enter your lucky number (1-10): ");
    scanf("%d", &lucky_number);

    printf("What is a decimal number (100-1000): ");
    scanf("%f", &decimal_number); 
    getchar();//my sister told me to put this so that it works this time

    printf("What is something you eat for breakfast: ");
    fgets(breakfast, sizeof(breakfast), stdin);

    printf("What is your favourite color: ");
    fgets(favourite_color, sizeof(favourite_color), stdin);

    printf("What is the year: ");
    scanf("%d", &year);
    getchar();

    printf("Enter the color of your eyes: ");
    fgets(eye_color, sizeof(eye_color), stdin);

    printf("How old are you: ");
    scanf ("%d", &age);
    getchar();

    printf("What is your favourite school subject: ");
    fgets(favourite_subject, sizeof(favourite_subject), stdin);

    printf("Name: %s", name);
    printf("Lucky Number (1-10): %d\n", lucky_number);
    printf("Decimal Number (100-1000): %.2f\n", decimal_number);
    printf("Breakfast: %s", breakfast);
    printf("Favourite Color: %s", favourite_color);
    printf("School Name: %s", school_name);
    printf("Year: %d\n", year);
    printf("Eye Color: %s", eye_color);
    printf("Age: %d\n", age);
    printf("Favourite Subject: %s", favourite_subject);

    return 0;
}