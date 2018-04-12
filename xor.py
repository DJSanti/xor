######################################################
# Group: Greed
# Members: Alexandra Duran Chicas, Zachary Guillot, 
# Conan Howard, Oluwatoyosi Kade, Michael Mahan, 
# Darryl Rayborn, Jonathan Ruppel, Samantha Santiago
# Date: 04/11/2018
# Program: xor.py
# Objective: Read plaintext/ciphertext from stdin, XOR
# it with the bits of a key file, and send output to 
# stdout.
######################################################

# take message of size b bytes
# take key of size b bytes
# each bit of message is XOR'd with each bit of key
# XOR: where if either message or key has 1, then resulting output is 1; otherwise 0
# plain/cipher and key must be the same byte size

# things to do:

# import sys commands --> done
import sys
from itertools import cycle, izip # reference: https://docs.python.org/2/library/itertools.html

for i in sys.stdin:
	print i
# read plain/ciphertext from stdin
def xor(message, key):
	pass
	# if/else statement to XOR each bit
	for i in range(0, len(message)):
		pass
		hold = ""
		hold += message[i] ^ key[i]
	return hold
	
	# string to hold encrypted/decrypted
def Main():
	pass
	# controls sys stuff
	# send output to stdout
