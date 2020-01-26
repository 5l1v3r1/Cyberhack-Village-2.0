#!/usr/bin/env python 

'''
Devansh was learning the basics of encoding , and he implemented a simple python script
he encoded some valuable information using the below script that he wrote , 
He forgot to code a decoder , help Devansh to decode the ciphertext 

'''

flag = "" #FLAG REMOVED 
aski = []
for i in flag:
	aski.append(ord(i))
#print(aski) 


changed = []
for i in range(len(aski)):
    changed.append((aski[i]*2)+1337)
#print(changed) #an absurd encoding , coz Devansh is actually dumb

enc = ''
for i in range(len(aski)):
	enc = enc + str(changed[i]) + "x"
print(enc) #final ciphertext 

#this is ciphertext (encoded flag)
#enc = "1469x1481x1467x1501x1467x1505x1583x1501x1439x1573x1527x1575x1441x1567x1527x1539x1441x1567x1579x1527x1547x1567x1557x1569x1527x1547x1569x1587x"
