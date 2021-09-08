#!/usr/bin/python

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

# find average lenght of the word in each sentence

s = list(sentence1.replace(',',' ').replace('.',' ').replace('!',' ').split())
l = 0
for x in s:
    l += len(x)

# Given a string, find the first non-repeating character in it and return its index. 
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.

def findfirstuniq(s):
    for i,c in enumerate(s):
        if c not in s[i+1::]:
            return i
    return -1
"""
print(findfirstuniq('abcde'))
print(findfirstuniq('abcdae'))
print(findfirstuniq('alphabet'))
print(findfirstuniq('barbados'))
print(findfirstuniq('crunchy'))
"""

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

def palindromecheck(s):
    for i,c in enumerate(s):
        stemp = s[:i:] + s[i+1::]
        if stemp == stemp[::-1]:
            print(stemp, stemp[::-1])
            return True
    return False

#palindromecheck('ahla')
#palindromecheck('ahlb')

#Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of 
#the non-zero elements.

def movezeros(a):
    for x in a:
        if x == 0:
            a.append(0)
            a.remove(x)
    return a

#print(movezeros([0,1,2,3,0,1,2,3]))
#print(movezeros([1,2,3,4,0,0,0,0,5,6,7,8,0]))


# Given an array containing None values fill in the None values with most recent 
# non None value in the array 
def fillblanks(a):
    val = None
    for i,x in enumerate(a):
        if x:
            val = x
        else:
            a[i] = val
    print(a)
    return True

#array1 = [1,None,2,3,None,None,5,None]
#fillblanks(array1)


#Given two sentences, return an array that has the words that appear in one sentence and not
#the other and an array with the words in common. 

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

def wordcheck(a1, a2):
    adiff, asame = [], []
    for word in a1.split():
        if word in a2.split():
            asame.append(word)
        else:
            adiff.append(word)
    return adiff, asame

#print(wordcheck(sentence1, sentence2))

# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 

def checkprimes(n):
    x=1
    while x<=n:
        isprime = 1
        for y in range(1,x+1):
            if x%y == 0 and (y!=1 and y!=x):
                isprime = 0
        if isprime == 1:
            print(f"-- {x} -- ")
        x += 1

checkprimes(1445)
