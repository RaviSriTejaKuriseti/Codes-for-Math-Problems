import math

def fpower(x,t):
	if(t==0):
		return 1
	elif(t==1):
		return x
	else:
		y=fpower(x,t//2)
		if(t%2==0):
			return y*y
		else:
			return y*y*x


def checkperfectpower(n):
	x=int(math.log(n,2))+1
	y=int(n**0.5)+2
	for i in range(2,y):
		if (binarysearch(2,y,i,n)=="Not Perfect Power"):
			continue
		else:
			return binarysearch(2,y,i,n)
	return "Not Perfect Power"



def binarysearch(left,right,b,n):
	mid=(left+right)//2
	l=fpower(left,b)
	r=fpower(right,b)
	m=fpower(mid,b)
	if(l==n):
		return [left,b]
	elif(r==n):
		return [right,b]
	elif(m==n):
		return [mid,b]
	elif(m<n<r):
		return binarysearch(mid+1,right,b,n)
	elif(l<n<m):
		return binarysearch(left,mid,b,n)		
	else:
		return "Not Perfect Power"


def perfectpower(n):
	return checkperfectpower(n)

#O(log(n)*⋅(log(log(n)))**2) TimeComplexity

print(perfectpower(512))




