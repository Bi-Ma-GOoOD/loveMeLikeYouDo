#include <stdio.h>
// Driver Code
int main() {
    // Declare variables
    int n = 4, k = 50;
    // Initialize prices array
    int prices[4] = {23, 29, 37, 19};

    int dp[k + 1];
    for (int i = 0; i <= k; i++) {
        dp[i] = 0;
    }
    dp[0] = 1;

    for (int i = 0; i < n; i++) {
        for (int j = prices[i]; j <= k; j++) {
            if (dp[j - prices[i]]) {
                dp[j] = 1;
            }
        }
    }

    if (dp[k]) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }
}
