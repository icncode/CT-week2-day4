# Fizz Buzz Number 2
# Write a function that takes an integer num and returns a list of numbers from 1 to n, following the constraints below:

# If a number is divisible by 3, append 'Fizz' to the list instead of the number
# If a number is divisible by 5, append 'Buzz' to the list instead of the number
# If a number is divisible by both 3 and 5, append 'FizzBuzz' to the list instead of the number
# Otherwise, append the number to the list

# Example:
# Input: 15
# Output: [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
#          'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']

def solution(n):
    output = []
    for number in range(1,n+1):
        if number % 3 == 0 and number % 5 == 0:
            output.append('FizzBuzz')
        elif number % 3 == 0:
            output.append('Fizz')
        elif number % 5 == 0:
            output.append('Buzz')
        else:
            output.append(number)
    return output


print(solution(15))


    


# print(solution(15))
