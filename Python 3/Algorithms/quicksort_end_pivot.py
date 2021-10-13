###partition uses a pivot which will be placed in its correct position
###in the given array. One method is to select the last element as the pivot
###as below
###the partition function will check each element between i and high
###---if the element is less than the pivot, then we will switch that element
###---with that at index i, and increment i by 1
###at the end of the loop, we switch the pivot with the i+1th element
###and finally return i+1 as the index which will be used to recursively
###call the partition function

def partition(arr,low,high):
  p = arr[high]
  i = low-1
  for j in range(i+1,high):
    if arr[j]<p:
      i+=1
      arr[i],arr[j]=arr[j],arr[i]
  arr[i+1],arr[high]=arr[high],arr[i+1]
  return i+1
  
###this function will iterate over the array and pass subarrays to the left of
###the given index and the array to the right to partition function seperately

def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
        print(pi)
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)
    
l = [5,4,1,3,2]
quickSort(l,0,4)
print(l)