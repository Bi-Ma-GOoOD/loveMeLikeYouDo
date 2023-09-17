#include <stdio.h>
#include <stdlib.h>

struct Node {
  int data;
  struct Node *next;
  struct Node *children;
};

int count_children(struct Node *node) {
  if (node == NULL) {
    return 0;
  } else {
    int count = 0;
    for (struct Node *child = node->children; child != NULL; child = child->next) {
      count++;
    }
    return count;
  }
}

void add_child(struct Node *node, struct Node *child) {
  if (node == NULL) {
    return;
  }

  child->next = node->children;
  node->children = child;
}

// int main() {
//   struct Node *root = malloc(sizeof(struct Node));
//   root->data = 1;
//   root->children = malloc(sizeof(struct Node));
//   root->children->data = 2;
//   root->children->next = malloc(sizeof(struct Node));
//   root->children->next->data = 3;
//   root->children->next->next = NULL;

//   struct Node *child = malloc(sizeof(struct Node));
//   child->data = 4;

//   printf("member amount of node 1 is: %d\n", count_children(root));
//   printf("member of Node 1 are\n");
//   for (struct Node *node = root->children; node != NULL; node = node->next) {
//     printf("%d\n", node->data);
//   }

//   return 0;
// }

int main(){
  int vertices, parent;

  printf("Enter vertices: ");
  scanf("%d", &vertices);

  for(int i = 0; i < vertices - 1; ++i){
    printf("Enter parent:");
    scanf("%d", &parent);
    if(i = 0){
      struct Node *root = malloc(sizeof(struct Node));
      root->data = parent;
      struct Node *child = malloc(sizeof(struct Node));
      child->data = 2;
      add_child(root,child);
    }
  }
}
