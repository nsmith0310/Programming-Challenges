###binary search will continuously divide the sorted array into two, check if the
###midpoint is equal to the target
###if the target is smaller than the midpoint, we now only need to check the
###left/smaller half of the array (if it was larger, we would now check the
###right/larger side)
###from here, we now take the midpoint and check again, repeating this until
###the left pointer is equal to the right, and if at this point nothing has
###been found, the element is not present
###(l)ow initially equals 0, (h)igh initially equals the index of the last
###element and (m)id is set to the mid point of l and h, or (l+h)//2
###at each step, we have to update the l/h and m values so that the search
###will be in the correct halve at the correct indexes

def binary_search(arr,element):
  l = 0
  h = len(arr)-1
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
