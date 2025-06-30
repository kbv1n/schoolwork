# When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust the data. 
# This adjustment can be done by normalizing to values between 0 and 1, or throwing away outliers.
# For this program, adjust the values by dividing all values by the largest value. 
# The input begins with an integer indicating the number of floating-point values that follow.
# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'{your_value:.2f}')


length = int(input())
numbers = []

for i in range(length):
    numbers.append(float(input()))

sorted = list(numbers)
sorted.sort()
largest_value = sorted[-1]

for i in range(length):
    numbers[i] % largest_value
    print(f'{numbers[i] / largest_value:.2f}')
    