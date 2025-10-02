// AB 7th Variables Notes
#include <stdio.h>

int main(void){
    int grade = 95; //4 bytes
    float pi = 3.14; //4bytes
    double long_pi = 3.1415926358; //8 bytes
    char letter_grade = 'A'; //1 byte
    char name[] = "Adalynn"; //list of characters
    printf("%s did it!", name); //%s is place holder for variable (s inserts string)(d inserts integer)(c inserts a single character)
    printf("You have a %d, in the class. That is an %c", grade, letter_grade);

    return 0;
}