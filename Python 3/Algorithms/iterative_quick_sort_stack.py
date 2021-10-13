
###the partition function is the same as with the recursive version
def partition(arr,low,high):
  i = low-1
  pivot = arr[high]
  
  for j in range(low,high):
    if arr[j]<pivot:
      i+=1
      arr[i],arr[j]=arr[j],arr[i]
  
  arr[i+1],arr[high]=pivot,arr[i+1]
  return i+1

###the iterative version will use a stack 
def quickSortIterative(arr,l,h):
  size = h-l+1
  
  stack = [0]*size
  
  top = -1
  top+=1
  stack[top]=l
  top+=1
  stack[top]=h
  
  while top>=0:
    
    h = stack[top]
    top-=1
    l = stack[top]
    top-=1
    
    pivot = partition(arr,l,h)
    
    if pivot-1>l:
      top+=1
      stack[top]=l
      top+=1
      stack[top]=pivot-1
      
    if pivot+1<h:
      top+=1
      stack[top]=pivot+1
      top+=1
      stack[top]=h
      
