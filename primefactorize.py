import math
#Codes for finding primes in Sieve of Erathosthenes(O(nlog(logn))) Complexity and finding totient function and prime-factorization methods
def prime(n):
	L=[1]*(n+1)
	L[0]=L[1]=0
	L[2]=1
	j=2
	while(j<=n**0.5):
		if(L[j]):
			k=j**2
			while(k<=n):
				L[k]=0
				k+=j
		j+=1
	return L

M=[]
def primefactor(n):
	if(n%2==0):
		M.append(2)
		return primefactor(n//2)
	elif(n==1):
		return M
	else:
		A=prime(n)
		for i in range (3,len(A)):
			if(A[i]==1) and (n%i==0):
				M.append(i)
				return primefactor(n//i)


def primefactorize(n):
	if(n==1):
		return " "
	else:
		if(n%2==0):
			count=0
			while(n%2==0):
				n=n//2
				count+=1
			print(2,count)
			return primefactorize(n)
		else:
			L=[1]*(n+1)
			L[0]=L[1]=0
			L[2]=1
			j=2
			while(j<=n**0.5):
				if(L[j]):
					k=j**2
					while(k<=n):
						L[k]=0
						k+=j
				j+=1
			for i in range(3,len(L),2):
				if(n%i==0) :
					count=0
					while(n%i==0):
						n=n//i
						count+=1
					print(i,count)
			return primefactorize(n)



def factorize(n):
	L=[]
	for i in range(1,int(n**0.5)+1):
		if(n%i==0):
			L.append(i)
			L.append(n//i)
	if(L[-1]==L[-2]):
		L.pop()
	return L



def phi(n):
	if(n==1):
		return 1
	elif(n<1):
		return "Invalid Input"
	else:
		product=n
		L=prime(n)
		for i in range(2,len(L)):
			if(L[i]==1) and (n%i==0):
				product*=(i-1)/i
		return int(product)


def primefactorise(n,M):
	if(n==1):
		return M
	else:
		if(n%2==0):
			while(n%2==0):
				n=n//2
			M.append(2)
			return primefactorise(n,M)
		else:
			L=[1]*(n+1)
			L[0]=L[1]=0
			L[2]=1
			j=2
			while(j<=n**0.5):
				if(L[j]):
					k=j**2
					while(k<=n):
						L[k]=0
						k+=j
				j+=1
			for i in range(3,len(L),2):
				if(n%i==0) :
					count=0
					while(n%i==0):
						n=n//i						
					M.append(i)
			return primefactorise(n,M)



			








