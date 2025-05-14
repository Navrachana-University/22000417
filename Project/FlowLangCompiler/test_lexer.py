# test_lexer.py
from flowlang_lexer import lexer

code = '''
let x = 10
show x
range 1 to 3 do
    show x
'''

lexer.input(code)

for token in lexer:
    print(token)
