###a very basic greedy algorithm which works in this case because the 
###array elements are sorted by end interval
###the code will take a list of intervals (sorted by end/second value) and 
###output the maximal number of intervals which do not overlap
###begins by selecting the interval with the lowest end value, and continues
###by selecting the first element with a start value greater than the 
###last picked element's end time and updates the last selected element

###works because by selecting activities with the lowest end time, we always
###allow for more possible start times later


def mostIntervals(l):
  ind = [0]
  curr = l[0]
  for i in range(1,len(l)):
    if l[i][0]>=curr[1]:
      ind.append(i)
      curr=l[i]
  print(ind)




s = [1 , 3 , 0 , 5 , 8 , 5] 
f = [2 , 4 , 6 , 7 , 9 , 9] 

l = [[s[i],f[i]] for i in range(0,len(s))]

mostIntervals(l)