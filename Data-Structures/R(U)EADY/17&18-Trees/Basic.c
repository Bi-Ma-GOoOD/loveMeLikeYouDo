/*Basic Operation on Ordered Trees*/

#include <stdio.h>
#include <stdlib.h>

struct node{
    int key;
    struct node *parent;
    struct node *leftChild;
    struct node *rightSibling;
};

struct node *createRoot(int key){
    //Allocate memory for new node
    struct node *node = (struct node*)malloc(sizeof(struct node));

    //Assign key to this node
    node -> key = key;
    //Initialize parent
    node -> parent = NULL;
    //Initialize left child, and right child as NULL
    node -> leftChild = NULL;
    node -> rightSibling = NULL;
    return node;
}

struct node* createNode(int key, struct node* parent){
    //Allocate memory for new node
    struct node *node = (struct node*)malloc(sizeof(struct node));
    //Assign key to this node
    node -> key = key;
    //Initialize parent
    node -> parent = parent;
    //Initialize left child, and right child as NULL
    node -> leftChild = NULL;
    node -> rightSibling = NULL;
    //Set this node as a child to it's parent
    if(node->parent != NULL){
        if(node->parent->leftChild != NULL){
            struct node *child = node->parent->leftChild;
            while(child->rightSibling != NULL){
                child = child ->rightSibling;
            }
            child->rightSibling = node;
        }
        else{
            node->parent->leftChild = node;
        }
    }
    return node;
}

struct node *getParent(struct node *node){
    return node->parent;
}

struct node* getChild(struct node *node, int k){
    struct node *child = node->leftChild;
    for(int i = 1; i < k; i++){
        child = child -> rightSibling;
    }
    return child;
}