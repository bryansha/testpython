count = 0
list1 = []
go = True
while go:
    list1 = input("put your numbers here: ")
    length = len(list1)
    print(length)
    count += 1
    print(list1)
    ques = input("Anything else? ")


    if ques == "":
        go = False

