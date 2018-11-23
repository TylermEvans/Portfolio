#pragma once

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

unsigned int timeMilli;

void timer_init();
void increment_secs();
void increment_millisecs();