#include <stdio.h>

int main(){
    char buf[128];
    int i;

   for(i = 0; i < 128; i++){
    scanf("%c", buf);
   }
   int length = sizeof(buf)/sizeof(buf[0]);
   for(i = 0; i < length; i++){
    printf("%c", buf[i]);
   }
}