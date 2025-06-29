input1 = int(input())
input2 = int(input())
input3 = int(input())
input4 = int(input())
input5 = int(input())

Integer = input1 + input2 + input3 + input4 + input5
Float = float(Integer)
String = str(input1) + str(input2) + str(input3) + str(input4) + str(input5)

print(f'Integer: {Integer}')
print(f'Float: {Float:.1f}')
print(f'String: {String}')