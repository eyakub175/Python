import array
arr = array.array('i',[1,2,3])
print("The new created array is :", end=" ")
for i in range(0,3):
    print(arr[i], end=" ")
print("\r")
#using append

arr.append(4)
for i in range(0,4):
    print(arr[i], end=" ")
print("\r")
#using insert()

arr.insert(1,5)
for i in range(0,5):
    print(arr[i], end=" ")
print("\r")
#using pop()
arr.pop(1)
for i in range(0,4):
    print(arr[i], end=" ")
print("\r")

#using remove()
arr.remove(1)
for i in range(0,3):
    print(arr[i], end=" ")
print("\r")

#using index()

print(arr.index(3))
print("\r")

#using reverse()

arr.reverse()
print("The array after reversing is :", end=" ")
for i in range(len(arr)):
    print(arr[i], end= " ")
print("\r")
