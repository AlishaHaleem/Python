file = open("my_file.txt")
print(file.read())
# file.close()
# TODO: as we not remember to write file.close so we used
#  with statement foe not write close

with open ("my_file.txt") as file:
    contents = file.read()   # print(file.read())
    print(contents)

with open("new_file.txt", mode="w") as file:
    file.write("\nNew text.")  # new file created by this function

# TODO: In this we used ./  for moving to directory top to down
# TODO: and ../  for moving to directory down to top

