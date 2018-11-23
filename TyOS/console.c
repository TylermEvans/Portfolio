//console.c
#include "console.h"
#include "sans.h"
#include "util.h"
volatile unsigned* serialport = (unsigned*) 0x16000000;
volatile unsigned* serialflags = (unsigned*) 0x16000018;
int x = 0;
int y = 0;
char * buff = "";

void console_init(){

	haxis = 0x3f1f3f00 | (WIDTH/4-4);
	vaxis = 0x80b6000 | (HEIGHT-1);
	polarity = 0x067f3800;
	params = 0x1829;
	baseaddr1 = (unsigned)framebuffer;    //cast
		
}

void set_pixel(int x, int y, unsigned short upper, unsigned short lower)
{
	framebuffer[ WIDTH*2*y + x*2] = upper;
	framebuffer[ WIDTH*2*y + x*2 + 1] = lower;	
}
void set_square(int x, int y, unsigned short upper, unsigned short lower){
	
	int i,j;
	for (i=0; i < CHAR_HEIGHT; i++){
		for (j=0; j < CHAR_WIDTH; j++){
			set_pixel(x+j,y+i,upper,lower);
			
		}
		
	}
	
	
}
void draw_line(int x, int y, int width, int height, unsigned short upper, unsigned short lower){
	int i,j;
	for (i = 0; i < width; i++){
		for (j = 0; j < height; j++){
			set_square(x + i,y + j,upper,lower);
		}
	}
	
	
}
void draw_inits(unsigned short upper, unsigned short lower){
	
	
	draw_line(400,300,100,5,upper,lower);
	draw_line(450,300,5,100,upper,lower);
	draw_line(520,300,90,5,upper,lower);
	draw_line(520,300,5,100,upper,lower);
	draw_line(520,350,90,5,upper,lower);
	draw_line(520,400,90,5,upper,lower);
	
	
	
	
	
}
void console_draw_character(int x, int y, char ch){

		int i,j;
		for (i = CHAR_HEIGHT; i > 0; i--){
			unsigned int Q = font_data[(int)ch][i];
			
			
			for (j = CHAR_WIDTH; j > 0; j--){
				
				unsigned int v = Q&1;
				
				Q = Q >> 1;
				if (v){
					set_pixel(j+x,i+y,0xff,0xff);
					
				}
				else{
					set_pixel(j+x, i+y, 0 , 0);
					
				}
				
				
				
			}
			
			
		}	
}
void console_draw_string(int x, int y, const char* s){
	int i;
	for (i = 0; s[i] != '\0'; i++){
		console_draw_character(x + (i*20), y, s[i]);
		
	}
}
void console_putc(char c){
	
	
	
	
	
	if (c=='\n'){
		x = 0;
		y++;
	}
	else if (c=='\r'){
		x = 0;
	}
	else if (c=='\t'){
		if (x%8==0){
			x+=8;
		}
		while (x%8!=0){
			x++;
		}
	}
	else if (c=='\x7f'){
		x--;
		set_square(x*(CHAR_WIDTH),y*(CHAR_HEIGHT),0x00,0x00);
		if (x<0){
			y--;
			x=(WIDTH/CHAR_WIDTH);
		}
	
		
	}
	else if (c=='\f'){
		x=0;
		y=0;
	}
	else if (c=='\b'){
		x--;
		if (x<=0){
			y--;
			x = (WIDTH/CHAR_WIDTH)-1;
			
		}
	}
	else{	
		
		if (x*CHAR_WIDTH>=WIDTH-CHAR_HEIGHT){
			y++;
			x = 0;
		}
		if(y*CHAR_HEIGHT>HEIGHT - CHAR_HEIGHT){
			
			kmemcpy((void*)framebuffer,(void*)framebuffer + (CHAR_HEIGHT*WIDTH*2),(WIDTH*HEIGHT*2) - (WIDTH * CHAR_HEIGHT * 2));
			kmemset((void*)framebuffer + (WIDTH * HEIGHT *2) - (WIDTH*CHAR_HEIGHT*2),'\0',WIDTH*CHAR_HEIGHT*2);
			y--;
		}
		console_draw_character(x*(CHAR_WIDTH),y*(CHAR_HEIGHT),c);
		x++;
		
		while ((*serialflags & (1<<5))){
			
		}
		*serialport = c;
	}
}





