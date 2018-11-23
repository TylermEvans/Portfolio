 #pragma once
 #define screen ((volatile unsigned char*)((0x7ffffff-(WIDTH*HEIGHT*2))&0xfffffff0))
 #define WIDTH 800
 #define HEIGHT 600