#include "memory.h"
#include "kprintf.h"

unsigned page_table[4096] __attribute__((aligned(16384)));
void memory_init(){
	int i;
	for (i = 0; i < 4096; i++){
		page_table[i] = (i<<20);
		page_table[i] |= SECTION;
		if (i < 4 || i > 127){
			page_table[i] |= USER_NO_ACCESS;
		}
		else{
			page_table[i] |= USER_READ_WRITE;
		}
		page_table[i] |= (1<<4);
		if (i < 127){
			page_table[i] |= CACHEABLE;
			page_table[i] |= BUFFERED;
		}
	}
	enable_pte_permission_check();
	set_page_table((void*)page_table);
	enable_mmu();
}	
void enable_pte_permission_check(){
    asm volatile(
        "mcr p15,0,%[reg],c3,c0,0"
        :   //no outputs 
        : [reg] "r" (0x55555555)    //inputs
    );
} 
void set_page_table(void* p){
    asm volatile(
        "mcr p15, 0, %[reg], c2, c0, 0"
        : 
        : [reg] "r"(p) 
    );
    invalidate_tlb();
}
void invalidate_tlb(){
    asm volatile(
        "mcr p15,0,%[reg],c8,c5,0\n"  //instruction tlb
        "mcr p15,0,%[reg],c8,c6,0\n"  //data tlb
        "mcr p15,0,%[reg],c8,c7,0\n"  //unified tlb
        :  : [reg]"r"(0) );
}
void enable_mmu(){
    asm volatile(
        "mrc p15,0,r0,c1,c0,0\n"
        "orr r0,r0,#1\n"
        "mcr p15,0,r0,c1,c0,0\n"
        :   //no inputs
        :   //no outputs
        : "r0" //clobbers
    );
}