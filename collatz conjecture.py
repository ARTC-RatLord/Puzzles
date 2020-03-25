
# coding: utf-8

# In[5]:


def collatz(a):
    collatz_conjecture=[a]
    while collatz_conjecture[-1]>1:
        if collatz_conjecture[-1]%2 == 0:
            collatz_conjecture.append(collatz_conjecture[-1]//2)
        else:
            collatz_conjecture.append(collatz_conjecture[-1]*3+1)
    return collatz_conjecture
collatz(20)

