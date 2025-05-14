%{
#include <stdio.h>
%}

%%

"let"   { printf("Found keyword 'let'\n"); }
[0-9]+  { printf("Found number: %s\n", yytext); }

%%

int yywrap(void) {
    return 1;  // Return 1 to indicate the end of the input
}


//int main() {
//    yylex();
//    return 0;
//}

