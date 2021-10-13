###merge sort divides the array in half recursively until we get the smallest
###part which when divided will have elements in both halves
###the algorithm then compares elements in both halves and sets the leftmost
###elements of the parent array to the smaller elements found by comparison

def merge(arr):
  ###check if array can be divided
  if len(arr)>1:
    ###midpoint
    m = len(arr)//2
    ###temporary sub arrays
    l,r = arr[:m],arr[m:]
    ###call recursively
    merge(l)
    merge(r)
    ###pointers
    i = j = k =0
    ###check elements of subarrays, setting the array to smaller of the two
    while i<len(l) and j<len(r):
      if l[i]<r[j]:
        arr[k]=l[i]
        i+=1
      else:
        arr[k]=r[j]
        j+=1
      k+=1
    ### one half of the temporary array is traversed before the other
    ### this will write over the array with the remaining elements in
    ###said subarray
    while i <len(l):
      arr[k]=l[i]
      i+=1
      k+=1
    while j <len(r):
      arr[k]=r[j]
      j+=1
      k+=1
