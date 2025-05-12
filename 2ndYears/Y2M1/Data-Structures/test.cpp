#include <iostream>
using namespace std;

/* structure for a node */
struct Node
{
	int data;
	struct Node *next;
};

/* Function to insert a node at the beginning of a linked list */
void insertNum(struct Node **start_ref, int data);
/* Function to bubble sort the given linked list */
void sortBubble(struct Node *start);
/* Function to swap data of two nodes a and b*/
void swap(struct Node *a, struct Node *b);
/* Function to print nodes in a given linked list */
void printList(struct Node *start);

int main()
{
	struct Node *start = NULL;
	int value;

	while(1){
		cin >> value;
		if(value == -1) {break;}
		else{
			insertNum(&start, value);
		}
	}

	sortBubble(start);
	cout << endl;
	printList(start);
}


void insertNum(struct Node **start_ref, int data)
{
	Node *ptr1 = new Node();
	ptr1->data = data;
	ptr1->next = *start_ref;
	*start_ref = ptr1;
}

void printList(struct Node *start)
{
	struct Node *temp = start;
	cout << endl;
	while (temp!=NULL)
	{
		cout << " " << temp->data << endl;
		temp = temp->next;
	}
}

void sortBubble(struct Node *start)
{
	int swapped, i;
	struct Node *ptr1;
	struct Node *lptr = NULL;

	/* Checking for empty list */
	if (start == NULL)
		return;

	do
	{
		swapped = 0;
		ptr1 = start;

		while (ptr1->next != lptr)
		{
			if (ptr1->data > ptr1->next->data)
			{
				swap(ptr1, ptr1->next);
				swapped = 1;
			}
			ptr1 = ptr1->next;
		}
		lptr = ptr1;
	}
	while (swapped);
}

void swap(struct Node *a, struct Node *b)
{
	int temp = a->data;
	a->data = b->data;
	b->data = temp;
}