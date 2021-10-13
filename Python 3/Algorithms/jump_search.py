###jump search uses blocks to speed up a sequential search
###this requires a sorted array, and will use some way of determining
###a block size ie sqrt(length)
###will then search at the end of blocks, and if the element checked
###is greater than or equal to the target, will search within that block
###the inner block search can be sequential or binary

def jumpSearch(arr,element):
  lim = len(arr)
  block = int(lim**.5)
  
  i = 1
  while i<=lim//block:
    
    if arr[block*i - 1]>=element:
      
      l = i-1
      h = block*i-1
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
        
    i+=1
  
  return -1
