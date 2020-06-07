


import re
import math
from collections import Counter


# training data
with open("text-ngram.dat","r") as rfile:
    infile = rfile.readlines()

unifile = open("unigram.dat","w")
bifile = open("bigram.dat","w")
trifile = open("trigram.dat","w")    

sent = [s for s in infile[0].split(".")]
   
for line in sent:
    for j in range(len(line.split())-1):
        uni = line.split()[j]
        bi = line.split()[j]+" "+line.split()[j+1]
        unifile = open("unigram.dat","a")
        bifile = open("bigram.dat","a")            
        unifile.write(str(uni)+"\n")
        bifile.write(str(bi)+"\n")            
        unifile.close()
        bifile.close()
    
    for k in range(len(line.split())-2):
        trifile = open("trigram.dat","a")
        tri = line.split()[k]+" "+line.split()[k+1]+" "+line.split()[k+2]
        trifile.write(str(tri)+"\n")
        trifile.close()

#read unigram
with open("unigram.dat","r") as rfile:
    infile_uni = rfile.readlines()

unigr = [s.rstrip("\n") for s in infile_uni]


#read bigram
with open("bigram.dat","r") as rfile:
    infile_bi = rfile.readlines()

bigr = [s.rstrip("\n") for s in infile_bi]


#read trigram
with open("trigram.dat","r") as rfile:
    infile_tri = rfile.readlines()

trigr = [s.rstrip("\n") for s in infile_tri]



#test data
test = "KICT also aspires to enhance the quality of learning and teaching"


uni_test = []
bi_test =  []
tri_test = []


for j in range(len(test.split())-1):
    uni_test.append(str(test.split()[j]))
    bi_test.append(str(test.split()[j]+" "+test.split()[j+1]))
    
for k in range(len(test.split())-2):
    tri_test.append(str(test.split()[k]+" "+test.split()[k+1]+" "+test.split()[k+2]))


"""
Step 1 - Create a python dictionary to find and store the counts of all unigrams, bigrams
and trigrams of the sentences in the training file.
"""
train_dict = Counter(unigr)
train_dict.update(Counter(bigr))
train_dict.update(Counter(trigr))

#print(train_dict)


"""
Step 2 - Create a python dictionary to store the trigrams, bigrams and unigrams for the
test sentence.
"""
test_dict = Counter(uni_test)
test_dict.update(Counter(bi_test))
test_dict.update(Counter(tri_test))

#print(test_dict)


"""
Step 3 - Calculate probability of each bigram and trigram in test sentence
"""
#Bigram Formula
bi_prob = 1.0
for i in range(len(bi_test)):
    bi_prob = bi_prob * (train_dict[bi_test[i]]/train_dict[(bi_test[i].split())[0]])

print("\n\n--Bigram Formula--")
print("P(KICT also aspires to enhance the quality of learning and teaching) is: ", bi_prob)


#Trigram Formula
tri_prob = 1.0
for i in range(len(tri_test)):
    tri_prob = tri_prob * (train_dict[tri_test[i]]/train_dict[(tri_test[i].split())[0] + " " + (tri_test[i].split())[1]])

print("\n\n--Trigram Formula--")
print("P(KICT also aspires to enhance the quality of learning and teaching) is: ", tri_prob)




"""
Step 4 - apply smoothing on all trigrams, bigrams or unigrams including the ones without zero counts.
"""
v = len(Counter(test.split()))

#Entropy
entropy = []
for i in range(len(bi_test)):
    #Smoothing
    prob = ((train_dict[bi_test[i]] + 1)/(train_dict[(bi_test[i].split())[0]] + v))
    entropy.append(prob * math.log2(prob))

h_of_x = (-1) * sum(entropy)

#perplexity
pp = math.pow(2,h_of_x)

print("\n--After Smoothing--")
print("H(x) is ", h_of_x, "\nPerplexity is ", pp)



#file to save the result
with open("result.dat", "w") as fwrite:
  fwrite.write("Lincoln Khan")
  fwrite.write("\n\n--Bigram Formula--\n")
  fwrite.write("P(KICT also aspires to enhance the quality of learning and teaching) is: ")
  fwrite.write(str(bi_prob))
  fwrite.write("\n\n--Trigram Formula--\n")
  fwrite.write("P(KICT also aspires to enhance the quality of learning and teaching) is: ")
  fwrite.write(str(tri_prob))
  fwrite.write("\n\n--After Smoothing--\n")
  fwrite.write("H(x) is ")
  fwrite.write(str(h_of_x))
  fwrite.write("\nPerplexity is ")
  fwrite.write(str(pp))
  
