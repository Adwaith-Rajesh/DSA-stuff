// binary search is performed on arrays the are already sorted
// the current program is implemented according to assumption that the
// given array is sorted

#include <stdio.h>

void main() {
    int size, key, found = 0;
    printf("Enter the number of elements: ");
    scanf("%d", &size);

    printf("Enter %d numbers\n", size);

    int arr[size];

    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }

    printf("The array\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    printf("Enter the number to search: ");
    scanf("%d", &key);

    // binary search

    int low = 0;
    int high = size;
    int mid;

    while (high != low) {
        mid = (low + high) / 2;
        if (arr[mid] == key) {
            found = 1;
            break;
        } else {
            if (key < arr[mid])
                high = mid - 1;
            else
                low = mid + 1;
        }
    }

    if (found) {
        printf("%d found at pos %d\n", key, mid);
    } else {
        printf("key not found");
    }
}