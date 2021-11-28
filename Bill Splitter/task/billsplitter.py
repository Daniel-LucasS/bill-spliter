# write your code here
import random


friends = {}                                                                            # create dictionary
print("Enter the number of friends joining (includes you):")
people_to_come = int(input())                                                           # How many peoples to come
print("")

# First verification
if people_to_come > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for name in range(people_to_come):
        names = str(input()).capitalize().strip()
        friends[names] = 0
    print("")
    print("Enter the total bill value:")
    bills = int(input())
    # Loop statement
    for name in friends.keys():
        friends[name] = round(bills / len(friends), 2)
    print("")

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input().strip().lower()                                                                   # Lucky Feature
    if 'yes' in answer:
        random_key = random.choice(list(friends.keys()))
        print(f"{random_key} is the lucky one!")
        del friends[random_key]
        print("")
        for name in friends.keys():
            friends[name] = round(bills / len(friends), 2)
        friends[random_key] = 0
        print(friends)
    else:
        print("No one is going to be lucky")
        print(friends)

else:
    print("No one is joining for the party")
