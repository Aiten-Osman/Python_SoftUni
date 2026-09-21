encrypted_message = input()
command = input()
while command != "End":
    command = command.split(" ")
    action = command[0]
    if action == "Translate":
        given_char, replacement_char = command[1], command[2]
        encrypted_message = encrypted_message.replace(given_char, replacement_char)
        print(encrypted_message)
    elif action == "Includes":
        substring = command[1]
        if substring in encrypted_message:
            print("True")
        else:
            print("False")
    elif action == "Start":
        substring = command[1]
        if encrypted_message.startswith(substring):
            print("True")
        else:
            print("False")
    elif action == "Lowercase":
        encrypted_message = encrypted_message.lower()
        print(encrypted_message)
    elif action == "FindIndex":
        given_char = command[1]
        for index in range(len(encrypted_message) - 1, -1, -1):
            if encrypted_message[index] == given_char:
                print(index)
                break
    elif action == "Remove":
        start_index, count = int(command[1]), int(command[2])
        encrypted_message = encrypted_message[:start_index] + encrypted_message[start_index + count:]
        print(encrypted_message)
    command = input()
