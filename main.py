"""
📝 Project 4: Daily Task Tracker (CLI App)
👨‍💻 Created by: Hashir Adnan
🌐 Website: www.techthf.xyz
🗓️ Date: [Insert today’s date]

📌 Description:
This is a simple command-line-based task tracker that allows users to:
1. Add new tasks
2. View all tasks
3. Exit the program

📦 Features:
- Adds tasks to a list
- Displays tasks with status (✅ completed / ❌ not completed)
- Clean user-friendly menu system

🧰 Technologies Used:
- Core Python (loops, conditionals, lists, dictionaries)

💡 Future Improvements:
- Add save/load using text files
- Mark tasks as completed
- Delete tasks or edit them

"""

def show_menu():
    print("\n📋 Task Tracker Menu:")
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Exit")

tasks = []  # This will store tasks in memory

while True:
    show_menu()
    choice = input("📌 Enter your choice (1-3): ")

    if choice == '1':
        task = input("📝 Enter the task: ")
        tasks.append({"task": task, "done": False})
        print("✅ Task added.")
    
    elif choice == '2':
        if not tasks:
            print("📭 No tasks found.")
        else:
            print("\n📄 Your Tasks:")
            for i, t in enumerate(tasks, start=1):
                status = "✅" if t["done"] else "❌"
                print(f"{i}. {t['task']} [{status}]")
    
    elif choice == '3':
        print("👋 Exiting. Goodbye!")
        break
    else:
        print("❗ Invalid choice. Try again.")
