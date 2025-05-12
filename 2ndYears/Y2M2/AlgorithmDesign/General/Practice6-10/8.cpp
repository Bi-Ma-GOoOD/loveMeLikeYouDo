#include <cstdio>
using namespace std;

struct BstNode {
    int data;
    BstNode *left;
    BstNode *right;
};
// create a node
BstNode *getNewNode(int data){
    BstNode *newNode = new BstNode();
    newNode -> data = data;
    newNode -> left = newNode -> right = NULL;
    return newNode;
}
// insert a node
BstNode *Insert(BstNode *root, int data){
    if(root == NULL){
        root = getNewNode(data);
        return root;
    }else if(data <= root -> data){
        root -> left = Insert(root -> left, data);
    }else{
        root -> right = Insert(root -> right, data);
    }
    return root;
}

int main(){
    BstNode *root = NULL; // creating an empty tree
    root = Insert(root, 4);
    root = Insert(root, 2);
    root = Insert(root, 5);
    root = Insert(root, 1);
    root = Insert(root, 3);
    root = Insert(root, 6);
}