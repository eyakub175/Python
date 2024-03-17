#taking multiple input from user in python in two ways
#using split()

x,y,z = input("Enter 3 number:").split()
print(x,y,z)
print(type(x)) #here x type is string

a, b = input("Enter a 2 number: ").split()
print("first number {}, second number {}".format(a,b))

# taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter a multiple value: ").split()))
print("List of students: ", x)


#using list comprehension
x, y = [int(x) for x in input("Enter two value: ").split()]
print("First number is {} and second number is {}".format(x, y))
print()
