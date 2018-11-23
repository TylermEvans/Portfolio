#include "keyboard.h"
#include "interrupt.h"
#include "util.h"
#include "kprintf.h"
static char linebuf[LINEBUF_SIZE];
static int linebuf_chars = 0;
static volatile int linebuf_ready=0;
int press = 0;
char last_key = -1;
unsigned last_code = -1;
int shift = 0;
int keyboard_getline(char* buffer,int num){
    while( !linebuf_ready ){
        sti(); 
        halt(); 
    }
    kmemcpy((void*)buffer,(void*)linebuf,linebuf_chars);
    linebuf_ready = 0;
    int result = linebuf_chars;
    linebuf_chars = 0;
    return result;
}
void keyboard_init(){
	*KEYBOARD_CTL = (1<<2) | (1<<4);
}
void keyboard_interrupt(){
	volatile unsigned q = *KEYBOARD_DATA;
	char ascii; 
	ascii = translate_scancode(q, 1);
	if(linebuf_ready){

	}
	else if(ascii == '\x7f'){
		if (linebuf_chars>0){
			linebuf[linebuf_chars] = ' ';
			kprintf("%c", ascii);
			linebuf_chars--;
		}
	}
	else if(ascii == '\n'){
		linebuf_ready = 1;
		kprintf("\n");
	}
	else if(linebuf_chars >= LINEBUF_SIZE){
		//DO NOTHING
	}
	else if(ascii >= 32 && ascii <= 126){
		linebuf[linebuf_chars] = ascii;
		kprintf("%c",ascii);
		linebuf_chars++;
	}
	else{
		//IGNORE
	}	
}
char translate_scancode(unsigned code, int press){
	char result = -1;
	if (last_code == 0xf0){
		if (code == 18 || code == 89){
			shift = 0;
		}
		result = 0;
	}else{
		if (code == 18 || code == 89){
			shift = 1;
		}
		if (shift){
			if (code == 22){
				result = 33;
			}
			if (code == 30){
				result = 64;
			}
			if (code == 38){
				result = 35;
			}
			if (code == 37){
				result = 36;
			}
			if (code == 41){
				result = 32;
			}
			if (code == 46){
				result = 37;
			}
			if (code == 54){
				result = 94;
			}
			if (code == 61){
				result = 38;
			}
			if (code == 62){
				result = 42;
			}
			if (code == 70){
				result = 40;
			}
			if (code == 69){
				result = 41;
			}
			if (code == 73){
				result = '>';
			}
			if (code == 76){
				result = ':';
			}
			if (code == 78){
				result = 95;
			}
			if (code == 82){
				result = '"';
			}
			if (code == 85){
				result = '+';
			}
			if (code == 84){
				result = '{';
			}
			if (code == 91){
				result = '}';
			}
		}
		else{
			if (code == 44){
				result = 't';
			}
			if (code == 90){
				result = '\n';
			}
			if (code == 102){
				result = '\x7f';
			}
			if (code == 13){
				result = '\t';
			}
			if (code == 21){
				result = 'q';
			}
			if (code == 22){
				result = '1';
			}
			if (code == 26){
				result = 'z';
			}
			if (code == 27){
				result = 's';
			}
			if (code == 28){
				result = 'a';
			}
			if (code == 29){
				result = 'w';
			}
			if (code == 30){
				result = '2';
			}
			if (code == 33){
				result = 'c';
			}
			if (code == 34){
				result = 'x';
			}
			if (code == 35){
				result = 'd';
			}
			if (code == 36){
				result = 'e';
			}
			if (code == 37){
				result = '4';
			}
			if (code == 38){
				result = '3';
			}
			if (code == 41){
				result = 32;
			}
			if (code == 42){
				result = 'v';
			}
			if (code == 43){
				result = 'f';
			}
			if (code == 44){
				result = 't';
			}
			if (code == 45){
				result = 'r';
			}
			if (code == 46){
				result = '5';
			}
			if (code == 49){
				result = 'n';
			}
			if (code == 50){
				result = 'b';
			}
			if (code == 51){
				result = 'h';
			}
			if (code == 52){
				result = 'g';
			}
			if (code == 53){
				result = 'y';
			}
			if (code == 54){
				result = '6';
			}
			if (code == 58){
				result = 'm';
			}
			if (code == 59){
				result = 'j';
			}
			if (code == 60){
				result = 'u';
			}
			if (code == 61){
				result = '7';
			}
			if (code == 62){
				result = '8';
			}
			if (code == 66){
				result = 'k';
			}
			if (code == 68){
				result = 'o';
			}
			if (code == 69){
				result = '0';
			}
			if (code == 70){
				result = '9';
			}
			if (code == 73){
				result = '.';
			}
			if (code == 75){
				result = 'l';
			}
			if (code == 76){
				result = ';';
			}
			if (code == 77){
				result = 'p';
			}
			if (code == 78){
				result = '-';
			}
			if (code == 82){
				result = ',';
			}
			if (code == 85){
				result = '=';
			}
			if (code == 84){
				result = '[';
			}
			if (code == 91){
				result = ']';
			}
		}
		
	}	

	last_code = code;
	return result;
}