%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

extern int yylex(void); 
extern int yy_scan_string(char*);
extern int yyparse();
 
/*
void yyerror(const char *str)
{
        fprintf(stderr,"error: %s\n",str);
}
*/
 
 
int yywrap()
{
        return 1;
} 
  
  
struct node 
{
    char* data;          
    struct node *next;
}*head,*tail;


struct Table 
{
    char* data;          
}*table;


void createList(char* data);
void insertNodeAtEnd(char* data);
void printList();
void tableName(char* data);


int main(int argc, char **argv)
{
    
    char input[40] = "Select col1 , col2, col3 from tab1;";
    //char input[40] = "Select * from tab1;";

    yy_scan_string (input);

    //yylex();
    yyparse();
    
    printf("TABLE: %s\n", table->data);
    printList();

    //yy_delete_buffer(input);
    
    return 0;
} 


void createList(char* data) 
{
    struct node *n1 = malloc(sizeof(struct node));
    
    n1->data = malloc(sizeof(strlen(data)+1));
    strcpy(n1->data, data);
    n1->next = NULL;
    
    head = n1;
    tail = n1;       
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



void printList() {
  struct node* ptr = head;
  while(ptr) {
    printf("COLOUMN: %s\n", ptr->data);
    ptr = ptr->next;
  }
}

void tableName(char* data)
{
  struct Table *temp = malloc(sizeof(struct Table));
  temp->data = malloc(sizeof(strlen(data)+1));
  strcpy(temp->data, data);
  
  table = temp;
  
  temp = NULL;
  free(temp);
  
  //table = malloc(sizeof(strlen(data)+1));
  //strcpy(table->data, data);
}


%}

%token SELECT FROM END STAR
%union {char *string;}
%token <string> TOK

%%

commands:   /* empty */
            | commands command
            ;

command:
            SELECT TableCommaList FROM TOK END
            {                
                tableName($4);
            }
            ;

TableCommaList:
            STAR   { createList("ALL"); }
            | TOK  { createList($1); }
            | TableCommaList ',' TOK  { insertNodeAtEnd($3); }
            ;

/*
TableCommaList:
            TOK  { printf("COLOUMN : %s\n", $1); }
            | TableCommaList ',' TOK  { printf("COLOUMN : %s\n", $3); }
            ;
*/  

%%

