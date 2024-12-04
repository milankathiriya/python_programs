'''
_ _ _ _ 1
_ _ _ 1 2
_ _ 1 2 3
_ 1 2 3 4
1 2 3 4 5
'''

for i in range(1, 6):
    for k in range(5, i, -1):
        print("_", end="")
    for j in range(1, i+1):
        print(j, end="", sep=" ")
    print()
