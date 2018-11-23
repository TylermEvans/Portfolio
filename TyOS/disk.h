#pragma once
#include "superblock.h"
#include "blockgroupdescriptor.h"
#include "inode.h"
#define MMCP_START ((volatile unsigned*) 0x1c000000 ) 
#define POWER ( MMCP_START)
#define CLOCK (MMCP_START+1)
#define ARG (MMCP_START+2)
#define CMD (MMCP_START+3)
#define RESPONSE_CMD (MMCP_START+4)
#define RESPONSE (MMCP_START+5)
#define DATA_TIMER (MMCP_START+9)
#define DATA_LENGTH (MMCP_START+10)
#define DATA_CONTROL (MMCP_START+11)
#define DATA_COUNTER (MMCP_START+12)
#define STATUS (MMCP_START+13)
#define CLEAR (MMCP_START+14)
#define INTERRUPT0_MASK (MMCP_START+15)
#define INTERRUPT1_MASK (MMCP_START+16)
#define SELECT (MMCP_START+17)
#define FIFO_COUNT (MMCP_START+18)
#define DATA_FIFO (MMCP_START+32)
void disk_init();
void disk_read_sector(unsigned sector, void* datablock);
void disk_write_sector(unsigned sector, void* datablock);
void read_block(unsigned blocknum, void* p);
int isBusy();
void disk_suite();
void disk_read_block_partial(unsigned v1, void * p, int start, int count);
void disk_read_inode(unsigned n, struct Inode * ino);
unsigned get_file_inode(unsigned dir_inode, const char * fname);
