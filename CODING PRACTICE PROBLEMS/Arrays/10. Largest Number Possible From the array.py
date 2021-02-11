"""
Given a list of non negative integers, arrange them in such a manner that they form the largest number 
possible.The result is going to be very large, hence return the result in the form of a string.

Example 1:

Input: 
N = 5
Arr[] = {3, 30, 34, 5, 9}

Output: 9534330

Explanation:
Given numbers are {3, 30, 34,5, 9}, the arrangement 9534330 gives thelargest value.

Example 2:

Input: 
N = 4
Arr[] = {54, 546, 548, 60}

Output: 6054854654

Explanation: Given numbers are {54, 546,548, 60}, the arrangement 6054854654 gives the largest value.

"""
def Compare(x,y):
    """
    This function compares in such a way that, if int(string(x)+string(y))<int(string(y)+string(x)) returns -1 
    else 1 
    """
    xy=str(x)+str(y)
    yx=str(y)+str(x)
    if int(xy)>int(yx):
        return -1 
    return 1
   
def MyMergeSort(arr):
    """
    This function returns the sorted version of array needed for the problem of largest possible number from 
    given array 
    input : arr - array to be sorted 
    returns : expected sorted array 
    """
    if len(arr)>1:
        m=len(arr)//2
        l=arr[:m]
        r=arr[m:]
        MyMergeSort(l)
        MyMergeSort(r)
        i=j=k=0 
        while (i<len(l) and j<len(r)):
            if Compare(l[i],r[j])<0:
                arr[k]=str(l[i])
                k+=1 
                i+=1 
            else:
                arr[k]=str(r[j])
                k+=1 
                j+=1 
        while i<len(l):
            arr[k]=str(l[i])
            k+=1 
            i+=1 
        while j<len(r):
            arr[k]=str(r[j])
            k+=1 
            j+=1 

def LargestPossibleNumber(arr):
   """
   This function returns the largest possible number that can be formed by merging the given array
   Input :arr- containing n numbers
   returns : largest_possible_num - largest possible number that can be formed by merging the given array
   
   Time Complexity : O(nlogn) # for sorting 
   """
   largest_possible_num=-1
   MyMergeSort(arr)
   largest_possible_num="".join(arr)
   return largest_possible_num

                   
# enter the number of test cases
t=int(input())
while t>0:
   n=int(input()) # enter the size of the array
   input_arr=list(map(int, input().split(' ')[:n])) # get array elements for chocolate packet size 
   print(LargestPossibleNumber(input_arr))
   t-=1