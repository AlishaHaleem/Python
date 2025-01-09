print("Default values")
print("Hello world")

print("Positional arguments")


def add(n1 , n2):
    print(n1 + n2)


add(5, 10)


print("Keyword arguments")


def add(n1 , n2):    # n1 = 5 , n2 = 10
    print(n1 + n2)    # 5 + 10 = 15


add(n2=10, n1=5)