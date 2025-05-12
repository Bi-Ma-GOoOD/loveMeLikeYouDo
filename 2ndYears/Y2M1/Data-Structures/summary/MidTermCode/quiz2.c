#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Nd{
    int data;
    struct Nd *next;
}node;

typedef struct Linklist{
    int lenght;
    node *head;
}numlist;

node *newnode(){
    node *p;

    p = (node *)malloc(sizeof(node));
    p->next = NULL;
    return p;
}

int main(){
    node *first = newnode();
    node *second = newnode();

    first->data = 1;
    first->next = second;
    second->data = 2;
    second->next = NULL;
    return 0;
}