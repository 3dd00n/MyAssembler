op = {'and':'00000',
	'cand':'00000',
	'or':'00000',
	'xor':'00000',
	'add':'00001',
	'nadd':'00001',
	'seq':'00001', 
	'slt':'00001', 

	'andi':'00100', 
	'candi':'00101', 
	'ori':'00110', 
	'xori':'00111', 
	'addi':'01000', 
	'naddi':'01001', 
	'seqi':'01010', 
	'slti':'01011', 

	'sll':'01100', 
	'srl':'01101', 
	'sra':'01110', 
	'ror':'01111',

	'beq':'10000', 
	'bne':'10001', 
	'blt':'10010', 
	'bge':'10011',

	'lw':'10100', 
	'sw':'10101', 

	'jalr':'11011', 
	'j':'11100', 
	'jal':'11101', 
	'imm':'11110'}

fun = {'and':'00', 
	'cand':'01',
	'or':'10',
	'xor':'11',
	'add':'00',
	'nadd':'01',
	'seq':'10',
	'slt':'11'}

reg = {'r0':'000', 
	'r1':'001', 
	'r2':'010', 
	'r3':'011', 
	'r4':'100', 
	'r5':'101', 
	'r6':'110', 
	'r7':'111'}

file_name = input('enter file name: ')
file = open(file_name, 'r')

lines = file.readlines() # return list of all lines in file
lines[-1] += '\n'
file.close()

line_counter = 1
for line in lines:

	if(line == '\n'): # skip empty lines
		continue
	elif(line[0] == '#'): # skip comment lines
		continue

	line = line[:-1] # remove \n

	line = line.split(" ", 1) # return list with two elements -> [instruction, args]
	inst = line[0] # instruction

	line[1] = line[1].replace(" ", "") # remove spaces
	args = line[1].split(',') # return list of arguments
	print(args)

	bin_inst = '' + op[inst] # instruction in binary

	if(op[inst] == '00000' or op[inst] == '00001'): # R-type: op, reg, reg, reg
		bin_inst += reg[args[0]]
		bin_inst += reg[args[1]]
		bin_inst += reg[args[2]]
		bin_inst += fun[inst]

	elif(op[inst] == '11100' or op[inst] == '11101' or op[inst] == '11110'): # J-type: op, imm11
		bin_inst += args[0]

	else: # I-type: op, reg, reg, imm5
		bin_inst += reg[args[0]]
		bin_inst += reg[args[1]]
		bin_inst += args[2]

	#print(bin_inst)

	hex_inst = '' # instruction in hex
	hex_inst += hex(int(bin_inst[0:4], 2))[2:]
	hex_inst += hex(int(bin_inst[4:8], 2))[2:]
	hex_inst += hex(int(bin_inst[8:12], 2))[2:]
	hex_inst += hex(int(bin_inst[12:16], 2))[2:]
	

	print(str(line_counter) + '.' + hex_inst)
	line_counter += 1