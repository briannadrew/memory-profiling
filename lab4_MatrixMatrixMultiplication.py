# lab4_BriannaDrew.py

# Brianna Drew
# February 8, 2021
# ID: #0622446
# Lab #4

# NO PROFILER...
# 10: 0.0 seconds overall, 0.0 milliseconds per element
# 50: 0.02293872833251953 seconds overall, 0.009175491333007813 milliseconds per element
# 100: 0.1775059700012207 seconds overall, 0.017750597000122072 milliseconds per element
# 300: 4.710371255874634 seconds overall, 0.05233745839860704 milliseconds per element
# 500: 26.396376848220825 seconds overall, 0.10558550739288329 milliseconds per element

# WITH PROFILER...
# 10: 0.18154478073120117 seconds overall, 1.8154478073120117 milliseconds per element
# 50: 6.0029144287109375 seconds overall, 2.401165771484375 milliseconds per element
# 100: 47.81924366950989 seconds overall, 4.781924366950989 milliseconds per element

# It is quite clear to see that the use of a profile exponentially increased the runtimes
# for the function. I think this is because this profile in particular is a memory
# profiler and doesn't measure runtimes. Therefore, the maker of this profiler most
# likely made a tradeoff, sacrificing runtime for more accurate measures of memory
# usage, ensuring the module takes it's time to perform the necessary analyses.

import random
import time
from memory_profiler import profile


@profile
def multiply():
    for i in range(size):
        for j in range(size):
            for k in range(size):
                P[i][j]=P[i][j]+(A[i][k]*B[k][j]) # multiplication



size=int(input("Enter size: "))

r1=size
c1=size
r2=size
c2=size


A=[[0 for i in range(c1)] for j in range(r1)] # initialize matrix A

# input matrix A
for i in range(r1):
    for j in range(c1):
        x=random.randint(1,100)
        A[i][j]=x

B=[[0 for i in range(c2)] for j in range(r2)] # initialize matrix B

# input matrix B
for i in range(r2):
    for j in range(c2):
        x=random.randint(1,100)
        B[i][j]=x

P=[[0 for i in range(c2)] for j in range(r1)] # initialize product matrix
start = time.time()
multiply() 
end = time.time()
elapsed = end - start # calculate overall runtime
elements = len(P) * len(P[0]) # get number of elements in the product matrix

# print results
print("Overall Time: ", elapsed, "seconds. Elements in Result Matrix: ", elements,
    ". Time per Element: ", (elapsed / elements) * 1000, " milliseconds.")

