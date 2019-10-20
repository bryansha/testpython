count = 0

go = True
while go:
    list1 = input("put your numbers here: ")
    list1 = list1.split()
    list1.sort()
    for i in range(len(list1)-1):
        print(list1[i], end=" ")
    print(list[-1])

    length = len(list1)
    print("You entered", length, "numbers")

    ques = input("Anything else? ")
    if ques == "more":
        go = True
    elif ques == "":
        go = False
