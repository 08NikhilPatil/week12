def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True
        
def primes_galore(L):
    if len(L)==0:
        return 0
    count=0
    ind=[]
    for i in range(2,len(L)):
        if is_prime(i):
            ind.append(i)
    index=[2]+ind
    for x in index:
        if is_prime(L[x]):
          count+=1

    return count
      

def f(x,y):
    return 30+x**2+y**2-3*x-4*y
def survival(T):
  tdatetime=datetime.datetime.now()
  for x in range(6):
      for y in range(6):
          #print(x,y)
        print(datetime.datetime.now()-tdatetime)
        if f(x,y)<=T:
              
          return True
  return False

import datetime
begin_time=datetime.datetime.now()
print(survival(30))
print(datetime.datetime.now()-begin_time)

s=str(input())
alpha='abcdefghijklmnopqrstuvwxyz'
beta=''
for i in s:
    s1=alpha.index(i)
    beta+=alpha[25-s1]
    
print(beta)

def m(L):
    n=len(L)
    mean=sum(L)/n
    return mean
    
def std_dev(X):
    std=0
    for i in range(len(X)):
        std+=(X[i]-m(X))**2
        dev=(std/(len(X)-1))**0.5
    return dev


def result(L,m):
    if m%len(L)==0:
        return L
    n=m%len(L)
    return result([L[-1]]+L[:-1],n-1)
    
inlist=input().split(',')
m=int(input())
outlist=result(inlist,m)
print(','.join(outlist))


def depth(exp):
    count=0
    maxcount=0
    for char in exp:
        if char == '(':
            count+=1
        elif char == ')':
            count-=1
        if count>maxcount:
            maxcount=count
        
    return maxcount