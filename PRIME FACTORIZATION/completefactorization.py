import math
import random


def miller_rabin_primalitytest(n,a):
	z=n-1
	d=z
	while(d%2==0):
		d=d//2
	if(pow(a,d,n)!=1):
		x=d
		while(x<n):
			r=pow(a,x,n)
			if(r==n-1):
				return "Probable Prime"
			else:
				x=2*x
		return "Composite"
	else:
		return "Probable Prime"

def isprime(n):
	if(n%2==0 and n>2):
		return False
	elif(n==2):
		return True
	else:
		if(n<2047):
			L=[2]
		elif(n<1373653):
			L=[2,3]
		elif(n<25326001):
			L=[2,3,5]

		elif(n<3215031751):
			L=[2,3,5,7]

		elif(n<2152302898747):
			L=[2,3,5,7,11]

		elif(n<3474749660383):
			L=[2,3,5,7,11,13]

		elif(n<341550071728321):
			L=[2,3,5,7,11,13,17]

		elif(n<3825123056546413051):
			L=[2,3,5,7,11,13,17,19,23]
		else:
			L=[2,3,5,7,11,13,17,19,23,29,31,37]
		i=0
		while(i<len(L)):
			if(miller_rabin_primalitytest(n,L[i])=="Probable Prime"):	#WORKS FOR ALL NUMBERS LESS THAN 2^64.
				i+=1
			else:
				return False
		return True

def pollardrho(n):
	if(isprime(n)):
		return n
	else:
		x=random.randrange(2,n)
		y=x
		d=1
		while (d==1):
			x=(pow(x,2,n)+1)%n
			y=(pow(y,2,n)+1)%n
			y=(pow(y,2,n)+1)%n
			d=math.gcd(abs(x-y),n)
		if(d==n):			
			return pollardrho(n)
		else:
			return d

def sieveoferathosthenes(n=10**6+10):
	primes=[]
	L=[True]*(n+1)
	L[0]=L[1]=False
	j=2
	while(j<=n**0.5):
		if(L[j]):
			k=j**2
			while(k<=n):						
				L[k]=False
				k+=j
		j+=1
	
	for i in range(0,len(L)):
		if(L[i]):
			primes.append(i)
	return primes




def factorize(n):
	if(n==1):
		return []
	elif(isprime(n)):
		return [n]
	else:
		factors=[]
		x=int(n**0.5)+2
		INT_MAX=10**6+10
		minsize=min(x,INT_MAX)
		L=sieveoferathosthenes(minsize)
		for i in range(0,len(L)):
			p=L[i]
			if(n%p==0):
				while(n%p==0):
					n=n//p
					factors.append(p)
		
		if(n==1):
			return factors

		elif(isprime(n)):
			factors.append(n)
			return factors
		else:
			fact=pollardrho(n)
			if(isprime(fact)):
				factors.append(fact)
				factors.append(n//fact)
			else:
				temp=fact
				temp1=pollardrho(fact)
				factors.append(temp1,fact//temp1,n//fact)
			return factors


def primefactorize(n):
	factorsdict={}
	M=factorize(n)
	for i in range(0,len(M)):
		if(M[i] in factorsdict.keys()):
			factorsdict[M[i]]+=1
		else:
			factorsdict[M[i]]=1
	return factorsdict


def arrayoffactors(n):
	dic=primefactorize(n)
	L=[]
	for e in dic.keys():
		L.append((e,dic[e]))	
	fac=[1]
	for e,f in L:
		fac+=[i*e**j for j in range(1,f+1) for i in fac]
	return fac








