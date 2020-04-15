// Linked list Sum.c
#include<stdio.h>
#include<stdlib.h>
struct Node 
{
  int data;
  struct Node *next;
};
// struct Node* AddTwoNummbers(struct Node* list1,struct Node* list2)
// {
//   return list1;
// }
void insertAtEnd(struct Node *head, int value)
{
  struct Node *newNode;
  newNode = malloc(sizeof(struct Node));
  newNode->data = value;
  newNode->next = NULL;

  struct Node *temp = head;
  while (temp->next != NULL)
  {
    temp = temp->next;
  }
  temp->next = newNode;
}
int main()
{
  struct Node list1,list2,*newnode,*p;
  int i,val;
  for (i = 0; i < 3;i++)
  {
    scanf("%d",&val);
    insertAtEnd(&list1, val);
  }
  p->next = NULL;
  // for (p = list1; p->next!=NULL; p++)
  // {
  //   printf("%d", p->data);
  // }
  return 0;
}
