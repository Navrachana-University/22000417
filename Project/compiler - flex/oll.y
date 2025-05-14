%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void yyerror(char *s);
int yylex();

typedef struct {
    char *id;
    int value;
} Symbol;

Symbol symbol_table[100];
int symbol_count = 0;

Symbol* find_or_create_symbol(char *name) {
    for (int i = 0; i < symbol_count; i++) {
        if (strcmp(symbol_table[i].id, name) == 0) {
            return &symbol_table[i];
        }
    }
    symbol_table[symbol_count].id = strdup(name);
    symbol_table[symbol_count].value = 0;
    return &symbol_table[symbol_count++];
}

%}

%union {
    int num;
    char *id;
}

%token <num> NUM
%token <id> ID
%token LET ASSIGN ADD SEMICOLON
%type <num> expression

%right ASSIGN  // Assign has right-to-left associativity
%left ADD      // Addition has left-to-right associativity

%%

program:
    program statement
    |
    ;

statement:
    LET ID ASSIGN expression SEMICOLON {
        printf("STORE %s\n", $2);
    }
    ;

expression:
    NUM {
        printf("PUSH %d\n", $1);
        $$ = $1;
    }
    | ID {
        printf("LOAD %s\n", $1);
    }
    | expression ADD expression {
        printf("ADD\n");
    }
    ;

%%

void yyerror(char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
