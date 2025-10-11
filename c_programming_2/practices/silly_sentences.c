// AB 7th Silly Sentences

#include <stdio.h>

int main() {
    char name[30];
    char place[30];
    char object[30];

    printf("Enter a mystical/magical name (one word): ");
    scanf("%29s", name);

    printf("Enter a whimsical place (one word): ");
    scanf("%29s", place);

    printf("Enter an enchanted object (one word): ");
    scanf("%29s", object);

    printf("One day, %s went to %s and found a magical %s! When %s took the %s, %s threw it into the enchanted lake to get rid of the %s forever!\n", name, place, object, name, object, name, object);

    return 0;
}