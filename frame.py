frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

userinput = int(input())

if userinput > len(frameworks):
    print('Error')
else:
    print(frameworks[userinput])

