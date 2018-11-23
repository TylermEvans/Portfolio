.section .text
    .global itable_start, itable_end
itable_start:
.word itable
itable:
    ldr pc, handler_reset_address
    ldr pc, handler_undefined_address
    ldr pc, handler_svc_address
    ldr pc, handler_prefetchabort_address
    ldr pc, handler_dataabort_address
    ldr pc, handler_reserved_address
    ldr pc, handler_irq_address
    ldr pc, handler_fiq_address
handler_reset_address: 
    .word handler_reset
handler_undefined_address:
    .word handler_undefined
handler_svc_address:
    .word handler_svc
handler_prefetchabort_address:
    .word handler_prefetchabort
handler_dataabort_address:
    .word handler_dataabort
handler_reserved_address:
    .word handler_reserved
handler_irq_address:
    .word handler_irq
handler_fiq_address:
    .word handler_fiq
itable_end:
.word .

handler_reset:
    ldr sp,=pfa_stack
    sub lr,lr,#4
    push {lr}
    push {r0-r12}
    bl handler_reset_c
    pop {r0-r12}
    ldm sp!, {pc}^
    b forever
handler_undefined:
    ldr sp,=pfa_stack
    sub lr,lr,#4
    push {lr}
    push {r0-r12}
    bl handler_undefined_c
    pop {r0-r12}
    ldm sp!, {pc}^
    b forever
handler_svc:
    ldr sp,=svc_stack
    push {lr}
    push {r0-r12}
    mov r0,sp
    bl handler_svc_c
    pop {r0-r12}
    ldm sp!, {pc}^
handler_prefetchabort:
    ldr sp,=pfa_stack
    sub lr,lr,#4
    push {lr}
    push {r0-r12}
    mov r0,sp
    bl handler_prefetchabort_c
    pop {r0-r12}
    ldm sp!, {pc}^
    b forever
handler_dataabort:
    ldr sp,=pfa_stack
    sub lr,lr,#4
    push {lr}
    push {r0-r12}
    mov r0,sp
    bl handler_dataabort_c
    pop {r0-r12}
    ldm sp!, {pc}^
    b forever
handler_reserved:
    ldr sp,=pfa_stack
    sub lr,lr,#4
    push {lr}
    push {r0-r12}
    bl handler_reserved_c
    pop {r0-r12}
    ldm sp!, {pc}^
    b forever
handler_irq:
    ldr sp,=irq_stack
    sub lr,lr,#4
    push {lr}
    push {r0-r12}
    bl handler_irq_c
    pop {r0-r12}
    ldm sp!, {pc}^
    b forever
handler_fiq:
    ldr sp,=pfa_stack
    sub lr,lr,#4
    push {lr}
    push {r0-r12}
    bl handler_fiq_c
    pop {r0-r12}
    ldm sp!, {pc}^
    b forever
forever:
    b forever

.section .data


    .rept 1024
    .word 0
    .endr
pfa_stack:
    .rept 1024
    .word 0
    .endr
svc_stack:
    .rept 1024
    .word 0
    .endr
und_stack:
    .rept 1024
    .word 0
    .endr
irq_stack:
