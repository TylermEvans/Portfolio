#pragma once
#define va_start(L,x) real_va_start(&L,&x,sizeof(x))
#define va_arg(L, T) (*((T*)real_va_arg(&L,sizeof(T))))
typedef struct _va_list{
	char * q;
}va_list;
static void real_va_start(va_list * v, void*p, int size ){
	char * c = (char*)p;
	v->q = c+size;
	
}
static void* real_va_arg(va_list * v, int size){
	char * tmp = v->q;
	v->q+=size;
	return tmp;
}
static void va_end(){
	
}
