// AB 7th Variables Notes
#include <stdio.h>

int main(void){
    int grade; //4 bytes
    const float pi = 3.14; //4bytes
    double long_pi = 3.1415926358; //8 bytes
    char letter_grade; //1 byte
    char name[] = "Adalynn"; //list of characters
//User input
    printf("What is your grade percentage as a whole number: ");
    scanf("%d", &grade);

    printf("What is your letter grade: ");
    scanf(" %c", letter_grade);


    printf("%s did it!\n", name); //%s is place holder for variable (s inserts string)(d inserts integer)(c inserts a single character)
    printf("You have a %d, in the class. That is an %c\n", grade, letter_grade);

    return 0;
}