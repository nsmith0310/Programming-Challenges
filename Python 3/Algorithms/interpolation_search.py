###interpolation search is similar to binary search but performs better when 
###the array values are uniformly distributed

def intSearch(arr,elem):
  l = 0
  h = len(arr)-1
  while l<=h and elem>=arr[l] and elem<=arr[h]:
    if l==h:
      if arr[l]==elem:
        return arr[l]
      else:
        return -1
    pos = l + int(((elem-arr[l])*(h-l))/(arr[h]-arr[l]))
    if arr[pos]==elem:
      return pos
    elif arr[pos]<elem:
      l=pos+1
    else:
      h=pos-1
  return -1
