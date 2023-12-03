#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct nd{
    // struct item data;
    struct nd *next;
}node;

void delete(node *curr){
    node *temp;

    temp = curr->next;
    curr->next = temp->next;
    free(temp);
}