# 22000417 - Vaidehi Hirani

# Out Little Language (OLL) Compiler

This project is a compiler for a simple language called Out Little Language (OLL)[cite: 1]. It takes OLL code as input and compiles it into assembly code, then assembles and links it to create an executable[cite: 1, 2, 3, 4].

##  Building Blocks

The compiler follows these main steps:

1.  **Tokenization:** The input OLL code is parsed into a list of tokens[cite: 1, 5, 6].
2.  **Assembly Code Generation:** The list of tokens is converted into a corresponding assembly program[cite: 2, 9, 10, 11, 12].
3.  **Assembly:** The assembly code is assembled into an object file using the `nasm` assembler[cite: 3].
4.  **Linking:** A linker (like GCC) is used to create the final executable[cite: 4].

##  Compiler (`compiler.py`)

The core of the compiler is the `compiler.py` script[cite: 6].

###   Usage

To compile an OLL program, run the `compiler.py` script from the command line, providing the OLL file as an argument:

```bash
python compiler.py program0.oll