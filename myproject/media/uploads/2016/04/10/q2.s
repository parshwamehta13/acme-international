	AREA QUES2, CODE, READONLY
	ENTRY
	LDR r0, = 0x4020; location where stored
	LDR r1, loc ; no. to be stored in r1
	STR r1,[r0] ; store value of r0 in location at r1
loc DCD 0xAEF67D90; no. to be stored
	END