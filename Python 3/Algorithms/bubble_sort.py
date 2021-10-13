def bubble(l):
  lim = len(l)
  while 1!=-1:
    t = 0
    for i in range(0,lim-1):
      
      if l[i]>l[i+1]:
        l[i],l[i+1] = l[i+1],l[i]
        t=1
    if t==0:
      break
