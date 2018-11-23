#include "file.h"
#include "errno.h"
#include "util.h"
#include "disk.h"
#include "kprintf.h"
struct File file_table[MAX_FILES];
struct Inode ino;
const char block_buffer[4096];
unsigned U[1024];
#define SEEK_SET 0
#define SEEK_CUR 1
#define SEEK_END 2
#define BYTES_PER_BLOCK 4096
int file_open(const char * fname, int flags){
	int flen = kstrlen(fname);
	int i;
	int idx = 1;
	for (i = 3; i < MAX_FILES; i++){
		if (file_table[i].in_use==0){
			idx = i;
			break;
		}
	}
	if (i==MAX_FILES){
		return -EMFILE;
	}
	disk_read_inode(2,&ino);
	i = 0;
	while(ino.direct[i]!=0){
		read_block(ino.direct[i],(void*)block_buffer);
		char * p = (char *)block_buffer;
		while(1){
			struct DirEntry * de = (struct DirEntry*)p;
			if (0==kmemcmp((void*)fname,de->name,de->name_len) && flen==de->name_len){
				disk_read_inode(de->inode,&(file_table[idx].ino));
				file_table[idx].offset = 0;
				file_table[idx].in_use = 1;
				return idx;
			}
			if (de->rec_len==0){
				break;
			}
			p+=de->rec_len;
		}
		i++;
	}
	return -ENOENT;

}
int file_close(int fd){
	if (file_table[fd].in_use==0){
		return -ENOENT;		
	}
	else if(fd >= MAX_FILES){
		return -EINVAL;
	}else{
		file_table[fd].in_use = 0;
		return 0; 
	}

	
}
int file_read(int fd, void* buf, int count){
	if (fd < 0){
		return -EINVAL;
	}
	if (fd > MAX_FILES - 1){
		return -EINVAL;
	}
	struct File * fp = &file_table[fd];
	if (fp->in_use==0){
		return -ENOENT;
	}
	if (count <= 0){
		return SUCCESS;
	}
	if (fp->offset >= fp->ino.size){
		return SUCCESS;
	}
	int bi = kdiv(fp->offset, BYTES_PER_BLOCK);
	if (bi < 12){
		read_block(fp->ino.direct[bi],(void*)block_buffer);	
		int bo = kmod(fp->offset, BYTES_PER_BLOCK);
		int remaining_block = BYTES_PER_BLOCK - bo;
		int remaining_file = fp->ino.size - fp->offset;
		int smallest;
		if(count <= remaining_block && count <= remaining_file){
	    	smallest = count;
	  
		}
		else if(remaining_block <= remaining_file && remaining_block <= count){
	    	smallest = remaining_block;
	    	
		}	
		else{
	    	smallest = remaining_file;
	    	
		}
		kmemcpy(buf,(void*)block_buffer + bo,smallest);
		fp->offset += smallest;
		return smallest;
	}
	else{
		bi-=12;
		if (bi < 1024){
			read_block(fp->ino.indirect,(void*)U);
			read_block(U[bi], (void*)block_buffer);
			int bo = kmod(fp->offset, BYTES_PER_BLOCK);
			int remaining_block = BYTES_PER_BLOCK - bo;
			int remaining_file = fp->ino.size - fp->offset;
			int smallest;
			if(count <= remaining_block && count <= remaining_file){
		    	smallest = count;
		  
			}
			else if(remaining_block <= remaining_file && remaining_block <= count){
		    	smallest = remaining_block;
		    	
			}	
			else{
		    	smallest = remaining_file;
		    	
			}
			kmemcpy(buf,(void*)block_buffer + bo,smallest);
			fp->offset += smallest;
			return smallest;
		}
		else{
			bi-=1024;
			int oi = bi>>10;
			int ii = bi&0x3ff;
			read_block(fp->ino.doubleindirect, (void*)U);
			read_block(U[oi],(void*)U);
			read_block(U[ii],(void*)block_buffer);
			int bo = kmod(fp->offset, BYTES_PER_BLOCK);
			int remaining_block = BYTES_PER_BLOCK - bo;
			int remaining_file = fp->ino.size - fp->offset;
			int smallest;
			if(count <= remaining_block && count <= remaining_file){
		    	smallest = count;
		  
			}
			else if(remaining_block <= remaining_file && remaining_block <= count){
		    	smallest = remaining_block;
		    	
			}	
			else{
		    	smallest = remaining_file;
		    	
			}
			kmemcpy(buf,(void*)block_buffer + bo,smallest);
			fp->offset += smallest;
			return smallest;


		}
		



	}
	

}
int file_write(int fd, const void* buf, int count){
	return -ENOSYS;
}
int file_seek(int fd, int offset, int whence){
	if (fd < 0){
		return -EINVAL;
	}
	if (fd > MAX_FILES - 1){
		return -EINVAL;
	}
	struct File * fp = &file_table[fd];
	if (whence==SEEK_SET){
		if (offset < 0){
			return -EINVAL;
		}
		else{
			fp->offset = offset;
			return SUCCESS;
		}
	}
	if (whence==SEEK_CUR){
		if (fp->offset + offset < 0){
			return -EINVAL;
		}
		else{
			fp->offset += offset;
			return SUCCESS;
		}
	}
	if (whence==SEEK_END){
		if (offset + (int)fp->ino.size < 0){
			return -EINVAL;
		}
		else{
			fp->offset = fp->ino.size + offset;
			return SUCCESS;
		}
	}
	//kprintf("yes");
	return -EINVAL;
}