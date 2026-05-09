def save_todo():
    print("=" * 40, "Save Your Task", "=" * 40,'\n')
    print("Type 'quit' to exit the program and save your Todos")
    
    tasks = []
    
    while True:
        u_task = input("Enter Todo task: ").strip()
        
        if u_task.lower() == 'quit':
            break
        
        # is u_task empty?
        if not u_task:
            print("Field can't be empty. Please enter a Todo task: ")
            continue
                
        tasks.append(u_task)
        print(f"Added: {u_task} \n")
        
    
    with open("todo.txt", "w") as f:
        for line in tasks:
            f.write(line + "\n")
            
save_todo()