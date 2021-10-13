###exponential search will use a sorted array and starting with 1, take
###multiples, say by 2, of the starting counter and compare the target
###with the counter. Once we find an index with the counter, we can
###now use binary search to search for the element between the most recent
###and last multiple of the counter similar to jump search

def exponentialSearch(arr,element):
  if arr[0]==element:return 0
  
  lim = len(arr)
  
  
  i = 1
  while i<lim and arr[i]<=element:
    
    i = 2*i
  
  l = i//2
  h = min(lim,i)
  m = (l+h)//2
  
  while l<=h:
    if arr[m]==element:return m
    elif arr[m]<element:
      l = m+1
      m = (l+h)//2
    else:
      h = m-1
      m = (l+h)//2
        
  return -1
