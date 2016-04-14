	area ques4, code, readonly
	entry
	ldr r0, = 9
	ldr r1, = 8
	ldr r2, = 0x0010
	ldr r3, = 0x0020
	ldr r4, = 0x0001
	str r0,[r2]
	str r1,[r3]
	mov  r4,r0
	mov  r0,r1
	mov	r1,r4
	str 	r0,[r2]
	str 	r1,[r3]
	end