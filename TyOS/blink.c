#include "blink.h"
int main(int argc, char* argv[])
{   
    int i,j;
    while(1){
        for(i=0;i<HEIGHT;++i){
            for(j=0;j<WIDTH;++j){
                 screen[WIDTH*2*i + j*2] = 0x1f;
                 screen[ WIDTH*2*i + j*2 + 1] = 0x00;
                 int t;
                 for (t = 0; t < 10000; t++){

                 }
            }
        }
        asm volatile("bkpt");
    }
    return 0;
}