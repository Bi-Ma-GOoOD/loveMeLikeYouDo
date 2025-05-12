#include <stdio.h>
#include <stdlib.h>

int main(){
    int i;
    int *p, *q;

    p = (int *)calloc(5,sizeof(int));
    q = (int *)malloc(5*sizeof(int));

    if(p == NULL)
        printf("Memory allocation by calloc(); failed\n");
    else if(q == NULL)
        printf("Memory allocation by malloc(); failed\n");
    else{
        printf("Calloc()\t Malloc()\n");
        for(i = 0; i < 3; i++){
            printf("p[%d] = %d\t q[%d] = %d\n", i, p[i], i, *(q+i));
        }
        free(p);
        free(q);
    }
}