def main():
    numberofitems = input("Enter number of items >> ")
    while numberofitems.isalpha():
        print("Please insert a number")
        numberofitems = input("Enter number of items >>" )
    numberofitems = int(numberofitems)
    stack = []
    top = 0
    supermax = numberofitems
    choice = "a"
    while choice != "x":
        printoptions()
        choice = input("Enter choice >> ")
        while choice.isdigit():
            print("Please enter a letter")
            choice = input("Enter choice >> ")

        #Push a number
        if choice in "Aa":
            if top < supermax:
                num = inputnum()
                stack.insert(top,num)
                top+=1
            else:
                print("Stack overflow")
            printstack(stack)
        
        #Pop a number to remove
        elif choice in "Bb":
            if top > 0:
                choice = input("Do you really want to pop the element? [Y/N]: ")
                if choice in "Yy":
                    stack.pop()
                    top-=1
                else:
                    continue
            else:
                print("Stack underflow")
            printstack(stack)

        #to print the stacks
        elif choice in "Cc":
            print("top element is",stack[top-1])
            print("count = ",top)

        elif choice in "Dd":
                print("\t [h] Half")
                print("\t [t] Top-Bottom")
                choice = input("Enter the operation you wish to perform: ")
                if choice in "Hh":
                    count = input("Enter number of stacks: ")
                    while count.isalpha():
                        print("Please enter a number")
                        count = input("Enter number of stacks: ")
                    count = int(count)
                    stack1 = stack[0:count]
                    stack2 = stack[count:]
                    for i in range(len(stack1)-1,-1,-1):
                        print(i, "-",stack1[i])
                    print("\n")
                    for j in range(len(stack2)-1,-1,-1):
                        print(j, "-",stack2[j])
            

                elif choice in "Tt":
                    count = input("Enter a number of stacks: ")
                    while count.isalpha():
                        print("Please enter a number")
                        count = input("Enter a number of stacks: ")
                    count = int(count)
                    stack1 = stack[0:count]
                    stack2 = stack[count:]
                    for i in range(len(stack1)-1,-1,-1):
                        print(i, "-",stack1[i])
                    print("\n")
                    for j in range(len(stack2)-1,-1,-1):
                        print(j, "-",stack2[j])

                    

        #exit
        elif choice in "Xx":
            choice = input("Do you really want to exit? [Y/N]: ")
            if choice in "yY":
                break
            else:
                continue
def printoptions():
    print("[a] Push")
    print("[b] Pop")
    print("[c] Peek")
    print("[d] Share")
    print("[x] End")

def inputnum():
    num = input("Enter number to push >> ")
    while num.isalpha():
        print("Try again!")
        num = input("Enter number to push >> ")
    num = int(num)
    return num

def printstack(stack):
    for i in range (len(stack)-1,-1,-1):
        print(i,"-",stack[i])
main()
