#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct nd{
    int data;
    struct nd *next;
}node;

void insert(node *curr){
    node *temp;

    temp = (node *)malloc(sizeof(node));
    temp->next = curr->next;
    curr->next = temp;
}