"""
    Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of
    the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print
    "FizzBuzz".
"""


# Function to check whether the given integer is Fizz, Buzz or FizzBuzz.
def fizz_or_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# Main function to hold main execution code.
def main():
    for i in range(1, 51):
        fizz_or_buzz(i)


# Call main function to run upon execution of file.
if __name__ == "__main__":
    main()
