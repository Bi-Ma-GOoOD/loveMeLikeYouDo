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
/*ให้ทําการสร้าง rooted tree ในรูปประกอบด้านว่างด้วยวิธีhardcode ใน main function โดยนิสิต
จะต้องสร้างโหนดใน tree ผ่าน createNode operation*/
struct node *createRoot(char *name, int size, int type);
struct node *createNode(char *name, int size, int type, struct node *parent);
void postOrderTraversal(struct node *root, int *totalSize);
void preOrderTraversal(struct node *root);

int main(){
    int total_size = 0;
    struct node* user = createRoot("/user/rt/courses/",1,1);
    
    struct node* cs016 =createNode("cs016/",2,1,user);
    struct node* cs252 =createNode("cs252/",1,1,user);
    
    struct node* grade1 =createNode("grades",8,0,cs016);
    struct node* homeworks =createNode("homeworks/",1,1,cs016);
    struct node* programs =createNode("programs/",1,1,cs016);
    
    struct node* project =createNode("projects/",1,1,cs252);
    struct node* grade2 =createNode("grades",3,0,cs252);
    
    struct node* hw1 =createNode("hw1",3,0,homeworks);
    struct node* hw2 =createNode("hw2",2,0,homeworks);
    struct node* hw3 =createNode("hw3",4,0,homeworks);
    
    struct node* pr1 =createNode("pr1",57,0,programs);
    struct node* pr2 =createNode("pr2",97,0,programs);
    struct node* pr3 =createNode("pr3",74,0,programs);
    
    struct node* papers =createNode("papers/",1,1,project);
    struct node* demos =createNode("demos/",1,1,project);
    
    struct node* buylow =createNode("buylow",26,0,papers);
    struct node* sellhigh =createNode("sellhigh",55,0,papers);
    
    struct node* market =createNode("market",4786,0,demos);
    postOrderTraversal(user, &total_size);
    preOrderTraversal(user);
    printf("total size is: %d\n",total_size);
}
/*ให้ทําการสร้าง rooted tree ในรูปประกอบด้านว่างด้วยวิธีhardcode ใน main function โดยนิสิต
จะต้องสร้างโหนดใน tree ผ่าน createNode operation*/
struct node *createRoot(char *name, int size, int type){
    struct node *node = (struct node*)malloc(sizeof(struct node));
    
    strcpy(node->name, name);
    node->size = size;
    node->type = type;
    node->parent = NULL;
    node->firstChild = NULL;
    node->nextChild = NULL;
    node->total_size = 0;
    return (node);
}
struct node *createNode(char *name, int size, int type, struct node *parent){
    struct node *node = (struct node *)malloc(sizeof(struct node));

    strcpy(node->name, name);
    node->size = size;
    node->type = type;
    node->parent = parent;
    node->firstChild = NULL;
    node->nextChild = NULL;
    node->total_size = 0;

    if(node->parent != NULL){
        if(node->parent->firstChild != NULL){
            struct node *child = node->parent->firstChild;
            while(child->nextChild != NULL){
                child = child->nextChild;
            }
            child->nextChild = node;
        }else{
            node->parent->firstChild = node;
        }
    }
    return node;
}
void postOrderTraversal(struct node *root, int *totalSize){
    struct node *child = root->firstChild;
    while(child != NULL){
        postOrderTraversal(child, totalSize);
        child = child->nextChild;
    }
    root->total_size = root->size; 
    *totalSize += root->total_size;
}
void preOrderTraversal(struct node *node){
    struct node *child = node->firstChild;
    while(child != NULL){
        preOrderTraversal(child);
        child = child->nextChild;
    }
    printf("name: %s, size: %d\n", node->name, node->size);
}
