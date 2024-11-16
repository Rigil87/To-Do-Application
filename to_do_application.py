# My list
task_list = []
# Function for main menu        
def menu():
        print("""\nWELCOME TO YOUR TO DO LIST!!
          
    Add -------> Add a Task
    Delete-----> Delete a Task
    View-------> View Tasks
    Exit-------> Exit/Quit
    """)
#Main function to run the To-Do List application.
def main():
    while True:
        menu()
        try:
            choice = input("Enter your choice: ").capitalize().rstrip()
            if choice == "Add":
                added_task()
            elif choice == "Delete":
                deleted_task()
            elif choice == "View":
                viewed_task()
            elif choice == "Exit":
                exit_task()
                break
            else:
                print("Invalid choice.")
        finally:
            print()
# Task is used to add items to the to do list           
def added_task():
    add_task = input("""What needs to be added to your to do list? """
                    ).capitalize().rstrip()
    task_list.append(add_task)
    if not add_task:
        print("You didn't enter anything genius!")
    else:
        print(f"You added '{add_task}' to your task list:")
# Task is used to delete items from the to do list
def deleted_task():
    delete_task = input('''\nWhat would you like to delete from your 
to do list?  ''').capitalize().rstrip()
    if not delete_task:
            print("You didn't type anything....")
    else: 
        try:
            task_list.remove(delete_task)    
        except ValueError:
            print("\nPlease view list and enter selection as it appears.")
        else:
            print(f"{delete_task} has been deleted from your to do list.")
        finally:
            print()            
# Task is used to print a numbered list of tasks
def viewed_task():
    if task_list:
        print("\nThese are your tasks:")
        for item, task in enumerate(task_list, start=1):
            print(f"{item}. {task}")
    else:
        print("Your task list is empty.")
# Task used to exit the program        
def exit_task():
    print("\nGoodbye! Thanks for using the to do list!\n")
# Runs program               
main()
       