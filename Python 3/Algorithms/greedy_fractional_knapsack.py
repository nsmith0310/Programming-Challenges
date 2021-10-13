###fractional/continuous fractional knapsack problem
###solved with greedy algorithm:
###sort each value-wieght pair in descending order of their ratio
###we cannot take more than 1 of each in this version, and can simply just 
###add whole items until we cannot due to the weight capacity. any remainder
###will be a fraction of the current item we are on 

def fractionalSack(v,w,c):
  lim = len(v)
  l = [[v[i],w[i]] for i in range(0,lim)]
  l.sort(key = lambda x: x[0]/x[1])
  t=0
  cap = 0
  for i in range(lim-1,-1,-1):
    if cap+l[i][1]<c:
      cap+=l[i][1]
      t+=l[i][0]
    elif cap<c:
      
      t+=int(l[i][0]*(c-cap)/l[i][1])
      break
  return t
