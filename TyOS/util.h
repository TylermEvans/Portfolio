
#pragma once
void kmemcpy(void * dst, void * src, int num_bytes);
void kmemset(void * dst, char val, int num_bytes);
int kmemcmp(void * a, void * b, int n);
int kstrlen(const char *);
int kdiv(int numpy, int den);
int kmod(int numpy, int den);
