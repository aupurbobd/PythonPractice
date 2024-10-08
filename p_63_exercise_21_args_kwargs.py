import math
def canrequirement(height, width, coverage):
    return math.ceil(height*width/coverage)


h=int(input("Enter the height of the wall:"))
w=int(input("Enter the width of the wall:"))
c=int(input('Enter the area of wall that 1 can of paint covers:'))

print(f'Total number of cans required for painting the wall is {canrequirement(h,w,c)}')