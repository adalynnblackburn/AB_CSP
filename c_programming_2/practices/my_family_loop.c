// AB 7th My Family Loop Practice

#include <stdio.h>

int main(void){
    char families[][20] = {"Mom", "Evelynn", "McAlynn", "Ashlynn", "Dad"};
    for(int i = 0; i < 5; i++){
        printf("Hello, %s!\n", families[i]);
    }

    return 0;
}