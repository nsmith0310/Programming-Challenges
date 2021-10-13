
def selection(l):
  lim = len(l)
  for c in range(0,lim):
    mn = 9999999999999
    mn_ind = 0
    for i in range(c,lim):
      if l[i]<mn:
        mn = l[i]
        mn_ind = i
    l[c],l[mn_ind]=l[mn_ind],l[c]
