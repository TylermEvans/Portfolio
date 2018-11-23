#include "kprintf.h"
#include "disk.h"
#include "superblock.h"
#include "blockgroupdescriptor.h"
#include "util.h"
#include "inode.h"
const char block_buffer[4096];
struct Superblock * spblock;
struct BlockGroupDescriptor * blockGroupDescriptors;
struct Inode ino;
void disk_init(){
	
	*POWER = 3;
	*CLOCK = 8;
	*CMD = (1<<10);
	*CMD = 8 | (1<<10);
	do{
		
		*CMD = 55 | (1<<10) | (1<<6);
		*ARG = 0xffffffff;
		*CMD = 41 | (1<<10) | (1<<6);
		
		
	}while(isBusy());
	*CMD = 2 | (1<<10) | (1<<6) | (1<<7);
	*CMD = 3 | (1<<10) | (1<<6); 
	unsigned relative_address = *RESPONSE;
	*ARG = relative_address;
	*CMD = 7 | (1<<10) | (1<<6);

	//read in superblock
	disk_read_block_partial(0,(void*)block_buffer,1024,1024);
	kmemcpy(spblock,(void*)block_buffer, 1024);
}
void disk_read_sector(unsigned sector, void* datablock){
	
	*DATA_LENGTH = 512;
	*DATA_TIMER = 100;
	*DATA_CONTROL = 1 | (1<<1) | (9<<4);
	*ARG = 512*sector;
	*CLEAR=0x3ff;
	*CMD = 17 | (1<<10) | (1<<6);
	unsigned* p = (unsigned*)datablock;
	int k;
	for(k=0;k<128;++k){
		while( *STATUS & (1<<19) )
			;	
		*CLEAR = 0x3ff;
		unsigned v = *DATA_FIFO;
		*p++ = v;
	}
}
void disk_write_sector(unsigned sector, void* datablock){
	*DATA_LENGTH = 512; 
	*DATA_TIMER = 100;
	*DATA_CONTROL = 1 | (9<<4);
	*ARG = 512*sector;     
	*CLEAR=0x3ff; //clear status flags
	//do the write
	*CMD = 24 | (1<<10) | (1<<6); 
	unsigned* p = (unsigned*)datablock;
	int k;
	for(k=0;k<128;++k){
    //wait until buffer is empty
		while( (*STATUS & (1<<20)) )
			;
		*CLEAR = 0x3ff;
		*DATA_FIFO = *p;
		p++;
	}	
}
void read_block(unsigned blocknum, void * p){
	int i;
	for (i=0; i < 8; i++){
		disk_read_sector((blocknum*8)+i,p+(512*i));
	}
}
int isBusy(){
    //return busy bit
    return *STATUS& (1<<24) ; 
}
void disk_read_block_partial(unsigned v1, void * p, int start, int count){
	static char buff[4096];
	int i;
	for (i=0; i < 8; i++){
		disk_read_sector((v1*8)+i,(void*)buff + (512*i));
	}
	kmemcpy(p,(void*)buff+start,count);
}
void disk_read_inode(unsigned n, struct Inode * ino){
	n--;
	int driggs = kdiv(n,spblock->inodes_per_group);
	int inodeTableStart = spblock->blocks_per_group*driggs + 4;
	int inodes_to_skip = kmod(n,spblock->inodes_per_group);
	int bytesToSkip = inodes_to_skip * sizeof(struct Inode);
	int blocks_to_skip = kdiv(bytesToSkip,4096);
	disk_read_block_partial(inodeTableStart + blocks_to_skip,ino,(kmod(n,32)) * sizeof(struct Inode),sizeof(struct Inode));
	
}
void disk_suite(){
	//read in superblock
	disk_read_block_partial(0,(void*)block_buffer,1024,1024);
	kmemcpy(spblock,(void*)block_buffer, 1024);
	
	disk_read_inode(2,&ino);
	int i;
	for (i = 0; ino.direct[i] != 0 ;i++){
		read_block(ino.direct[i],(void*)block_buffer);
		char * p = (char *)block_buffer;

		while(1){

			struct DirEntry * de = (struct DirEntry*)p;
			if (de->rec_len==0){
				break;
			}
			kprintf("<%d>  ",de->inode);
			kprintf("%.*s\n",de->name_len, de->name);
			p+=de->rec_len;
		}
	}
	//calculate num of block groups
	int block_group_num = 0;
	int total_block_num = spblock->block_count;
	while(total_block_num > 0){
		total_block_num -= spblock->blocks_per_group;
		block_group_num++;
	}
	//read in block group descriptors
	read_block(1,(void*)block_buffer);
	kmemcpy(blockGroupDescriptors,(void*)block_buffer,sizeof(struct BlockGroupDescriptor)*block_group_num);
}
