#include "util.h"

void kmemcpy(void * dst, void * src, int num_bytes){
	char * sp = (char*)src;
	char * dp = (char*)dst;
	while(num_bytes--){
		*dp++ = *sp++;
	}
	
	
}
void kmemset(void * dst, char val, int num_bytes){
	char * dp = (char*)dst;
	while(num_bytes--){
		*dp++ = val;
		
	}
	
}
int kmemcmp(void * a, void * b, int n){
	char * ap = (char*)a;
	char * bp = (char*)b;
	while(n > 0){
		if(*ap < *bp){
			return -1;
		}
		else if (*ap > *bp){
			return 1;
		}
		n--;
		ap++;
		bp++;
	}	
	return 0;
}
int kstrlen(const char * s){
	int n = 0;
	while(*s){
		n++;
		s++;
	}
	return n;
}
int kdiv(int numpy, int dumpy){
	int TUB = 0;
	int quota = 0;
	int i;
	for (i=0; i <32; i++){
		TUB <<=1;
		if (numpy&(0x80000000>>i)){
			TUB|=1;
		}
		quota<<=1;
		if(TUB>=dumpy){
			quota|=1;
			TUB-=dumpy;
		}
	}
	return quota;
}
int kmod(int numpy, int den){
	int TUB = 0;
	int quota = 0;
	int i;
	for (i=0; i <32; i++){
		TUB <<=1;
		if (numpy&(0x80000000>>i)){
			TUB|=1;
		}
		quota<<=1;
		if(TUB>=den){
			quota|=1;
			TUB-=den;
		}

	}
	return TUB;
}