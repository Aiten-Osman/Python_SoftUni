crop = input().split(" & ")
command = input()
while command != "Collect!":
    command_list = command.split()
    action = command_list[0]

    if action == "Plant":
        crop_name = command_list[1]
        if crop_name not in crop:
            crop.insert(0, crop_name)

    elif action == "Transplant":
        crop_name = command_list[1]
        if crop_name in crop:
            crop.remove(crop_name)
            crop.append(crop_name)

    elif action == "Replace":
        idx1 = int(command_list[1])
        idx2 = int(command_list[2])
        if 0 <= idx1 < len(crop) and 0 <= idx2 < len(crop):
            crop[idx1], crop[idx2] = crop[idx2], crop[idx1]

    elif action == "Uproot":
        crop_name = command_list[1]
        if crop_name in crop:
            crop.remove(crop_name)

    command = input()

print(" | ".join(crop))

