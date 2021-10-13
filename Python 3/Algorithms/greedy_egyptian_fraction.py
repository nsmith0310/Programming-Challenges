###this algorithm will find the fraction representation of any fraction with a
###smaller numerator than denominator

###this is classified as greedy because is selects the maximum possible
###fraction fraction as the subsequent addedend to be subtracted from the
###remaining value until the numberator is reduced to 1

from math import ceil,gcd

def subtract(n1,d1,n2,d2):
  n1*=d2
  n2*=d1
  d1*=d2
  d2*=d1
  
  
  return [n1-n2,d1]
  
def fraction(n,d,f):
  greed = ceil(d/n)
  f.append("1/"+str(greed))
  
  n1 = subtract(n,d,1,greed)
  if n1[0]==0 or n1[1]==0:
    return f
  else:
    return fraction(n1[0],n1[1],f)
    
    
    
print(' + '.join(fraction(223,3333,[])))
  
  
  
  