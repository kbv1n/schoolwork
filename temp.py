#solution accepts integer input representing a water temperature
#temperature >= 212, water state is "Boiling"
#temperature between 115-211, exclusive of the stop, water state is "Hot"
#temperature between 80-115, water state is "Warm"
#temperature between 33-80, water state is "Cold"
#temperature < 33, water state is "Frozen"
#temperature = 212, safety comment "Caution: Hot!"
#temperature < 33, safety comment "Watch out for ice!"
#solution outputs the water state and potential safety comment based on temperature


tempinput = int(input())
water = ''

if tempinput < 33:
    water = 'Frozen'
elif 33 <= tempinput < 80:
    water = 'Cold'
elif 80 <= tempinput < 115:
    water = 'Warm'
elif 115 <= tempinput < 211:
    water = 'Hot'
elif tempinput >= 212:
    water = 'Boiling'
    
if water == 'Frozen':
    print('Watch out for ice!') 
elif water == 'Boiling':
    print('Caution: Hot!')
    
print(water)

    
