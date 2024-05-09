try:
    s = str(input("Enter a String: "))
    print (s)
    p = list()
    p = ["(",")","[","]","{","}"]
    for i in s:
        for j in p:
            if p != i:
                False
except:
    print("Please enter a valid String")