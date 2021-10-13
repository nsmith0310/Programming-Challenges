###KMP pattern searching algorithm
###this algorithm builds on the basic "naive" search algorithm which
###will check a superpattern of length M for a subpattern of length N 
### M - N + 1 times, and will not utilize previously checked values (this one does)
###it does so by maintaining a LPS array which will be used to skip unneccessary
###checks 

###the LPS array will store the length of the longest proper prefix which
###is also a suffix of the pattern we are going to look for.
###these values will be used in the main algorithm to circumvent repeated checking

def LPSarray(n,sub,lps):
  
  length = 0
  i = 1
  while i<n:
    if sub[i]==sub[length]:
      length+=1
      lps[i] = length
      i+=1
    else:
      if length!=0:
        length = lps[length-1]
      else:
        lps[i]=0
        i+=1
  return lps
  
###the search algorithm will use the lps array to set the position of
###the pattern pointer following a complete match/ mismatch to a point in 
###the pattern where we can potentially match
###the lps array will be used to retrieve the index of the pattern we will
###attempt to start matching from
def KMPsearch(array,pattern):
  f = []
  n = len(pattern)
  m = len(array)
  
  lps = LPSarray(n,pattern,[0]*n)
  
  i = 0
  j = 0
  while i<m:
    if array[i]==pattern[j]:
      i+=1
      j+=1
      
    if j==n:
      f.append(i-j)
      j = lps[j-1]
    elif i<m and array[i]!=pattern[j]:
      if j!=0:
        j = lps[j-1]
      else:
        i+=1
  return f
  
  
  
print(KMPsearch("aaabbaaabaa","baa"))