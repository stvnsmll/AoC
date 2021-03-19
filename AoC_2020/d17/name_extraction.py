#Get the things from the list

name_file = open("./list_to_get.txt", 'r')
name_data = []

while True:
    # Get next line from file
    line = name_file.readline()

    # if line is empty end of file is reached
    if not line:
        break

    #print(line)
    name_data.append(line.strip())

name_file.close()


full_list = ""
for i in name_data:
    new_name = i.split(" = ")[0]
    print(new_name)
    full_list += (", " + new_name)

print()
print(full_list)