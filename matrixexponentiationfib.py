import math
#FASTEST CODE TO COMPUTE NTH FIBONACCI NUMBER (IN O(log n) Time and O(n) Space Complexity)

def power(L,n):
	if(n==1):
		return L
	elif(n%2==0):
		A=power(L,n/2)
		return multiply(A,A)
	else:
		A=power(L,n//2)
		return multiply(A,multiply(A,L))

def multiply(A,B):
	if(len(A[0])==len(B)):
		l=len(A)
		m=len(B)
		n=len(B[0])
		return multiplication(A,B,l,m,n)
	else:
		return "Invalid Input"

def multiplication(A,B,l,m,n):
	C=[[0 for i in range(n)]for j in range (l)]
	for i in range (0,l):
		for j in range(0,n):
			sum=0
			for k in range(0,m):
				sum+=A[i][k]*B[k][j]
			C[i][j]=sum
	return C


def fib(n):
	if(n==0):
		return 0
	else:
		A=[[1,1],[1,0]]
		B=power(A,n)
		return B[0][1]
	
	
	






