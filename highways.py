highway_number = 190
if 1 <= highway_number <= 90:
    direction = 'north/south' if highway_number % 2 != 0 else 'east/west'
    print(f"I-{highway_number} is primary, going {direction}")
elif 100 <= highway_number <= 999 and highway_number % 100 != 0:
    primary = highway_number % 100
    direction = 'north/south' if highway_number % 2 != 0 else 'east/west'
    print(f"I-{highway_number} is auxilary, serving I-{primary}, going {direction}")
# elif highway_number % 100
else:
    print(f"{highway_number} is not a valid interstate highway number.") 
    
print(00 % 100)






input_month = 'September'
input_day = 31
Season = ''

Spring = [
    'March',
    'April',
    'May',
    'June'
]
Summer = [
    'June',
    'July',
    'August',
    'September'
]
Autumn = [
    'September',
    'October',
    'November',
    'December'
]
Winter = [
    'December',
    'January',
    'February',
    'March'
]

if 0 <= input_day > 31:
    # if input_month == 'September' or 'June' and input_day >= 31:
    Season = 'Invalid'

elif input_month in Spring:
    if input_month == 'March' and 19 >= input_day:
        Season = 'Winter'
    if input_month == 'June' and 21 <= input_day:
        Season = 'Summer'
    elif input_month in Spring:
        Season = 'Spring'
elif input_month in Summer:
    if input_month == 'September' and 22 <= input_day:
        Season = 'Autumn'
    elif input_month in Summer:
        Season = 'Summer'
elif input_month in Autumn:
    if input_month == 'December' and 21 <= input_day:
        Season = 'Winter'
    elif input_month in Autumn:
        Season = 'Autumn'
elif input_month in Winter:
        Season = 'Winter'
else: 
    if input_month not in Spring or Autumn or Summer or Winter or 0 >= input_day >= 31:
        Season = 'Invalid'

print(Season)
