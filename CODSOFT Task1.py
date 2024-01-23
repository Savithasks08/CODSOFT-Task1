#A program for to do list

#Main program
#Create an empty list to store the tasks

list_task = []


#Function to display the menu options
def display_menu():
    #A print statement to show choices
    print("Menu:")
    print("\n1. Create a title for the tasks")
    print("\n2. Add a task")
    print("\n3. Delete a task")
    print("\n4. Display all tasks")
    print("\n5. Exit")
#End of display_menu() function
    
#Function to create the title for the tasks
def create_title():
    #Getting the title from the use
    title=input("\nEnter the title:")
    #Adding the title in the list_task 
    list_task.append(title)
    print("\nTitle added successfully.")
#End of create_title() function
    
#Function to add a task to the list
def add_task():
    #Getting the tasks from the user
    add_task=input("\nEnter the task you want to add: ")
    #Adding the task in list_task
    list_task.append(add_task)
    print("\nTask added successfully.")
#End of add_task() function
    

#Function to delete a task from the list
def delete_task():
    #Get the tasks to delete from already created task list
    del_task=input("\nEnter the task you want to delete: ")
    #If condition for checking the task is there in list_tasks or Not
    if del_task in list_task:
        #Removing the task using 'remove' method
        list_task.remove(del_task)
        print("\nTask deleted successfully.")
    else:
        print("\nTask not found.")
#End of delete_task() function
        

#Function to view all the tasks in the list
def display_tasks():
    print("Your to-do list:")
    i=1
    #A for loop for displaying the tasks
    for task in list_task:
        print(i,".",task)
        i=i+1
        
#End of display_tasks() function
        

# Function to choose the tasks
def choice_tasks():
    #Calling the choice_tasks() function for displaying the choices   
    display_menu()
    #Get the input from the user to choose the mentioned choices
    
    choice = input("\nEnter your choice: ")

    #A while loop for checking the valid choices and Calling the functions respectively

    while choice != "6":
        if choice=="1":
            create_title()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            display_tasks()
        elif choice=="5":
            exit()
        else:
            print("\nInvalid choice. Please try again.")
            exit()
        display_menu()
        choice = input("\nEnter your choice: ")
#End of choice_tasks() function   


# Call the run_program function to start the program
choice_tasks()