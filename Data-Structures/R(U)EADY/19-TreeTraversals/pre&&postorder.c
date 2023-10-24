/*อธิบายในส่วนของการทำ pre และ post คับ ซึ่งการทำ pre และ post จะอยู่ในส่วนของ 
link structure Tree */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node{
    char name[100];
    int size;
    int type;
    int total_size;
    struct node *parent;
    struct node *firstChild;
    struct node *nextChild;
};

// postorder Traversal
void postOrderTraversal(struct node *root, int *totalSize){
    struct node *child = root->firstChild;
    while(child != NULL){
        postOrderTraversal(child, totalSize);
        child = child->nextChild;
    }
    root->total_size = root->size; 
    *totalSize += root->total_size;
}

// preorder Traversal
void preOrderTraversal(struct node *node){
    struct node *child = node->firstChild;
    while(child != NULL){
        preOrderTraversal(child);
        child = child->nextChild;
    }
    printf("name: %s, size: %d\n", node->name, node->size);
}