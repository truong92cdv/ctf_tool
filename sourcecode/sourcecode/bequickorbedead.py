#!/usr/bin/env python
# -*- coding: utf-8 -*-

flag = "RK\236\212`v\273\236SJ\204\272GM\211\215CP\242\201HK\223\202wW\223\213LA\230\226YC\217\234tA\222\210\\W\211\204YK\222\213qF͆\031C\234\206U_"
v2_addr = 0x7fffffffe0cc
v2 = 0xe5fd2222
v2_plus_1 = 0x22
v2_plus_2 = 0xfd
v2_plus_3 = 0xe5
v2_plus = [0x22, 0x22, 0xfd, 0xe5]

for i in range(40):
	result = i
	flag = flag[:i] + chr(ord(flag[i]) ^ v2_plus[i%4]) + flag[i:]
	if (i % 4) == 3:
		v2 += 1

print flag
