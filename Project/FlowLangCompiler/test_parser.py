# test_parser.py
from flowlang_parser import parser
from flowlang_interpreter import execute_program

# Sample code to parse and execute
code = '''let x = 5
show x
range 1 to 3 do
    show x
'''

# Parse the code
parsed_instructions = parser.parse(code)

# Execute the parsed instructions
execute_program(parsed_instructions)
