// linearly search for an element in a an array of n elements

#include <stdio.h>

void main() {
    int size, key, found = 0;

    printf("Enter the size of the array: ");
    scanf("%d", &size);

    int arr[size];

    printf("Enter %d elements\n", size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }

    printf("The array\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    printf("Enter the key to search: ");
    scanf("%d", &key);

    for (int i = 0; i < size; i++) {
        if (arr[i] == key) {
            found = 1;
            printf("Key found ar pos: %d\n", i);
            break;
        }
    }

    if (!found) {
        printf("The key does not exists in the array\n");
    }
}
