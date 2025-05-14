'''
Compiler for Out Little Language (.oll)
'''

import sys
import os

#read arguments
program_filepath = sys.argv[1]

print("[CMD] Parsing")
############################
#     Tokenize Program
############################

#read file lines
program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [
        line.strip()
            for line in program_file.readlines()]
    
program = []
for line in program_lines:
    parts = line.split(" ")
    opcode = parts[0]

    # check for empty line
    if opcode == "":
        continue

    # store opcode token
    program.append(opcode)

    # handle each opcode
    if opcode == "PUSH":
        # expecting a number
        number = int(parts[1])
        program.append(number)
    elif opcode == "PRINT":
        # parse string literal
        string_literal = ' '.join(parts[1:])[1:-1]
        program.append(string_literal)
    elif opcode == "JUMP.EQ.0":
        # read label
        label = parts[1]
        program.append(label)
    elif opcode == "JUMP.GT.0":
        # read label
        label = parts[1]
        program.append(label)

'''
Compile to assembly
'''

asm_filepath = program_filepath[:-4] + ".asm"
out = open(asm_filepath, "w")

out.write("""; -- header --
bits 64
default rel
""")

out.write("""; -- variables --
section .bss
""")

out.write("""; -- contants --
section .date
""")

out.write("""; -- Entry Point --
section .text
global main

main:
\tPUSH rbp
\tMOV rbp, rsp
\tSUB rsp, 32
""")



ip = 0
while ip < len(program):
    opcode = program[ip]
    ip += 1

    if opcode.endswith(":"):
        out.write(f"; -- Label ---\n")
        out.write(f"{opcode}\n")
    elif opcode == "PUSH":
        number = program[ip]
        ip += 1

        out.write(f"; -- PUSH ---\n")
        out.write(f"\tPUSH {number}\n")
    elif opcode == "POP":
        out.write(f"; -- POP ---\n")
        out.write(f"\tPOP\n")
    elif opcode == "ADD":
        out.write(f"; --ADD ---\n")
        out.write(f"\tPOP rax\n")
        out.write(f"\tADD qword [rsp], rax\n")
    elif opcode == "SUB":
        out.write(f"; -- SUB ---\n")
        out.write(f"\tPOP rax\n")
        out.write(f"SUB qword [rsp], rax\n")
    elif opcode == "PRINT":
        string_literal_index = program[ip]
        ip += 1

        out.write(f"; -- PRINT ---\n")
        out.write(f"; NOT IMPLEMENTED \n")
    elif opcode == "READ":
        out.write(f"; -- READ ---\n")
        out.write(f"; NOT IMPLEMENTED \n")
    
    elif opcode == "JUMP.EQ.0":
        label = program[ip]
        ip += 1

        out.write(f"; -- JUMP.EQ.0 ---\n")
        out.write(f"\tCMP qword [rsp], 0\n")
        out.write(f"\tJE {label}\n")
    elif opcode == "JUMP.GT.0":
        label = program[ip]
        ip += 1

        out.write(f"; --JUMP.GT.0 ---\n")
        out.write(f"\tCMP qword [rsp], 0\n")
        out.write(f"\tJG {label}\n")
    elif opcode == "HALT":
        out.write(f"; --HALT ---\n")
        out.write(f"\tJMP EXIT_LABEL\n")

out.write("EXIT_LABEL:\n")
out.write(f"\tXOR eax, eax\n")
out.write(f"\tMOV rsp, rbp\n")
out.write(f"\tPOP rbp\n")
out.write(f"\tRET\n")

out.close()

print("[CMD] Assembling")
os.system(f"nasm -f win64 {asm_filepath}")
print("[CMD] Linking")
os.system(f"gcc -o {asm_filepath[:-4] + '.exe'} {asm_filepath[:-3]+'o'}")

print("[CMD] Running")
os.system(f"{asm_filepath[:-4] + '.exe'}")