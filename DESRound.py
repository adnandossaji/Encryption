# Adnan Dossaji
# CSC 333

def int_bin(integar, bits):
	return bin(integar)[2:].zfill(bits)

def str_int(string):
	return int(string, 2)

def s_box(six_bits, sbox_num):
	if six_bits == 0:
		six_bits = "000000"
	elif six_bits == 1:
		six_bits = "000001"
	else:
		if type(six_bits) == int:
			six_bits = int_bin(six_bits, 4)
		else: six_bits = str(six_bits)

	sbox = [
		# S1
		[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
		 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
		 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
		 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

		# S2
		[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
		 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
		 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
		 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

		# S3
		[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
		 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
		 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
		 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

		# S4
		[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
		 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
		 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
		 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

		# S5
		[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
		 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
		 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
		 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

		# S6
		[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
		 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
		 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
		 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

		# S7
		[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
		 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
		 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
		 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

		# S8
		[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
		 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
		 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
		 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]],
	]


	row = six_bits[0] + six_bits[-1]
	col = six_bits[1:-1]

	row = int(row, 2)
	col = int(col, 2)

	#ONLY ON S2
	bin_output = sbox[sbox_num-1][row][col]
	bin_output = bin(bin_output)[2:].zfill(4)

	return bin_output

def init_permutation(bits):

	# use initial permutation table to swap bits around

def final_permutation(bits):

	# use final permutation table to swap bits around

def f(bits, key):
	# expand 32 bits passed to 48 bits by duplicating 16 bits

	# XOR 48 bits with 48 bit key
	# ex. key ^ bits

	# break 48 bits into chunks of 6 bits
	# 8 chunks

	# run each chunk through s_box
	# chunk_0 = s_box(chunk, 0)
	# chunk_1 = s_box(chunk, 1)
	# chunk_2 = s_box(chunk, 2)
	# chunk_3 = s_box(chunk, 3)
	# chunk_4 = s_box(chunk, 4)
	# chunk_5 = s_box(chunk, 5)
	# chunk_6 = s_box(chunk, 6)
	# chunk_7 = s_box(chunk, 7)

	# put 4 bit chunks back together

	# 32 bits

	# permutate 32 bits

	# return 32 bits


def get_new_key(bits):

	# 56 bits are transformed
	# 56 bits are split into 28 bit halves
	# for rounds 1, 2, 9, 16 the two halves are each rorated left by one bit
	# for all other rounds the two halves are each rorated left by two bits
	# put two halves back together
	# permutate 56 bits into 48 bits

	# return triple of two halves and 48 bits key (half0, half1, key)

def get_key_schedule(key):
	# key is converted into 64 bits

	# key does a parody check over the last 8 bits
	# and checks if the last bit is 0 and 1 based
	# on the summation of bits that equal 1

	# 56 bits remain

	# run these lines of code 16 times
		# run get_new_key(bits)
		# save key
		# put halves back together and pass into next run of get_new_key


	# save key n...16 which are 48 bits in list length 16

	# return key_schedule_list


def DES(key, plaintext):
	# run get key schedule over key and get 16 keys
	# Convert plaintext to 64 bits

	# run initial permutation over 64 bits

	# run DESRound over permutated 64 bits n...15 times and pass key n

	# run final permutation over bits

	# return ciphertext


def DESRound(new_key, text_input=None, L=None, R=None): # returns a triple (text_input, L, R)
		# if text_input != none
			# split text_input 64 bits into L = 32 bits, R = 32 bits
		# elif L != None AND R != None:
			# get new key from get_new_key()

			# pass the right 32 bits R to function f and new_key
			# XOR L and what returns from function f
			# next_right = what returns from line above
			# next_left = R
		# else: return None

		# return tuple of left and right

def __main__():
	# take input for a key and check for 16 characters or 64 bits
	# take input for a plaintext and check for 16 characters or 64 bits

	# if everything checks out pass key and plaintext to DES and wait for a cipher text
