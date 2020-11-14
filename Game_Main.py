import random, time

user_choice = input("How many numbers would you like to try to memorize?\n")
user_choice = int(user_choice)

numbers = []
for i in range (0,user_choice):
    numbers.append(random.randint(0,9))
print(numbers)

time.sleep(1.5)
for i in range(0,50):
    print('')

for i in range(0, user_choice):
    print("enter number at index " + str(i))
    number = int(input())
    if number == numbers[i]:
        print("You are right!")
    else:
        print("Sorry, incorrect.")
        break

print(numbers,"\nAwesome! You won!")