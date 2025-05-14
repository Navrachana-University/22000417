# run_compiler.py

from flowlang_lexer import lexer
from flowlang_parser import parser, intermediate_code
from flowlang_interpreter import run_interpreter

def compile_flowlang(code):
    # Step 1: Tokenize the code
    intermediate_code.clear()
    lexer.input(code)
    tokens = list(lexer)
    print("Tokens:")
    for token in tokens:
        print(token)

    # Step 2: Parse the code
    print("\nParsing...")
    parser.parse(code, lexer=lexer)
    print("\nIntermediate Code:")
    for line in intermediate_code:
        print(line)

    # Step 3: Execute the intermediate code
    run_interpreter()

# Test with an example FlowLang code snippet
if __name__ == '__main__':
    sample_code = '''
    flow {
        let x = 5
        let y = range(1 to 5)
        do {
            show "hello"
            let x = x + 1
        } until (x == 10)
    }

    '''

    compile_flowlang(sample_code)
