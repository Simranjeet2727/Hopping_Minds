#binary search
def bs(list1,n):
    low = 0  
    high = len(list1) - 1  
    mid = 0  
   

    while low <= high:  
        # for get integer result   
        mid = (high + low) // 2  
  
        # Check if n is present at mid   
        if list1[mid] < n:  
            low = mid + 1  
  
        # If n is greater, compare to the right of mid   
        elif list1[mid] > n:  
            high = mid - 1  
  
        # If n is smaller, compared to the left of mid  
        else:  
            return mid  
  
            # element was not present in the list, return -1  
    return -1        
        
        
        
#Initial list1  
list1 = [5,4,3,2,1,6,7,8,9,10] 
list2=sorted(list1) 
n =int(input("enter element: ")) 
  
# Function call   
result = bs(list2, n)  
  
if result != -1:  
    print("Element is present at index:",result)  
else:  
    print("Element is not present in list1") 