# flowlang_lexer.py
import ply.lex as lex

# List of token names
tokens = (
    'LET',
    'IDENTIFIER',
    'EQUALS',
    'NUMBER',
    'SHOW',
    'RANGE',
    'TO',
    'DO',
    'NEWLINE',
)

# Reserved words mapping
reserved = {
    'let': 'LET',
    'show': 'SHOW',
    'range': 'RANGE',
    'to': 'TO',
    'do': 'DO'
}

# Regular expression rules
t_EQUALS = r'='

# A token for identifiers (variable names)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# A token for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Handle newlines (as a token, important for our parser)
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
