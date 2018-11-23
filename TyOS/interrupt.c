#include "util.h"
#include "interrupt.h"
#include "kprintf.h"
#include "errno.h"
#include "syscalls.h"
#include "file.h"
#include "console.h"
#include "kprintf.h"
#include "timer.h"
#include "keyboard.h"
#include "mouse.h"
#include "process.h"
//enable only the interrupts we'll use
extern void* itable_start;
extern void* itable_end;
int mouse_x = 0;
int mouse_y = 0;
struct PCB process_table[MAXPROC];
int current_pid=-1;
unsigned breakpoint;
void interrupt_init(){
    kmemcpy((void*)0, itable_start, itable_end-itable_start);
    *IRQ_ENABLE= (IRQ_KEYBOARD | IRQ_MOUSE | IRQ_TIMER );
    sti();
}
void handler_prefetchabort_c(unsigned* regs){
    kprintf("EXCEPTION: Prefetch abort\n");
    kprintf("Faulting instruction at 0x%x", regs[13]);
    
    while(1){

    }
}
void handler_undefined_c(){
    kprintf("404 ERROR. Try Destroying your computer");
}
void handler_fiq_c(){
    kprintf("404 ERROR. Try Destroying your computer");
}
void handler_irq_c(){
	unsigned asserted = *IRQ_STATUS;
	if( asserted & IRQ_TIMER ){
        *TIMER_ACK = 1;    //acknowledge at timer chip
        increment_secs();
    }
    if ( asserted & IRQ_KEYBOARD ){
    	keyboard_interrupt();
    }
    if (asserted & IRQ_MOUSE){
    	mouse_interrupt();
    }

}
void handler_reserved_c(){
    kprintf("404 ERROR. Try Destroying your computer");
}
void handler_svc_c(unsigned* ptr){

	switch(ptr[0]){
		case SYSCALL_OPEN:
		{
			ptr[0] = file_open((char*)ptr[1], ptr[2]);
			break;
		}
		case SYSCALL_CLOSE:
		{
			ptr[0] = file_close(ptr[1]);
			break;
		}
		case SYSCALL_READ:
		{

			int fd = ptr[1];
		    if( fd == 0 ){
		        ptr[0] = keyboard_getline((char*)ptr[2],ptr[3]);
		    }
		    else if( fd < 3 )
		        ptr[0] = -ENOSYS;
		    else{
		        ptr[0] = file_read(fd,(void*)ptr[2],ptr[3]);
		    }
		    break;


		}
		case SYSCALL_BRK:{
			breakpoint = ptr[1];
			ptr[0] = ptr[1];
			break;
		}
		case SYSCALL_SBRK:{
			unsigned lastval = breakpoint;
			breakpoint+=ptr[1];
			ptr[0] = lastval;  
			break;
		}
		case SYSCALL_HALT:{
			halt();
		    break;
		}
		case SYSCALL_UPTIME:{
			
			ptr[0] = timeMilli;
			break;
		}
		case SYSCALL_WRITE:
		{
			//ptr[1] fd
			//ptr[2] buf
			//ptr[3] amount of stuff 
			int i;
			char * tmp = (char*)ptr[2];
			for (i = 0; i < ptr[3]; i++){
				console_putc(tmp[i]);
			}
			ptr[0] = ptr[3];
			break;
		}
		case SYSCALL_EXIT:{
			while(1){

			}
			break;
		}
		default:{
			ptr[0] = -ENOSYS;
		}
	}
}
void handler_reset_c(){
    kprintf("404 ERROR. Try Destroying your computer");
}
void handler_dataabort_c(){
    kprintf("404 ERROR. Try Destroying your computer");
    unsigned fault_address;
	asm volatile("mrc p15,0, %[reg],c6,c0,0\n" : [reg] "=r" (fault_address) );
	unsigned data_fault_status;
	asm volatile("mrc p15, 0, %[reg],c5,c0,0\n" : [reg] "=r"(data_fault_status));
}
void sti(){
    asm volatile(
        "mrs r0,cpsr\n"
        "and r0,r0,#0xffffff7f\n"
        "msr cpsr,r0" : : : "r0" 
    );
}
void halt(){
    asm volatile(
        "mov r0,#0\n"
        "mcr p15,0,r0,c7,c0,4" 
        : : : "r0"
    );
}
/*void sched_init(){
    int i;
    for (i = 0; i < MAXPROC; i++){
    	process_table[i] = VACANT;
    }
}
unsigned* get_current_pagetable(){
    unsigned x;
    asm volatile(
        "mrc p15, 0, %[reg], c2, c0, 0"
        : [reg] "=r"(x) );
    return (unsigned*)x;
}*/