import random
import string

n = int(input('How many EC2 instances do I need: '))

# Get the department name from the user.
department = input('Enter the name of the department (Marketing, Accounting, or FinOps): ')

# Check if the department name is valid.
if department in ["Marketing", "Accounting", "FinOps"]:
    for f in range (n):
        # Generate a random number between 1 and 100 and associate it with the department.
        random_number = random.randrange(1, 100)
        print(f'Random number: {random_number}, Department: {department}')
else:
    print('This is not allowed.')


