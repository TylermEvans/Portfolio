//console.h
#pragma once
#define CHAR_WIDTH 16
#define CHAR_HEIGHT 25
#define WIDTH 800
#define HEIGHT 600
#define pl110 ( (volatile unsigned*)0xc0000000 )
#define haxis       (*(pl110+0))    //offset 0: horizontal axis                             
#define vaxis       (*(pl110+1))    //offset 4: vertical axis                               
#define polarity    (*(pl110+2))    //offset 8: clock+polarity 
#define lineend     (*(pl110+3))    //offset 12: line end
#define baseaddr1   (*(pl110+4))    //offset 16: upper panel base address                           
#define baseaddr2   (*(pl110+5))    //offset 20: lower panel base address
#define intmask     (*(pl110+6))    //offset 24: interrupt mask
#define params      (*(pl110+7))    //offset 28: panel parameters 
#define framebuffer ((volatile unsigned char*)((0x7ffffff-(WIDTH*HEIGHT*2))&0xfffffff0))


void console_init();
void set_pixel(int x, int y, unsigned short upper, unsigned short lower);
void set_square(int x, int y, unsigned short upper, unsigned short lower);
void draw_line(int x, int y, int width, int height, unsigned short upper, unsigned short lower);
void console_draw_character(int x, int y, char ch);
void console_draw_string(int x, int y, const char* s);
void draw_inits(unsigned short upper, unsigned short lower);
void console_putc(char x);
void sweet();

