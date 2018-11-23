// kernelmain.c
#include "console.h"
#include "disk.h"
#include "util.h"
#include "kprintf.h"
#include "interrupt.h"
#include "kernelmain.h"
#include "file.h"
#include "disk.h"
#include "exec.h"
#include "timer.h"
#include "keyboard.h"
#include "memory.h"
#include "mouse.h"
void kmain(){
	//kmemset(&sbss, 0, &ebss-&sbss);
	console_init();
	disk_init();
	interrupt_init();
	timer_init();
	keyboard_init();
	//mouse_init();
	memory_init();
	int error = exec("testsuite.bin");
	if (error < 0){
		kprintf("error: %d", error);
	}
	while(1){
		
		
	}

}