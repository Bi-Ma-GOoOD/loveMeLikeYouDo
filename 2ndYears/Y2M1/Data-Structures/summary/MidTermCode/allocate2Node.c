#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct nd{
    int data;
    struct nd *next;
}node;

int main(){
    node *first = NULL;
    node *last = NULL;

    first = (node *)malloc(sizeof(node));
    last = (node *)malloc(sizeof(node));

    first->data = 1;
    first->next = last;

    last->data = 5;
    last->next = NULL;

    return 0;
}