#!/usr/bin/env python  

'''
Soution By : Asm0d3us(Devansh Batham)
'''

import base64 

with open('ciphertext.txt', 'r') as dev:
	encoded = dev.read()
for i in range(16):
	sol = base64.urlsafe_b64decode(encoded)
	encoded = sol
print(sol)

#FLAG : BHARAT{hmm_B4s3s_w3r3_e4sy}