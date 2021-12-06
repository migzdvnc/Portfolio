def main():
    numberofitems = input("Enter number of items >> ")
    while numberofitems.isalpha():
        print("Please enter a number!")
        numberofitems = input("Enter number of items >> ")
    numberofitems = int(numberofitems)
    q = []
    top = 0
    supermax = numberofitems
    front = 0
    rear = 0
    back = 0
    choice = ""
    while choice != "x":
        printoptions()
        choice = input("Enter choice >> ")
        while choice.isdigit():
            print("Please enter a letter!")
            choice = input("Enter choice >> ")

        #command for enqueue
        if choice in "aA":
            if top < supermax:
                num = inputnum()
                q.insert(top,num)
                top+=1
                rear += 1
                back += 1
            else:
                print("\nStack overflow\n")

        #command for dequeue
        elif choice in "Bb":
            if top > 0:
                del q[0]
                front += 0
                back -= 1
                top-=1
                rear -= 1
            else:
                print("\nStack underflow\n")
            

        #command for print
        elif choice in "Cc":
            printstack(q)
            print("index",front)
            print("front",q[0],"\n")
            print("index",rear-1)
            print("rear",q[back-1])

        #user exit
        elif choice in "dD":
            choice = input("Do you really want to exit? [Y/N]: ")
            if choice in "yY":
                break
            else:
                continue
def printoptions():
    print("[a] Enqueue")
    print("[b] Dequeue")
    print("[c] Display")
    print("[d] Exit")

def inputnum():
    num = input("Enter number to push >> ")
    while num.isalpha():
        print("Please enter a number")
        num = input("Enter a number to push >> ")
    num = int(num)
    return num

def printstack(q):
    print(q)
main()
