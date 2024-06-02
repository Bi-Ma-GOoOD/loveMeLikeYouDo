#include <stdlib.h>

struct node{
    int key;
    struct node *parent;
    struct node *left;
    struct node *right;
};

struct node *createNode(int key){
    // New node
    struct node *node = (struct node *)malloc(sizeof(struct node));

    //Assign ke to this node
    node->key = key;

    //Initialize parent , left and rith child as NULL
    node->parent = NULL;
    node->left = NULL;
    node->right = NULL;
    return(node);
}

// Insert Left
struct node *createLeft(int key, struct node *parent){
    // Insert new node as a left child of parent
    struct node *node = create(key);
    parent->left = node;
    node->parent = parent;
    return(node);
}

// Insert Right
struct node *createRight(int key, struct node *parent){
    // Insert new node as a right child of parent
    struct node *node = create(key);
    parent->right = node;
    node->parent = parent;
    return(node);
}

int main(){
    /*create root*/
    struct node *root = createNode(1);
    createLeft(2, root);
    createRight(3, root);
    createLeft(4, root->left);
    return 0;
}