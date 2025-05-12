#include <stdio.h>

int main(){

    int a[4] = {101, 201, 301};
    int b[]  = {101, 201, 301};
    int i;
    char c[3] = "ab";
    char d[3] = {'a', 'b'};

    printf("Compare between array a and array b\n");
    for(i = 0 ; i < 3 ; i++) printf("a[%d] = %d, b[%d] = %d\n",i, a[i], i , b[i]);
    printf("sizeof a is %d\n",sizeof(a));
    printf("sizeof b is %d\n",sizeof(b));
    printf("So array a same as array b\n\n");

    for(i = 0; i < 3 ; i++)
        if(c[i] == '\0') printf("c[%d] -> array c terminate with NULL character\n", i);
        else printf("c[%d] = %c\n", i, c[i]);
    for(i = 0; i < 3; i++)
        if(d[i] == '\0') printf("d[%d] -> array d terminate with NULL character\n", i);
        else printf("d[%d] = %c\n", i, d[i]);
}