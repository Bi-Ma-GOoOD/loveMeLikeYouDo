#include <stdio.h>
#include <stdlib.h>

struct node{
    int key;
    struct node *parent;
    struct node *leftChild;
    struct node *rightSibling;
    struct node *array;
};

struct node *createRoot(int key);
struct node *createNode(int key, struct node* parent);
struct node *getChild(struct node *node, int amount);

int main(){
    int vertices, root, parent, i, j, k;
    int child = 2, count = 0;

    printf("Enter vertices: ");
    scanf("%d ", &vertices);

    // int array[vertices], array1[vertices];

    for(i = 0; i <= vertices-1; ++i){
        if(i == 0){
            printf("Enter start root and child: ");
            scanf("%d", &root);
            struct node* array[i] = createRoot(root);
            struct node* array[i+1] = createNode(child, array[i]);
            i++;
            child ++;
        }else{
            printf("Enter start root and child: ");
            scanf("%d", &parent);
            struct node* array[i] = createNode(child, array[parent]);
            child ++;
        }
    }
    for(j = 0; array[j] != NULL; ++j){
        int amount;
        amount = getChild(array[j], count)->key;
        array1[j] = amount;
        amount = 0;
    }
    for(k = 0; k < vertices; ++k){
        printf("%d  ", &array1[k]);
    }
}

struct node *createRoot(int key){
    struct node *node = (struct node*)malloc(sizeof(struct node));
    
    node -> key = key;
    node -> parent = NULL;
    node -> leftChild = NULL;
    node -> rightSibling = NULL;
    return (node);
}

struct node* createNode(int key, struct node *parent){
    struct node* node = (struct node*)malloc(sizeof(struct node));
    node -> key = key;
    node -> parent = parent;
    node -> leftChild = NULL;
    node ->rightSibling = NULL;

    if(node->parent != NULL){
        if(node->parent->leftChild != NULL){
            struct node* child = node->parent->leftChild;
            while(child->rightSibling != NULL){
                child = child->rightSibling;
            }
            child->rightSibling = node;
        }else{
            node->parent->leftChild = node;
        }
    }
    return node;
}

struct node *getChild(struct node* array, int count){
    struct node* child = array->leftChild;
    for(int i = 0; child != NULL; ++i){
        count += 1;
    }
    return count;
}