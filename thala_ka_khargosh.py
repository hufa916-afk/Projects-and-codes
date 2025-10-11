print("Welcome to Thala for a reason calculator!")
print("______________________________________________")
print(" ")
print("Enter 1 for string input. Enter 2 for integer input.")
first = input("Choose: ")
if first == "1":
    stringInput = input("Enter your String: ")
    length = len(stringInput)
    if(length==7):
        print("Thala for a reason!")
    else:
        print("Bole jo koyal bago me...")
elif first == "2":
    integerInput = int(input("Enter your Integer: "))
    integerOutput = [int(x) for x in str(integerInput)]
    y=0
    for i in range(len(integerOutput)):
        y = y + integerOutput[i]
    if(y==7):
        print("Thala for a reason!")
    else:
        print("Bole jo koyal bago me...")
else:
    print("Bole jo koyal bago me...\nTry again.")
