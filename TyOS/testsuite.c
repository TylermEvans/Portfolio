
#include "syscalls.h"
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char* argv[])
{

    printf("Hello, world!\n");
    printf("Random numbers: %d %d %d\n",rand(),rand(),rand());
    FILE* fp = fopen("article5.txt","r");
    if(!fp){
        printf("Cannot open!\n");
        return 0;
    }
    fflush(NULL);
    char data[32];
    while(1){
        if( 0 == fgets(data,sizeof(data),fp) ){
            printf("<EOF>");
            break;
        }
        printf("%s",data);
    }
    return 0;
}