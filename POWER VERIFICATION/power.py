import math

def binarysearch(L,left,right,k):
	mid=(left+right)//2
	if(L[left]==k):
		return left
	elif(L[right]==k):
		return right
	elif(L[mid]==k):
		return mid
	elif(L[right]<k) or (L[left]>k):
		return -1
	elif(L[mid]<k):
		return binarysearch(L,mid+1,right,k)	
	elif(L[mid]>k):
		return binarysearch(L,left,mid,k)
	else:
		return -1
#O(logn)



def ispower(m,n):
	if(m==n):
		return True
	elif(n%m!=0):
		return False
	else:
		return ispower(m,n//m)
#O(logn)


def isperfectpower(m,n):
	if(m==n):
		return True
	elif(m>n):
		return False
	else:
		x=m
		i=1
		while(n>x):
			x=x*x
			i=2*i
		L=[x]*(i//2+1)
		for j in range(len(L)-1,0,-1):
			L[j-1]=L[j]//m
		p=binarysearch(L,0,len(L)-1,n)
		if(p==-1):
			return False
		else:
			return True
#O(log(log n))


def fpower(x,n):
	if(n==0):
		return 1
	elif(n==1):
		return x
	else:
		y=fpower(x,n//2)
		if(n%2==0):
			return y*y
		else:
			return y*y*x
#O(logn)






	

			

