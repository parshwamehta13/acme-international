	AREA question5, code, READONLY
	ENTRY
		ldr r0, =0x5000 ; load a value into register r0
		ldr r1, =0x20 ; load another value into register r1
		ldr r3, =0x5012 ; load an address into register r3
		ldr r4, =0x0001 ; load a value into register r4
		ldr r5, =0x0002 ; load a value into register r5
		str r1, [r0] ; store the data in r0 to the address stored at register r1
		ands r2, r1, #1 ; and data in r1 with 1 and store it in r2
		beq label ; if zero flag is set, jump to "label"
		str r4, [r3] ; store the data in r4 to the address stored at register r3
		bal jump ; always jump to label "jump" 
label str r5, [r3]
jump nop
	END
