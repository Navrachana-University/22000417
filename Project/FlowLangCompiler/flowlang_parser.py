# flowlang_parser.py
import ply.yacc as yacc
from flowlang_lexer import tokens

# Store all the parsed instructions
instructions = []

def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_let(p):
    '''statement : LET IDENTIFIER EQUALS NUMBER NEWLINE'''
    p[0] = ('let', p[2], p[4])

def p_statement_show(p):
    '''statement : SHOW IDENTIFIER NEWLINE'''
    p[0] = ('show', p[2])

def p_statement_range(p):
    '''statement : RANGE NUMBER TO NUMBER DO NEWLINE statement_list'''
    p[0] = ('range', p[2], p[4], p[7])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()
