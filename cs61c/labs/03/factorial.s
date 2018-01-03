.data
n: .word 8

.text
main:
	la t0, n
    lw a0, 0(t0)
    jal ra, factorial
    
    addi a1, a0, 0
    addi a0, x0, 1
    ecall # Print Result
    
    addi a0, x0, 10
    ecall # Exit

factorial:
	addi t1, a0, x0 # Number of the factorial
	addi t2, x0, 1
	beq t1, x0, end
	mul t2, t2, t1
	addi t1, t1, -1
	jal x0, factorial
end:
	add a0, t2, x0
	jr ra

