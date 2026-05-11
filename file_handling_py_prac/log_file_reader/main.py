with open("logs.txt", 'r') as f:
    for line in f:
        if line.startswith("ERROR"):
            print(line)