def args(*args ):
    print(args[0])
    #print(kwargs)
    sum = 0
    for n in args:
        sum += n
    return sum



#print(add(3, 5,6 ,1 , 2 , 7, 8, 9,11))
#add()

def calculate(n , **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

class car:
    def __init__(self , **kwargs):
        self.make = kwargs.get["make"]
        self.model = kwargs.get["model"]
        self.color = kwargs.get["color"]
        self.seat = kwargs.get["seat"]

my_car = car (make = 'Nisa', model = 'Gt_R')
print(my_car.model)