#pragma once
#define IRQ_KEYBOARD (1<<3)
#define IRQ_MOUSE (1<<4)
#define IRQ_TIMER (1<<6)
#define IRQ_STATUS ((volatile unsigned*) 0x14000000)
#define IRQ_ENABLE ((volatile unsigned*) 0x14000008)
#define IRQ_DISABLE ((volatile unsigned*) 0x1400000c)
#define TIMER_LOAD ((volatile unsigned*)0x13000100)
#define TIMER_RELOAD (TIMER_LOAD + 6)
#define TIMER_ACK (TIMER_LOAD + 3)
#define TIMER_CTL (TIMER_LOAD + 2)
#define TIMER_ONE_SHOT 1
#define TIMER_REPEATED 0
#define TIMER_16_BITS 0
#define TIMER_32_BITS 2
#define TIMER_PRESCALE_1 0
#define TIMER_PRESCALE_16 4
#define TIMER_PRESCALE_256 8
#define TIMER_DO_INTERRUPTS 32
#define TIMER_CYCLE_ONCE 0
#define TIMER_CYCLE_FOREVER 64
#define TIMER_ENABLE 128
void interrupt_init();
void handler_prefetchabort_c();
void handler_undefined_c();
void handler_fiq_c();
void handler_irq_c();
void handler_svc_c();
void handler_dataabort_c();
void handler_reset_c();
void handler_reserved_c();
void sti();
void halt();