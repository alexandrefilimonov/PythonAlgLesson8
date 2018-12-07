#Task 1. Определение количества различных подстрок с использованием хеш-функции. Пусть
#дана строка S длиной N, состоящая только из маленьких латинских букв. 
#Требуется найти количество различных подстрок в этой строке.
#------------------------

import hashlib

nSubstrings=1
list_hashes=[]
def rabin_karp(s, subs):
    len_subs = len(subs)
    h_subs = hash(subs)
    for i in range(len(s) - len_subs + 1):
        if (h_subs not in list_hashes and h_subs == hash(s[i:i + len_subs])):
            print("Substring #",nSubstrings,":",subs)
            list_hashes.append(h_subs)
            return i
    return -1

s="veni, vidi, vici"   #"papa" 
print("String s is",s)
n=len(s) #16
for i in range(n-1):
    j=n-i
    while(j>0) :
        if (not(j==n and i==0)) :
            if (rabin_karp(s, s[i:i+j])!=-1):
                nSubstrings+=1 
        j-=1
print("Total substrings found is", nSubstrings-1)



