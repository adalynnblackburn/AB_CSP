// AB 7th Loops Notes
#include <stdio.h>

int main(void){
    int nums[] = {1,654,4,56,8,742,5}; // Arrays = lists
    char candies[][20] = {"KitKat", "Skittles", "Nerds", "Hershey", "Reese's"};

    for(int x = 0; x < 7; x++){
        printf("%d\n", nums[x]);
    }

    for(int i = 0; i < 5; i++){
        printf("%s, is my favorite candy!\n", candies[i]);
    }

    int num = 0;
    while(num < 11){
        printf("%d\n", num);
        num++;
    }

    for(int num = 1; num < 11; num++){
        printf("%d\n", num);

    }

    return 0;
}