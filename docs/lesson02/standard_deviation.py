"""
CSE212 
(c) BYU-Idaho
02-Prove - Problem 1.2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

"""
These 3 functions will (in different ways) calculate the standard
deviation from a list of numbers.  The standard deviation
is defined as the square root of the variance.  The variance is 
defined as the average of the squared differences from the mean.
"""

def standard_deviation_1(numbers):
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    avg = total / count
    sum_squared_differences = 0
    for number in numbers:
        sum_squared_differences += (number - avg) ** 2
    variance = sum_squared_differences / count
    return variance ** 0.5


def standard_deviation_2(numbers):
    sum_squared_differences = 0
    count_numbers = 0
    for number in numbers:
        total = 0
        count = 0
        for value in numbers:
            total += value
            count += 1
        avg = total / count
        sum_squared_differences += (number - avg) ** 2
        count_numbers += 1
    variance = sum_squared_differences / count_numbers
    return variance ** 0.5


def standard_deviation_3(numbers):
    count = len(numbers)
    avg = sum(numbers) / count
    sum_squared_differences = 0
    for number in numbers:
        sum_squared_differences += (number - avg) ** 2
    variance = sum_squared_differences / count
    return variance ** 0.5

numbers = [600, 470, 170, 430, 300]
print(standard_deviation_1(numbers))  # Should be 147.322 
print(standard_deviation_2(numbers))  # Should be 147.322 
print(standard_deviation_3(numbers))  # Should be 147.322 