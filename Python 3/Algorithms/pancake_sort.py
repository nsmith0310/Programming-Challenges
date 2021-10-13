def rev(arr,i):
  arr[:i+1]=arr[:i+1][::-1]
  return arr

def mx_ind(l,i):
  mx = -9999999999
  mx_ind = 0
  j = 0
  while j<i:
    if l[j]>mx:
      mx = l[j]
      mx_ind = j
    j+=1
  print(mx_ind)
  return mx_ind

def psort(l):
  lim = len(l)
  while lim>1:
    ind = mx_ind(l,lim)
    l = rev(l,ind)
    l = rev(l,lim-1)
    
    lim-=1
  return l
    

  