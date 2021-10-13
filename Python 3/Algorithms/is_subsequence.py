###check if b is a subsequence of a. The program will compare counters for each
###sequence, advancing both if they match, and only advancing the sequence being
###checked as the supersequence
###if the counter for the potential subsequence reached the end, it means that
###we were able to match all elements 

def subsequenceBool(a,b):
  lim1 = len(a)
  lim2 = len(b)
  i = 0
  j = 0
  while i<lim1:
    if a[i]==b[j]:
      i+=1
      j+=1
      if j==lim2:return True
    elif a[i]!=b[j]:
      i+=1
  return False
