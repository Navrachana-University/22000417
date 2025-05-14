#include <stdio.h>

extern int yyparse();

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    FILE *f = fopen(argv[1], "r");
    if (!f) {
        perror("File opening failed");
        return 1;
    }

    extern FILE *yyin;
    yyin = f;

    printf("[CMD] Parsing...\n");
    yyparse();
    fclose(f);

    return 0;
}
