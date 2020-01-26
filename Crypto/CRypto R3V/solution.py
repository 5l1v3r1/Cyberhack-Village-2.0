#!/usr/bin/env python 
'''
Solution by : Asm0d3us(Devansh Batham)
'''
import re 

enc = "1469x1481x1467x1501x1467x1505x1583x1501x1439x1573x1527x1575x1441x1567x1527x1539x1441x1567x1579x1527x1547x1567x1557x1569x1527x1547x1569x1587x"

pattern = r'x'
removed_x = re.sub(pattern,' ',enc)
removed_x_list = removed_x.split()
str_to_int = list(map(int,removed_x_list))


#actual decoding here 
flag_ascii = []
for i in range(len(str_to_int)):
    flag_ascii.append((str_to_int[i]-1337)//2)

#ascii to text
flag = ""
for i in range(len(flag_ascii)):
	flag = flag + chr(flag_ascii[i])
print(flag)

#FLAG : BHARAT{R3v_w4s_e4sy_isnt_it}