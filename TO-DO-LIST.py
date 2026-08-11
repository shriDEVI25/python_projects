tasks=[]

while True:
    print("--to do list--")
    print("1. Add Task")
    print("2. delete Task")
    print("3. view Task")
    print("4. exit")

    choice=input("enter your choice")
    #add task
    if choice=="1":
        task =input("enter task:")
        tasks.append(task)
        print("task added successfully")

    #delete task
    elif choice=="2":
        if len(tasks)==0:
            print("no task delete.")
        else:
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])
            num=int(input("enter task number to delete:"))
            if num >= 1 and num <= len(tasks):
                deleted_task= tasks.pop(num -1)
                print(deleted_task,"deleted successfully")
            else:
                print("invalid task number.")


    #view task
    elif choice =="3":
        if len(tasks) ==0:
            print("no tasks available.")
        else:
            print("your tasks:")
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])

    #exit

    elif choice=="4":
        print("thank you!")
        break
    else:
        print("invalid choice.")