tasks=[]

def add_task(task):
    tasks.append({"task":task,"completed":False})
    print(task,"added.")

def view_tasks():
    if not tasks:
        print("No task available.")
    else:
        for i,t in enumerate(tasks):
            status="Done" if t["completed"] else "Pending"
            print(f"{i+1}. {t['task']} [{status}]")

def mark_done(idx):
    if 0<=idx<len(tasks):
        tasks[idx]['completed']=True
        print(tasks[idx]["task"], " marked as done.")
    else:
        print("Invalid task number:")

def delete_task(idx):
    if 0<=idx<=len(tasks):
        r=tasks.pop(idx)
        print(r["task"], "deleted.")
    else:
        print("Invalid task number.")

def menu():
    while True:
        print("\nTo do List\n")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Tasks")
        print("4. Mark Tasks as Done")
        print("5. Exit")
        c=input("\nEnter your choice: ")
        if c=='5':
            print("Exiting...")
            break
        elif c=='1':
            t=input("Enter your task: ")
            add_task(t)
        elif c=='2':
            view_tasks()
        elif c=='3':
            n=int(input("Enter the task number to delete: "))
            delete_task(n-1)
        elif c=='4':
            n=int(input("Enter the task number you want to mark it as done: "))
            mark_done(n-1)
        else:
            print("Invalid choice. Enter again.")
menu()