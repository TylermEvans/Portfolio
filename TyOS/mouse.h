#pragma once
#define MOUSE_CTL ( (volatile unsigned*) 0x19000000 )
#define MOUSE_CMD ( (volatile unsigned*) 0x19000008 )
void mouse_init();
void mouse_interrupt();