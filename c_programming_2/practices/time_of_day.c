// AB 7th Time of Day Practice

#include <stdio.h>

int main(){
    int hour;
    
    printf("What is the hour in military time: ");
    scanf("%d", &hour);

    if (hour >= 5 && hour < 12){
        printf("Good Morning\n");
    }else if (hour >= 12 && hour < 17){
        printf("Good Afternoon\n");
    }else if (hour >= 17 && hour <= 21){
        printf("Good Evening\n");
    }else{
        printf("Good Night\n");
    }
    
    return 0;
}