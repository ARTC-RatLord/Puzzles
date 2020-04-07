# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 09:07:24 2020

@author: 502598
"""

import pprint
message='53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;1‡(;:‡*8†83(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;'
freq_list=['a','i','n','s','r','l','d','c']
print(len(freq_list))
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

count1=sorted(count.items(),key=lambda x:x[1])
pprint.pprint(count1)

message=message.replace('8','e')
message=message.replace(';','t')
message=message.replace('4','h')
message=message.replace('‡','o')
print(message)