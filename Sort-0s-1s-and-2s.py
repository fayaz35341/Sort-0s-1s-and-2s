class Solution:
    def sort012(self, arr):
        # selection  sort (1010 /1111)
        # for i in range(len(arr)):
        #     minv=i
        #     for j in range(len(arr)-1):
        #         if arr[i]<arr[j]:
        #             arr[minv],arr[j]=arr[j],arr[minv]
       
        
        #bubble sort (1010 /1111)
        # for i in range(len(arr)):
        #     i_swap=0
        #     for j in range(len(arr)-1):
        #         if arr[j]>arr[j+1]:
        #             arr[j],arr[j+1]= arr[j+1],arr[j]
        #             i_swap=1
        #     if (i_swap==0):
        #         break
       
        
        #insertion sort 1010 /1111
        # for i in range(1, len(arr)):
        #      j=i 
        #      while (j>0 and arr[j-1]>arr[j]):
        #          arr[j-1],arr[j]=arr[j],arr[j-1]
        #          j -= 1 
                 
        # merg sort
        # if len(arr)) <=1:
        #     return arr  
        # mid=len(arr)//2 
        # left= arr[:mid]
        # right=arr[mid:]
        # left=[x for x in arr if arr[x]<arr[mid]]
        # right=[x for x in arr if arr[x]>arr[mid]]
        
        # return self(left,right)
        
        low=0
        mid=0
        high=len(arr)-1
        while mid<=high :
            if arr[mid]==0:
                arr[low],arr[mid]=arr[mid],arr[low]
                low+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            else:
                arr[mid],arr[high]=arr[high],arr[mid]
                high-=1
            
        return arr
        
        
