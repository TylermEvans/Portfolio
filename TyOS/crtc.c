#include "syscalls.h"

static int syscall0(int p0){
    register unsigned r0 asm ("r0");
    r0=p0;
    asm volatile("svc #0" : "+r"(r0) : : "memory","cc");
    return r0;
}
static int syscall1(int p0, int p1){
    register unsigned r0 asm  ("r0");
    register unsigned r1 asm  ("r1");
    r0=p0;
    r1=p1;
    asm volatile("svc #0" : "+r"(r0),"+r"(r1) : : "memory","cc");
    return r0;
}
extern int fflush(void*);
extern unsigned sbss,ebss;
extern int main();
void _start(){
    //clear the bss
    char* p = (char*)&sbss;
    while(p != (char*)&ebss){
        *p=0;
        p++;
    }
    syscall1(SYSCALL_BRK, (unsigned)&ebss);
    main();
    fflush(0);
    syscall0(SYSCALL_EXIT);
}