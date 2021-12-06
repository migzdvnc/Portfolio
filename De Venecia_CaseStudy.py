class Color:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedColor:
    def __init__(self):
        self.head = None

    def printlist(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next

    def Begin(self,newdata):
        NewColor = Color(newdata)
        NewColor.next = self.head
        self.head = NewColor

    def End(self, newdata):
        NewColor = Color(newdata)
        if self.head is None:
            self.head = NewColor
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next=NewColor

    def Between(self,middle_color,newdata):
        if middle_color is None:
            print("There is no Node")
            return
        NewColor = Color(newdata)
        NewColor.next = middle_color.next
        middle_color.next = NewColor

    def Remove(self,removekey):
        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
            
        if (HeadVal == None):
            return
        prev.next = HeadVal.next
        HeadVal = None





c1 = LinkedColor()

c1.head = Color("Red")
c2 = Color("Green")
c3 = Color("Blue")
c4 = Color("Orange")
c5 = Color("Pink")
c6 = Color("Black")
c7 = Color("Purple")
c8 = Color("White")
c1.head.next = c5
c5.next = c3
c3.next = c7
c7.next = c2
c2.next = c8
c8.next = c6
c6.next = c4

while True:
    print("**********************************")
    print("[A] Add an Element in the Beginning")
    print("[B] Add an Element in the End")
    print("[C] Add an Element in Between")
    print("[D] Remove an Element")
    print("[E] Quit")
    print("**********************************")

    print("\n")
    print("**********************************")
    c1.printlist()
    print("**********************************")
    
    choice = input("Enter Choice: ")

    if choice in "Aa":
        color = input("Enter Color: ")
        c1.Begin(color)
        print("\n")
        c1.printlist()
        print("\n")
    elif choice in "Bb":
        color = input("Enter Color: ")
        c1.End(color)
        print("\n")
        c1.printlist()
        print("\n")
    elif choice in "Cc":
        color  = input("Enter Color: ")
        c1.Between(c1.head.next,color)
        print("\n")
        c1.printlist()
        print("\n")
    elif choice in "Dd":
        color  = input("Enter Color: ")
        ans = input("Are you sure you want to delete?: (Y/N)")
        if ans in "Yy":
            c1.Remove(color)
            print("\n")
            c1.printlist()
            print("\n")
        else:
            continue

    elif choice in "Ee":
        ans = input("Are you sure you want to exit?: (Y/N)")
        if ans in "Yy":
            break
        else:
            continue
        
        






