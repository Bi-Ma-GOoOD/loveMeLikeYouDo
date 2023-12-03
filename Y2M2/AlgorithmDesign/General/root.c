#include <stdio.h>

double rotoroto(double number) {
  double estimate = 0;
  while (1) {
    double new_estimate = (estimate + number / estimate) / 2;
    printf("%.12f", new_estimate);
    if (new_estimate == estimate) {
      break;
    }
    estimate = new_estimate;
  }
  return estimate;
}

int main() {
  double result = rotoroto(2);
  printf("%.12f\n", result);
  return 0;
}
