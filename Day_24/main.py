list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(x) for x in list_of_strings]
result = [x for x in numbers if x % 2 == 0]
print(result)


# Read numbers from file1.txt
with open("file1.txt") as file1:
    file1_numbers = [int(line.strip()) for line in file1]

# Read numbers from file2.txt
with open("file2.txt") as file2:
    file2_numbers = [int(line.strip()) for line in file2]

# Find common numbers using list comprehension
result = [num for num in file1_numbers if num in file2_numbers]

# Output the result
print("Common Numbers:", result)
