#include <stdio.h>
// Driver Code
int main() {
    // Declare variables
    int product_amount, target_price;
    // Input Amount Product and Target Price
    scanf("%d %d", &product_amount, &target_price);
    // Initial prices array
    int prices[product_amount];
    for (int i = 0; i < product_amount; i++) {
        scanf("%d", &prices[i]);
    }
    // Initial dp array = 0
    int subset_square[target_price + 1];
    for (int i = 0; i <= target_price; i++) {
        subset_square[i] = 0;
    }
    // Calculate by use subset sum
    subset_square[0] = 1;
    for (int i = 0; i < product_amount; i++) {
        for (int j = prices[i]; j <= target_price; j++) {
            // จะเข้า if ได้ก็ต่อเมื่อ j - prices[i] = ตัวเลขบางอย่าง(x)
            // แล้วเมื่อนำ x มาเป็น dp[x] ถ้าหากมีค่า = 1 แปลว่า เข้า if ได้เพราะเป็น T
            // จากนั้นจะทำการเปลี่ยน dp[j] = 1
            if (subset_square[j - prices[i]]) {
                subset_square[j] = 1;
            }
        }
    }
    // Check the last index in subset_square is True || False
    if (subset_square[target_price]) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }
}
