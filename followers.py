followers = {}

command = input()
while command != "Log out":
    command = command.split(": ")
    action = command[0]
    
    if action == "New follower":
        username = command[1]
        if username not in followers:
            followers[username] = 0 
            
    elif action == "Like":
        username = command[1]
        count = int(command[2])
        if username not in followers:
            followers[username] = count
        else:
            followers[username] += count
    elif action == "Comment":
        username = command[1]
        if username not in followers:
            followers[username] = 1
        else:
            followers[username] += 1
            
    elif action == "Blocked":
        username = command[1]
        if username in followers:
            del followers[username]  
        else:
            print(f"{username} doesn't exist.")
            
    command = input()


print(f"{len(followers)} followers")
for username, total_count in followers.items():
    print(f"{username}: {total_count}")