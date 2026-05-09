def input_todo():
    print("=" * 40, "Save Your Task", "=" * 40,'\n')
    print("Type 'quit' to exit the program and save your Todos")
    
    saved_tasks = []
    
    while True:
        u_task = input("Enter Todo task: ").strip().lower()
        
        # is u_task empty?
        if not u_task:
            print("Field can't be empty. Please enter a Todo task: ")
            continue
        
        if u_task == "quit":
            break
        
        saved_tasks.append(u_task)
        
    return saved_tasks
        
result_todos = input_todo()

with open("todo.txt", "a") as f:
    f.writelines(result_todos)