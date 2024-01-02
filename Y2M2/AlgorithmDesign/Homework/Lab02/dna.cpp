#include <iostream>
#include <algorithm>

int findLongestDNASequence(char *s) {
    int maxLength = 1;  // Initialize the length of the longest consecutive sequence to 1
    int currentLength = 1;  // Length of the consecutive sequence in the current iteration

    for (int i = 1; s[i] != '\0'; i++) {
        if (s[i] == s[i - 1]) {
            currentLength++;
        } else {
            currentLength = 1;  // Reset the length of the consecutive sequence
        }

        // Update the length of the longest consecutive sequence
        if (currentLength > maxLength) {
            maxLength = currentLength;
        }
    }

    return maxLength;
}

int main() {
    char s[1000000];
    scanf("%s", s);

    // Find the length of the longest consecutive DNA sequence
    int length = findLongestDNASequence(s);

    // Print the length of the longest consecutive DNA sequence
    printf("%d\n", length);

    return 0;
}