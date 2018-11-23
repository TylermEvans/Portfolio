#pragma once
#define CACHEABLE (1<<3)
#define BUFFERED (1<<2)
#define SECTION (2)
#define USER_NO_ACCESS (1<<10)
#define USER_READ_ONLY (2<<10)
#define USER_READ_WRITE (3<<10)
void memory_init();
void enable_pte_permission_check();
void set_page_table(void* p);
void invalidate_tlb();
void enable_mmu();
unsigned* get_current_pagetable();