###uses a prepend and recursively finds permutations for the list for n-1
###and prepends the iterating element to each

def permutations(l):
  lim = len(l)
  if lim==0:
    return []
  elif lim==1:
    return [l]
  else:
    
    l2 = []
    i = 0
    while i<lim:
      prepend = [l[i]]
      beforeafter = l[:i]+l[i+1:]
      for x in permutations(beforeafter):
        l2.append(prepend + x)
      i+=1
    return l2
