// AB 7th First Program 

#include <stdio.h>

int main(void){
    char name[50];
    printf("What is your name human?");
    scanf("%49s", name);
    printf("Hello, %s :)\n", name);
    
    return 0;
}