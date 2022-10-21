# adult club))))

# user age

age = int(input('How old are you?'))

ageClub = 21
if age >= ageClub:
    print(f'You are {age} old, and you can free enter  in our adult  club ')
elif age < ageClub:
    print(f'You are cannot come to our club now! Come back after {ageClub - age}. Se you there!')

x = 0
print('Yes' if x else 'No') # just short version of if statement above(not like in js)
###