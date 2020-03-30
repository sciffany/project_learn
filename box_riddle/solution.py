# Python Program to shuffle a given array 
import random 
  
# A function to generate a random permutation of arr[] 
def randomize (arr, n): 
    # Start from the last element and swap one by one. We don't 
    # need to run for the first element that's why i > 0 
    for i in range(n-1,0,-1): 
        # Pick a random index from 0 to i 
        j = random.randint(0,i) 
  
        # Swap arr[i] with the element at random index 
        
        arr[i],arr[j] = arr[j],arr[i] 
    return arr 
  
# Driver program to test above function. 

noOfTrials = 1000
n = 4
score = 0
for trialNo in range(noOfTrials):
    arr = [i for i in range(n)]
    n = len(arr)
    randomize(arr, n)
    bandScore = 0
    for personNo in range(n):
        # slight strategy
        # newArr = arr + arr
        # if personNo in newArr[personNo:personNo+int(n/2)]:
        #     bandScore+=1
        # random solution
        # newArr = [i for i in range(n)]
        # randomize(newArr, n)
        # for boxToLook in newArr[:(n/2)]:
        #     if personNo == arr[boxToLook]:
        #         bandScore+=1
        #         break
        #linky solution
        boxToLook = personNo
        for box in range(int(n/2)):
            # print(box)
            boxContent = arr[boxToLook]
            if boxContent == personNo:
                bandScore+=1
                break
            boxToLook = boxContent
    if bandScore == n:
        score+=1
print(score/noOfTrials * 100)
            
        
