#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct nd{
    int data;
    struct nd *next;
}node;

node *newNode(){
    node *p;

    p = (node *)malloc(sizeof(node));
    p->next = NULL;
    return p;
}

int main(){
    node *first = newNode();
    node *last = newNode();
    first->data = 1;
    first->next = last;
    last->data = 5;
    last->next = NULL;
    return 0;
}