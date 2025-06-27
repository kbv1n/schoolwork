a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

x = 0
y = 0

x_range = (-10, 10)
y_range = (-10, 10)
solution = []
# A + B = C | 8x + 7y = 38
#                  -b   -b
#             8x = 31y
#             x = 31/8
#               x = 3

# D + E = F | 3x - 5y = -1
# x = 3 , y = 2

for x in range(*x_range):
    for y in range(*y_range):
        if a * x + b * y == c and d * x + e * y == f:
            solution.append(x)
            solution.append(y)
            print(f'x = {x} , y = {y}')
        


if solution == []:
            print('There is no solution')   


            
        
            


    
    
    