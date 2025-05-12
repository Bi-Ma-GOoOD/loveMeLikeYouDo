#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct nd{
    int data;
    struct nd *next;
}node;

typedef struct linked_list{
    int length;
    node *head;
}numlist;

node *newnode(){
    node *p;

    p = (node*)malloc(sizeof(node));
    p->next = NULL;
    return p;
}

void initList(numlist *n){
    n->head = NULL;
}

int appendHeadList(numlist *s, node *p){
    if(s->head == NULL){
        s->head = p;
    }else{
        p->next = s->head;
        s->head = p;
    }
}

void printNumList(numlist l){
    node *pCurr = l.head;

    while(pCurr != NULL){
        printf("Num: %d\n", pCurr->data);
        pCurr = pCurr->next;
    }
}

int main(){
    numlist nl;
    node *n;
    initList(&nl);

    for(int i = 0; i < 3; ++i){
        n = newnode();
        n->data = i;
        appendHeadList(&nl, n);
    }

    printNumList(nl);
    return 0;
}