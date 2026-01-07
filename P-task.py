print("---welcome to GT task manager---")
tasks=[]
i= 0
while True:
    num=int(input("\n choose ur number (1-4):\n 1.add task\n 2.view tasks\n 3.delete task\n 4.exit \n enter ur choice: "))
    print("1.add task\n 2.view tasks \n 3.delete task \n 4.exit")
    if num==1:
        new_task = input("enter task name: ")
        tasks.append(new_task)
    print("\n")
    if num==2:
        print("---your tasks are:")
        for t in tasks:
            if t!="":
                i+=1
                print(f"{i}. {t}")
                print("\n this all tasks")
    if num==3:
        num=int(input("enter task number to delete: "))
        print(f"{i}. {t}")
        num+=1
        tasks.pop(num-1)
        print("complet delete !!")
    if num==4:
        print("exiting task manager")
        break