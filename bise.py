def bisectionsearch(L,left,right,k):
	mid=(left+right)//2
	if(right-left==1):
		return left
	else:
		if(L[left]<=k<L[mid]):
			return bisectionsearch(L,left,mid,k)
		elif(L[mid]<=k<L[right]):
			return bisectionsearch(L,mid,right,k)
		elif(k==L[right]):
			return right
		else:
			return -1

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
				

		



