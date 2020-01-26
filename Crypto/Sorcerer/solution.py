#!/usr/bin/env python 

'''
Solution by : Asm0d3us(Devansh Batham)

'''
import hashlib
import binascii

xored_hexed = "717b72617267484a03466c585d03446c4b03416c7d03444e"
unhexed = binascii.unhexlify(xored_hexed)
for i in range(256):
	decoded = ''.join(chr(ord(b)^i) for b in unhexed)
        if "BHARAT" in decoded:
          print(decoded)