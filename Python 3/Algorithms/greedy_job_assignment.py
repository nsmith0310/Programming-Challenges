###job scheduling for maximum profit 
###a greedy algorithm which will look for the highest profit jobs in
###descending (sorted) order
###this algorithm will try to find an empty slot for each job in descending
###order of profit based on their deadlines, and assign the job, if an empy
###slot exists, to the first open slot with the highest possible deadline
###value



def jobProfit(arr):
  lim = len(arr)
  arr.sort(key = lambda x: x[2])
  arr=arr[::-1]
  s = set()
  for i in range(0,lim):
    s.add(arr[i][1])
  t = len(list(s))

  slots = [False]*t
  schedule = [-1]*t
  
  for i in range(0,lim):
    s = min(arr[i][1]-1,t-1)
    while s>0 and slots[s]==True:
      s-=1
    if slots[s]==False:
      slots[s]=True
      schedule[s]=arr[i][0]
  return schedule
