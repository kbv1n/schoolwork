various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

userInput = int(input())

typeFinder = type(various_data_types[userInput]).__name__

print(f'Element {userInput}: {typeFinder}')