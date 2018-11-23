//my first kernel! :-)
	
	ldr sp,=stack
	b kmain
	
.section .data


	.rept 1024
	.word 42
	.endr
stack: