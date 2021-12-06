import collections
nos = input("Enter max of queues: ")
while nos.isalpha():
    print("Enter integers only")
    nos = input("Enter max of queues: ")
nos = int(nos)
dq = collections.deque([])
top = 0
while True:
    print("[a] Enqueleft")
    print("[b] Enqueright")
    print("[c] Popleft")
    print("[d] Popright")
    print("[e] Exit")
    choice = input("Enter Option: ")
    choice = choice.lower()

    #user Enqueleft
    if choice in "Aa":
        if top<nos:
            item = input("Enter item to enqueue: ")
            while item.isalpha():
                print("Please insert a number")
                item = input("Enter item to enqueue: ")
            item = int(item)
            dq.appendleft(item)
            top+=1
            print(dq)
        else:
            print("Queue overflow")

    #user Enqueright
    elif choice in "Bb":
        if top < nos:
            item = input("Enter item to enqueue: ")
            while item.isalpha():
                print("Enter integers only")
                item = input("Enter item to enqueue: ")
            item = int(item)
            dq.append(item)
            top+=1
            print(dq)
        else:
            print("Queue overflow")

    #user Popleft
    elif choice in "Cc":
        if top > 0:
            sure = input("Are you sure you want to dequeue?[Y/N]: ")
            if sure in "Yy":
                dq.popleft()
                top-=1
                print(dq)
            else:
                print(dq)
                continue
        else:
            print("Queue underflow")

    #user popright
    elif choice in "Dd":
        if top > 0:
            sure = input("Are you sure you want to dequeue?[Y/N]: ")

            if sure in "Yy":
                dq.pop()
                top-=1
                print(dq)
            else:
                print(dq)
                continue
        else:
            print("Queue underflow")

    #user exit
    elif choice in "Ee":
        sure = input("Are you sure you want to exit?[Y/N]: ")
        if sure in "Yy":
            print("Program terminated")
            break
        else:
            continue
    else:
        print("Invalid input")
