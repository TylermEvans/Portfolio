#include "mouse.h"
#include "kprintf.h"
//static int i = 0;
void mouse_init(){
	*MOUSE_CTL = (1<<2) | (1<<4);
	*MOUSE_CMD = 0xf6;
	*MOUSE_CMD = 0xf4;
}
void mouse_interrupt(){
	/*volatile unsigned data = *MOUSE_CMD;
	kprintf("mouse stuff: %d", i);
	i++;*/
}