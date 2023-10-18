# Set initialization
Park_1 = set()
Park_2 = set()

# Entering the numbers of the animals in Park_1 and Park_2

# Input validation for N1
while True:
    try:
        N1 = int(input("Enter the number of animals in 1st Park: "))
        break  # Break the loop if the input is a valid integer
    except ValueError:
        print("Please enter a valid number.")
        print("\n")

for i in range(N1):
    animal_park1 = input("Enter the name of the " + str(i + 1) + " animal in 1st park: ")
    Park_1.add(animal_park1)

# Input validation for N2
while True:
    try:
        N2 = int(input("Enter the number of animals in 2nd Park: "))
        break  # Break the loop if the input is a valid integer
    except ValueError:
        print("Please enter a valid number.")
        print("\n")

for i in range(N2):
    animal_park2 = input("Enter the name of the " + str(i + 1) + " animal in 2nd park: ")
    Park_2.add(animal_park2)

# Print the results
print("Animals in both Parks: " + str(Park_1.intersection(Park_2)))  # Use .intersection to find animals in both sets
print("Animals in 2nd park only: " + str(Park_2.difference(Park_1)))
