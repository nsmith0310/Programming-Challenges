def gnome(l):
  lim = len(l)
  i = 0
  while i<lim:
    if i==0:
      i+=1
    elif i==lim-1:
      if l[i]>=l[i-1]:break
      else:
        l[i-1],l[i]=l[i],l[i-1]
        i-=1
    else:
      if l[i]>=l[i-1]:
        i+=1
      else:
        l[i-1],l[i]=l[i],l[i-1]
        i-=1
