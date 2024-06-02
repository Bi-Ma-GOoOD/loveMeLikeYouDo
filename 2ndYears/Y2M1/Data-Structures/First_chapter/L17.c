#include <stdio.h>

int main(){
    int n[4] = {9, -7, 10, -2};
    float f[4] = {-0.5, 1,0.044, -3.1111};
    char l[4] = {'t', 'e', 's', 't'};
    
    for(int i = 0; i < 4; i++) {printf("%d %f %c\n",n[i], f[i], l[i]);}
    return 0;
}