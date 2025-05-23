# 22000417 - Vaidehi Hirani

# Out Little Language (OLL) Interpreter (Simple Version)

This project implements a basic interpreter for a simplified version of the Out Little Language (OLL). It demonstrates fundamental concepts of lexical analysis (scanning) and parsing.

## Overview

This interpreter takes OLL code as input and performs the following steps:

1.  **Lexical Analysis (Scanning):** The `oll.l` file defines the lexical rules for the OLL language. It identifies tokens such as keywords (`let`), numbers, and potentially identifiers (though identifier recognition is basic in this version).
2.  **Syntax Analysis (Parsing):** The `oll.y` file defines the grammar of the OLL language. It uses the tokens generated by the lexer to understand the structure of the OLL program.
3.  **Intermediate Representation (Implicit):** While not explicitly creating a separate intermediate representation, the parser takes actions based on the recognized grammar rules, such as printing instructions like `STORE`, `PUSH`, `LOAD`, and `ADD`.
4.  **Execution (Conceptual):** This version primarily focuses on parsing and generating a sequence of conceptual instructions rather than actual execution.

## Files

* **`main.c`:** This is the main program file. It handles command-line arguments, opens the input OLL file, sets up the lexer's input stream, calls the parser (`yyparse`), and manages file closing.
* **`oll.l`:** This file contains the Flex (Fast Lexical Analyzer) code that defines the lexical rules for the OLL language. It specifies how the input text is broken down into tokens.
* **`oll.y`:** This file contains the Bison (GNU Parser Generator) code that defines the grammar of the OLL language. It describes the valid syntax of OLL programs and the actions to be taken upon recognizing grammatical structures.
* **`test.oll`:** This is a sample OLL program used for testing the interpreter.

## Building and Running

To build and run this interpreter, you'll need to have Flex and Bison installed on your system. Here are the general steps:

1.  **Generate Lexer and Parser Code:**
    ```bash
    flex oll.l
    bison -d oll.y
    ```
    This will generate `lex.yy.c` (the lexer source code) and `oll.tab.c` and `oll.tab.h` (the parser source code and header file).

2.  **Compile the Interpreter:**
    ```bash
    gcc main.c lex.yy.c oll.tab.c -o oll_interpreter
    ```

3.  **Run the Interpreter:**
    ```bash
    .\oll_interpreter test.oll
    ```
    This will parse the `test.oll` file and print the actions defined in the parser rules to the console.

## OLL Language Features (as implemented)

This simple version of OLL currently supports:

* **Variable Declaration and Assignment:** Using the `let` keyword to declare variables and the `=` operator for assignment.
* **Integer Literals:** Numerical values.
* **Basic Arithmetic:** Addition using the `+` operator.
* **Statements:** Statements are terminated by a semicolon (`;`).

## `test.oll` Example

```oll
let x = 5;
let y = 10;
let z = x + y;