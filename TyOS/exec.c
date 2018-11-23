#include "exec.h"
#include "file.h"
#include "errno.h"
#include "util.h"
unsigned startup_code[] = {
    0xe10f0000,        //mrs     r0, CPSR
    0xe3c0001f,        //bic     r0, r0, #31
    0xe3800010,        //orr     r0, r0, #16
    0xe129f000,        //msr     CPSR_fc, r0
    0xe3a0d502,        //mov     sp, #8388608    ; 0x800000
};
int exec(const char* filename){
	 /*int fd = file_open(filename,0);
	 if (fd!=0){
	 	return -ENOENT;
	 }
	 else{
	 	
	 	int i = 0;
	 	int result = file_read(fd, (void*)0x400000, 100);
	 	i+=result;
	 	while(result!=0){
	 		result = file_read(fd, (void*)0x400000+i, 100);
	 		i+=result;
	 	}	 	
	 }
	 file_close(fd);
	 kmemcpy( (char*) 0x400000, startup_code, sizeof(startup_code) );
	 asm volatile("mov pc,%[reg]" : : [reg] "r" (0x400000));
	 return 0;*/
	 /*int pid;
	 int i;
	 for (i = 0; i < MAXPROC; i++){
	 	if (process_table[i] == VACANT){
	 		pid = i;
	 	}
	 	else{
	 		return -EAGAIN;
	 	}
	 }
	struct PCB * P = &process_table[pid];
	kmemset(P, 0, size(PCB) * MAXPROC);
	for (i = 0: i < 4096; i++){
		P->page_table[i] = 0;
	}

	int fd = file_open(filename);
	if (fd < 0){
		return fd;
	}*/
	int fd = file_open(filename,0);
	 if (fd < 0){
	 	return fd;
	 }
	 else{
	 	
	 	int i = 0;
	 	int result = file_read(fd, (void*)0x400000, 100);
	 	i+=result;
	 	while(result!=0){
	 		result = file_read(fd, (void*)0x400000+i, 100);
	 		i+=result;
	 	}	 	
	 }
	 file_close(fd);
	 kmemcpy( (char*) 0x400000, startup_code, sizeof(startup_code) );
	 asm volatile("mov pc,%[reg]" : : [reg] "r" (0x400000));
	 return 0;
}