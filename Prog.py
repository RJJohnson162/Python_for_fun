""" Develop a program that uses two functions.
The first function prompts the user to enter aa list of numbers
then pass the list to another function that performs calculations and returns:
sum of the numbers,
their average,
the smallest and largest number """
def get_numbers():
    num_list = []
    while True:
        try:
            num = float(input("Enter a number (or 'q' to quit): "))
            if num == 'q':
                break
            else:
                num_list.append(num)
        except ValueError:
            print("Invalid input")
    return num_list
def calculate(num_list):
    sum_of_nums = sum(num_list)
    avg = sum_of_nums / len(num_list)
    min_num = min(num_list)
    max_num = max(num_list)
    result = f"Sum: {sum_of_nums}\nAverage: {avg}\nSmallest Number: {
        min_num}\nLargest Number: {max_num}"
    return result

if __name__ == "__main__":
    num_list = get_numbers()
    print(calculate(num_list))
    