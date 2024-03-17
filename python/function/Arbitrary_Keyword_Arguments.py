def my_function(**allkeyword):
    print(allkeyword)
    #or
    print("His address is: "+allkeyword["address"])


my_function(name="eyakub", age=23, address ="Dhaka")