#include <stdio.h>
int main(){
    long check_num;
    long total = 0;
    scanf("%ld", &check_num);
    while(check_num>=1){
        total += check_num;
        check_num = check_num / 2;
    }
    printf("%ld", total);
}