
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


# In[1]:


#sorted balloon list
x = [(114,136),(67,88),(14,126),(76,141),(66,78),(26,137),(85,133),(113,139),(43,141),(106,137),(60,128),(61,83),(57,102),(19,96),(43,99),(52,99),(41,102),(38,137),(71,108),(37,120)]
balloon_sorted = sorted(x)
print(balloon_sorted)
N= len(x)
print(N)

 

throw_number=1
dart=balloon_sorted[19][0]
print (dart)

 

for i in reversed(range(0,N)):
    if dart > balloon_sorted[i][1]:
        throw_number +=1
        dart = balloon_sorted[i][0]
        
print(throw_number)
print(dart)

