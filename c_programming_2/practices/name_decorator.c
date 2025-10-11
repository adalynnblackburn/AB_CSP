// AB 7th Name Decorator

#include <stdio.h>
#include <string.h>

int main() {
    char name[50];
    char decorated[100];

    printf("Enter your name: ");
    scanf("%49s", name);

    sprintf(decorated, "<<< %s >>>", name);

    printf("%s\n", decorated);

    return 0;
}