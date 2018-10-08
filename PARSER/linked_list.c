#include <stdio.h>
#include <stdlib.h>


struct node 
{
    char* data;          
    struct node *next;
}*head, *tail;


void createList(char* data);
void insertNodeAtEnd(char* data);
void displayList();
void printList();


int main()
{
  createList("abc");
  insertNodeAtEnd("def");
  //displayList();
  printList();
}


void createList(char* data) 
{
    struct node *n1 = malloc(sizeof(struct node));
    
    n1->data = malloc(sizeof(strlen(data)+1));
    strcpy(n1->data, data);
    n1->next = NULL;
    
    head = n1;
    tail = n1;    
    
    //return n1;    
}


void insertNodeAtEnd(char* data)
{
    struct node *temp = malloc(sizeof(struct node));
    
    temp->data = malloc(sizeof(strlen(data)+1));
    strcpy(temp->data, data);
    temp->next = NULL;
    
    tail->next=temp;    
    tail = temp;
    
    temp = NULL;
    free(temp);
}


void displayList()
{
    struct node *temp;

    if(head == NULL)
    {
        printf("List is empty.");
    }
    else
    {
        temp = head;
        while(temp != NULL)
        {
            printf("Data = %c\n", temp->data); 
            temp = temp->next;                 
        }
    }
}


void printList() {
  struct node* ptr = head;
  while(ptr) {
    printf("Data: %s\n", ptr->data);
    ptr = ptr->next;
  }
}