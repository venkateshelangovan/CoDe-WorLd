"""
Given an array arr[ ] of size N having distinct elements, the task is to find the next greater element for
each element of the array in order of their appearance in the array.
       
Next greater element of an element in the array is the nearest element on the right which is greater than the
current element.

If there does not exist next greater of current element, then next greater element for current element is -1.
For example, next greater of the last element is always -1.

Sample input and output :

Input:

N = 4, arr[] = [1 3 2 4]

Output:

3 4 4 -1

Explanation:

In the array, the next larger element
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ?
since it doesn't exist, it is -1.

Input:

N = 5, arr[] [6 8 0 1 3]

Output:

8 -1 1 3 -1

Explanation:

In the array, the next larger element to
6 is 8, for 8 there is no larger elements
hence it is -1, for 0 it is 1 , for 1 it
is 3 and then for 3 there is no larger
element on right and hence -1.
"""
from collections import deque
 
def NextGreaterElement(arr):
   """
   This function returns the array with each element in the output_arr will return the next greater element
   of the element belongs to that index and if it doesn't exist, then -1 is assigned.
   input : arr - input array
   returns : output_arr - array with next greater element for each index
   
   Time Complexity : O(n)
   Space Complexity : O(n)
   """
   stack = deque()
   output_dict={}
   output_arr=[]
   stack.append(arr[0])
   for i in range(1,len(arr)):
       if len(stack)==0:
           stack.append(arr[i])
           continue 
       while (len(stack)!=0 and stack[-1]<arr[i]):
           output_dict[stack.pop()]=arr[i]
       stack.append(arr[i])
   while len(stack)!=0:
       output_dict[stack.pop()]=-1 
   for i in range(len(arr)):
       output_arr.append(str(output_dict[arr[i]]))
   return " ".join(output_arr)
           
                   
# enter the number of test cases
t=int(input())
while t>0:
   n=int(input()) # enter the size of the array
   input_arr=list(map(int, input().split(' ')[:n])) # get array elements
   print(NextGreaterElement(input_arr))
   t-=1