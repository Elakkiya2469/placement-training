#include<stdio.h>
int main() {
    int number,remainder, sum = 0;
    printf("Enter an integer: ");
    scanf("%d", &number);

    while (number != 0) {
        remainder = number % 10;
        sum += remainder;
        number /= 10;
    }
    printf("Sum of the digits: %d\n", sum);
    return 0;
}
