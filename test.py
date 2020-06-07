#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17  02:30:42 2020

@author: Lincoln
"""
from collections import Counter
train_sent = ["<s> i live in cheras </s>", "<s> i am an undergraduate student </s>", "<s> my campus is in gombak </s>"]



uni_train = []
bi_train =  []
tri_train = []

for train in train_sent:
    for j in range(len(train.split())-1):
        uni_train.append(str(train.split()[j]))
        bi_train.append(str(train.split()[j]+" "+train.split()[j+1]))
    
    for j in range(len(train.split())-2):
        tri_train.append(str(train.split()[j]+" "+train.split()[j+1]+" "+train.split()[j+2]))

train_dict = Counter(uni_train)
train_dict.update(Counter(bi_train))
train_dict.update(Counter(tri_train))

    
test = "<s> i live in gombak </s>"


uni_test = []
bi_test =  []
tri_test = []

for j in range(len(test.split())-1):
    uni_test.append(str(test.split()[j]))
    bi_test.append(str(test.split()[j]+" "+test.split()[j+1]))

for j in range(len(test.split())-2):
    tri_test.append(str(test.split()[j]+" "+test.split()[j+1]+" "+test.split()[j+2]))


test_dict = Counter(uni_test)
test_dict.update(Counter(bi_test))
test_dict.update(Counter(tri_test))



#print(train_dict, '\n')   
#print(test_dict,'\n')
#print(bi_test)


prob = 1.0
for i in range(len(bi_test)):
    prob = prob * (train_dict[bi_test[i]]/train_dict[(bi_test[i].split())[0]])
    
print(prob)




prob = 1.0
for i in range(len(tri_test)):
    prob = prob * (train_dict[tri_test[i]]/train_dict[(tri_test[i].split())[0] + " " + (tri_test[i].split())[1]])
    
print(prob)

#print( (train_dict['in gombak']/train_dict['in']))