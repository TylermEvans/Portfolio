#pragma once

struct PCB {
    int state;    
    //r0-r12
    unsigned registers[13];
    unsigned sp;    //r13
    unsigned lr;    //r14
    unsigned pc;    //r15
    unsigned cpsr;
    unsigned pagetable[4096] __attribute__((aligned(16384)));
    struct File* fds[MAX_FILES];    //TODO: Use this
} ;
#define MAXPROC 16
#define VACANT 0
#define READY 1
#define RUNNING 2
#define SLEEPING 3
void sched_init();