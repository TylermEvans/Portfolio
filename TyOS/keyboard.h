
#pragma once
#define KEYBOARD_CTL ((volatile unsigned*) 0x18000000)
#define KEYBOARD_DATA ((volatile unsigned*) 0x18000008)
#define LINEBUF_SIZE 50
int keyboard_getline(char* buffer,int num);
void keyboard_init();
void keyboard_interrupt();
char translate_scancode(unsigned code, int press);