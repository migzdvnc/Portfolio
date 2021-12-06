list1 = []
def bubbleInput():
    dgt = False
    while not(dgt):
        nums = input("Enter 10 integers: ")
        for i in nums:
            if not(i==" ") and not(i.isdigit()):
                dgt = False
                print("Enter integers only")
                break
            dgt = True
    list1.extend(int(x) for x in nums.split(" "))

def bubbleSort():
    for k in range(len(list1)):
        soorted = True
        for l in range(0,(len(list1)-k-1)):
            if list1[l] > list1[l+1]:
                soorted = False
                list1[l],list1[l+1] = list1[l+1],list1[l]
        if not(soorted):
            printSort(k)

def printSort(k):
    print("Pass",k,"=",list1)
    
bubbleInput()
bubbleSort()
print("Ascending order:",list1)
