#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces



# value = 32035
value = int(input())
tons = value // 32000
pounds = value % 2000 // 16
ounces = value % 16

print(f'Tons: {tons}')
print(f'Pounds: {pounds}')
print(f'Ounces: {ounces}')