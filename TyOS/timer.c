#include "timer.h"
#include "interrupt.h"
#include "util.h"

void timer_init() {
	timeMilli = 0;

    *IRQ_ENABLE= (IRQ_KEYBOARD | IRQ_MOUSE | IRQ_TIMER );
    *TIMER_LOAD = 1000;  
    *TIMER_RELOAD = 1000;   
    *TIMER_ACK = 1;
    *TIMER_CTL = TIMER_ENABLE 
            | TIMER_CYCLE_FOREVER 
            | TIMER_DO_INTERRUPTS 
            | TIMER_PRESCALE_1 
            | TIMER_32_BITS;
}

void increment_secs() {
	timeMilli += 1000;
}

void increment_millisecs() {
	timeMilli++;
}