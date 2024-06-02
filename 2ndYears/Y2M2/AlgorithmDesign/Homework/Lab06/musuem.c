#include <stdio.h>

long long nCr(int n, int r) {
  if (r > n / 2) {
    r = n - r;
  }
  long long result = 1;
  for (int i = 1; i <= r; ++i) {
    result *= (n - r + i);
    result /= i;
  }
  return result;
}
// Driver Code
int main() {
  // Input
  int night, weight_max;
  scanf("%d %d", &night, &weight_max);

  int items[night][2];  // Array to store weight and value of artifacts

  for (int i = 0; i < night; ++i) {
    scanf("%d %d", &items[i][0], &items[i][1]);
  }

  // Calculate total combinations
  long long total_combinations = nCr(night, weight_max);

  // Calculate total damage and count valid subsets
  long long total_damage = 0;
  int count = 0;
  for (int i = 0; i < (1 << night); ++i) {  // Iterate through all subsets
    int weight = 0, value = 0;
    for (int j = 0; j < night; ++j) {
      if (i & (1 << j)) {  // Check if artifact is included in the subset
        weight += items[j][0];
        value += items[j][1];
      }
    }
    if (weight <= weight_max) {
      // Add to total damage
      total_damage += value;
      count++;
    }
  }

  // Calculate and print average damage
  double average_damage = (double)total_damage / count;
  printf("%.2lf\n", average_damage);

  return 0;
}