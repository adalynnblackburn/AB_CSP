// AB 7th Expressions Notes
#include <stdio.h>
#include <math.h>

int main(void){
    int year = 2025;
    float pi = 3.14;
    double long_pi = 3.14159265359;
    printf("%d", year);
    printf("%d", 8/3);
    printf("%f.2\n", 8.0/3);
    printf("%d\n", (int) pow(2,4));

    year += 1; //compound assighnment operator
    printf("%d\n", year);
    year += 1;
    printf("%d\n", year);

    return 0;
}