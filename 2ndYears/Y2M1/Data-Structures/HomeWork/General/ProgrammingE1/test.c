#include <stdio.h>
#include <stdlib.h>

struct Node {
  int data;
  struct Node *children;
  struct Node *next;
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

struct node *sof(struct Node *node, struct Node *child) {
  if (node == NULL) {
    return 0;
  }

  child->next = node->children;
  node->children = child;
}

int main() {
  struct Node *root = malloc(sizeof(struct Node));
  root->data = 1;
  root->children = malloc(sizeof(struct Node));
  root->children->data = 2;
  root->children->next = malloc(sizeof(struct Node));
  root->children->next->data = 3;
  root->children->next->next = NULL;

  struct Node *child = malloc(sizeof(struct Node));
  child->data = 4;

  add_child(root, child);

  printf("จำนวนลูกของ Node 1 คือ %d\n", count_children(root));
  printf("รายการลูกของ Node 1 คือ\n");
  for (struct Node *node = root->children; node != NULL; node = node->next) {
    printf("%d\n", node->data);
  }

  return 0;
}

