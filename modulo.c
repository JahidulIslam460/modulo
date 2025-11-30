#include <stdio.h>
#include <stdlib.h>

// Modulo operation function
int modulo_operation(int a, int b) {
    if (b == 0) {
        printf("Error: Cannot perform modulo by zero\n");
        exit(1);
    }
    return a % b;
}

// Check if number is even
int is_even(int number) {
    return number % 2 == 0;
}

// Check if number is odd
int is_odd(int number) {
    return number % 2 == 1;
}

// Main function
int main() {
    printf("C Modulo Operations:\n");
    printf("====================\n");
    
    // Test modulo operations
    printf("10 %% 3 = %d\n", modulo_operation(10, 3));
    printf("15 %% 4 = %d\n", modulo_operation(15, 4));
    printf("8 %% 2 = %d\n", modulo_operation(8, 2));
    
    // Test even/odd
    printf("Is 7 even? %s\n", is_even(7) ? "Yes" : "No");
    printf("Is 12 odd? %s\n", is_odd(12) ? "Yes" : "No");
    printf("Is 12 even? %s\n", is_even(12) ? "Yes" : "No");
    
    return 0;
}
