//Delete Node At Point
#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *next;
};
Node *head;
void Insert(int data)
{
    Node *temp3 = new Node();
    temp3->data = data;
    temp3->next = head;
    head = temp3;
}
void Print()
{
    while(head != NULL)
    {
        cout << "In List:  " << head->data << endl;
        head = head->next;
    }
}
//Delete node at position n
void Remove(int data)
{
    Node *temp1 = head;
    if(data== 1)
    {
        head = temp1->next; // head now points to second node.
        delete(temp1);
        return;
    }
    for(int i = 0; i < data-2; i++)
    {
        temp1 = temp1->next;
    }
    // temp1 points to (n-1)th node
    Node *temp2 = temp1 -> next; // nth Node
    temp1->next = temp2->next;//(n+1)th Node
    delete(temp2); // delete temp2
}

int main()
{
    head = NULL; // empty list
    Insert(2);
    Insert(4);
    Insert(6);
    Insert(5); // List: 2, 4, 6, 5
    int n;
    cout << "Enter a position: " << endl;
    cin >> n;
    Remove(n);
    Print();
}