predef_list = [4, -27, 15, 33, -10]
userinput = int(input())
predef_list.sort()

if userinput > predef_list[-1]:
        Greater = True
else:
    Greater = False
    
print(f'Greater than Max? {Greater}')