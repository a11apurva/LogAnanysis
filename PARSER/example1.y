%{
#include <stdio.h>
#include <string.h>
 
void yyerror(const char *str)
{
        fprintf(stderr,"error: %s\n",str);
}
 
int yywrap()
{
        return 1;
} 
  
main()
{
        yyparse();
} 

%}

%token SELECT FROM END TOK

%%

commands:   /* empty */
            | commands command
            ;

command:
            SELECT TableCommaList FROM TOK END
            {
                
                printf("TABLE : %s\n", $4);
            }
            ;
        
TableCommaList:
            Table
            | TableCommaList ',' Table
            ;
    
Table:
            TOK
            {
                printf("COLOUMN : %s\n", $1);
            }
            ;

%%

