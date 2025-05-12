#include <stdio.h>
#include <stdlib.h>

// Define the structure of a tree node
struct TreeNode {
    int value;
    struct TreeNode* left;
    struct TreeNode* right;
};

struct TreeNode* createNode(int value) {
    struct TreeNode *newNode = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    newNode->value = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

struct TreeNode *insert(struct TreeNode *root, int value) {
    struct TreeNode *new_node;

    if (root == NULL) {
        new_node = malloc(sizeof(struct TreeNode));
        if (new_node == NULL) {
            return NULL;
        }

        new_node->value = value;
        new_node->left = NULL;
        new_node->right = NULL;

        return new_node;
    }

    if (value < root->value) {
        root->left = insert(root->left, value);
    } else if (value >= root->value) { 
        root->right = insert(root->right, value);
    }

    return root;
}


// Preorder traversal: Root -> Left -> Right
void preorderTraversal(struct TreeNode* root) {
    if (root == NULL) {
        return;
    }

    printf("%d ", root->value);
    preorderTraversal(root->left);
    preorderTraversal(root->right);
}

// Inorder traversal: Left -> Root -> Right
void inorderTraversal(struct TreeNode* root) {
    if (root == NULL) {
        return;
    }

    inorderTraversal(root->left);
    printf("%d ", root->value);
    inorderTraversal(root->right);
}

// Postorder traversal: Left -> Right -> Root
void postorderTraversal(struct TreeNode* root) {
    if (root == NULL) {
        return;
    }

    postorderTraversal(root->left);
    postorderTraversal(root->right);
    printf("%d ", root->value);
}

int main() {
    int N;
    scanf("%d", &N);

    struct TreeNode* root = NULL;

    for (int i = 0; i < N; i++) {
        int value;
        scanf("%d", &value);
        root = insert(root, value);
    }

    preorderTraversal(root);
    printf("\n");
    postorderTraversal(root);
    printf("\n");
    inorderTraversal(root);


    return 0;
}