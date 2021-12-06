list1 = []
def inputmerge():
    print("Enter 10 numbers")
    for x in range(10):
        nums = input("Enter a number: ")
        while nums.isalpha():
            print("Please enter a number")
            letter = input("Enter a number: ")
        list1.append(x)

def mergeSort(list1): 
    if len(list1) > 1: 
        mid = len(list1)//2
        L = list1[:mid]
        R = list1[mid:]

        print("Left: ", ' '.join(str(x)for x in L))
        print("Right: ", ' '.join(str(y)for y in R))
  
        mergeSort(L) 
        mergeSort(R) 
  
        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                list1[k] = L[i] 
                i+=1
            else: 
                list1[k] = R[j] 
                j+=1
            k+=1
          
        
        while i < len(L): 
            list1[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            list1[k] = R[j] 
            j+=1
            k+=1
  
        printList(list1)

def printList(list1): 
    for i in range(len(list1)):         
        print(list1[i],end=" ") 
    print()
        
inputmerge()
mergeSort(list1)

print ("Given array is", end=" ")  
printList(list1) 
mergeSort(list1) 
print("Sorted array is: ", end=" ") 
printList(list1) 

print("Ascending Order")
for i in range(len(list1)):
    print(list1[i], end= " ")
