// AB 7th Old Enough Practice

#include <stdio.h>

int main(){
    int age;

    printf("How old are you: ");
    scanf("%d", &age);

    if (age >= 18){
        printf("You are old enough to vote\n");
    }else if (age >= 16){
        printf("You aare old enough to drive\n");
    }else if (age >= 15){
        printf("You are old enough to get a learners permit\n");
    }else if (age >= 5){
        printf("You are old enough to go to school\n");
    }else {
        printf("You can't do anything :) hahaha...\n");
    }

    return 0;
}