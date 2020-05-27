import math
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

def checkperfectpower(n,a):
	x=int(math.log(n,2))+1
	if (binarysearch(2,x,a,n)=="Not Perfect Power"):
		if (a<int(n**0.5)+2) :
			return checkperfectpower(n,a+2)
		else:
			return binarysearch(2,x,a,n)

	else:
		return binarysearch(2,x,a,n)


def binarysearch(left,right,a,n):
	mid=(left+right)//2
	l=fpower(a,left)
	r=fpower(a,right)
	m=fpower(a,mid)
	if(l==n):
		return [a,left]
	elif(r==n):
		return [a,right]
	elif(m==n):
		return [a,mid]
	elif(m<n<r):
		return binarysearch(mid+1,right,a,n)
	elif(l<n<m):
		return binarysearch(left,mid,a,n)		
	else:
		return "Not Perfect Power"

def isperfectpower(n):
	return checkperfectpower(n,2+n%2)

#O(log(n)*⋅(log(log(n)))**2) TimeComplexity


