input_month = 'January'
input_day = 31
is_valid_date = True
Season = 'Invalid'

valid_months = {
    "January": 31, "February": 29, "March": 31, "April": 30,
    "May": 31, "June": 30, "July": 31, "August": 31,
    "September": 30, "October": 31, "November": 30, "December": 31
}

if input_month in valid_months:
    max_days = valid_months[input_month]
    if not (1 <= input_day <= max_days):
        is_valid_date = False
else:
    is_valid_date = False
    
if is_valid_date:
    if (input_month == 'March' and input_day >= 20) or \
        (input_month == 'April') or \
        (input_month == 'May') or \
        (input_month == 'June' and input_day <= 20):
            Season = 'Spring'
    elif (input_month == 'June' and input_day >= 20) or \
        (input_month == 'July') or \
        (input_month == 'August') or\
        (input_month == 'September' and input_day <= 21):
            Season = 'Summer'
    elif (input_month == 'September' and input_day > 21) or \
        (input_month == 'October') or \
        (input_month == 'November') or \
        (input_month == 'December' and input_day <= 20):
            Season = 'Autumn'
    elif (input_month == 'December' and input_day > 20) or \
        (input_month == 'January') or\
        (input_month == 'February') or \
        (input_month == 'March' and input_day < 20):
            Season = 'Winter'