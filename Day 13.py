import random
def add (n1 , n2):
    return add



def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
       # double_item = item * 2
        random_number = random.randint(1 , 3)
        new_item = add(random_number, item)
        b_list.append (new_item)
        print(b_list)

mutate([1 , 2 ,34 ,5 , 7])




