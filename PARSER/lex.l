%{
#include <stdio.h>
#include "ytab.h"
%}

%%
select        return SELECT;
from          return FROM;
[;]           return END;
[*]           return STAR;
\n            /* ignore end of line */;
[ \t]+        /* ignore whitespace */;
[a-zA-Z0-9]+  yylval=strdup(yytext); return TOK;
.             return (int) yytext[0];
%%
