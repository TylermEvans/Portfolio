#pragma once
#include "inode.h"
#define MAX_FILES 16
struct File{
	int in_use;
	struct Inode ino;
	int flags;
	int offset;
};
int file_open(const char * fname, int flags);
int file_close(int fd);
int file_read(int fd, void* buf, int count);
int file_write(int fd, const void* buf, int count);
int file_seek(int fd, int offset, int whence);