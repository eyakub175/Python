# Here x is a new reference to same list lst
def my_function(x):
    x[0] = 10
    x[1] = 10
    x[2] = 10

num = [1,3,4,5,6,7,8]
my_function(num)
print(num)