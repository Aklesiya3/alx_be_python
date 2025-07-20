pattern = int(input("enter the size of the pattern:"))
row = 0
while row < pattern :
    for col in range(pattern):
        print("*" , end="")
    print()
    row= row+1
