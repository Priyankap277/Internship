#!/usr/bin/env python
# coding: utf-8

# In[12]:


n= int(input("Enter variable:"))
fact=1
if n>=1:
    for i in range (1, n+1):
        fact=fact*i
    
print("factorial of variable:", fact)
    


# In[55]:


def isPrime(n):
    primeNumber = True
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
               primeNumber = False
    else:
        primeNumber = False
    return primeNumber    
        
n = int(input("Enter variable:"))
if isPrime(n):
    print(n , "is Prime number.")
else: 
    print(n, "is a composite number.")


# In[51]:


word = input("Enter a string:")
def isPalindrome(s):
    return s == s[::-1]
if isPalindrome(word):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")


# In[53]:


def find_third_side(side1, side2):
    side3 = (side1**2 + side2**2)**0.5
    return side3

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
third_side = find_third_side(side1, side2)

print(f"The length of the third side is: {third_side}")


# In[54]:


test_str = "pythonstring"
all_freq = {}
 
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print("Count of all characters in GeeksforGeeks is :\n "
      + str(all_freq))


# In[ ]:




