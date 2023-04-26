s = '-'
print(s.center(30,'-'))
print('my first app')
print(s.center(30,'-'))

print('should I have a cheat meal today?')
weekDays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri']
responses = []

for i in weekDays:
    response = input(f'did you go to gym on {i}? (yes or no)')
    if response == 'yes':
        responses.append(response)
        
canHaveACheatMeal = 'Yes' if len(responses) >= 5 else 'No'
print("Yes, you can " if canHaveACheatMeal=='Yes' else "No You can not have")