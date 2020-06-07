#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 23:03:16 2020

@author: Lincoln
"""
import math
from collections import Counter
train_sent = ["<s> I could not finish my homework because there is a virus in my hard drive </s>", "<s> I could sleep all night since it is so quiet and peaceful </s>", "<s> I have not eaten since my cat hide the plate </s>", "<s> We don’t like to do our assignment </s>"]



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

print(train_dict)
    
test = "<s> I could not submit my assignment because my cat ate it </s>"


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

print(test_dict)

v = len(Counter(test.split()))

#Entropy
entropy = []
for i in range(len(bi_test)):
    #smothing
    prob = ((train_dict[bi_test[i]] + 1)/(train_dict[(bi_test[i].split())[0]] + v))
    entropy.append(prob * math.log2(prob))

h_of_x = (-1) * sum(entropy)

#perplexity
pp = math.pow(2,h_of_x)

print("\n\n")
print("H(x) is ", h_of_x, "\nPerplexity is ", pp)