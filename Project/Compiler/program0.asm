; -- header --
bits 64
default rel
; -- variables --
section .bss
; -- contants --
section .date
; -- Entry Point --
section .text
global main

main:
	PUSH rbp
	MOV rbp, rsp
	SUB rsp, 32
; -- PUSH ---
	PUSH 10
; -- PUSH ---
	PUSH 7
; --ADD ---
	POP rax
	ADD qword [rsp], rax
; -- PRINT ---
; NOT IMPLEMENTED 
; --HALT ---
	JMP EXIT_LABEL
EXIT_LABEL:
	XOR eax, eax
	MOV rsp, rbp
	POP rbp
	RET
