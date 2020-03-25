from sys import argv

_, first, second, third = argv


def my_func(hour, rate, premium):
    return hour*rate+premium


print(my_func(int(first), int(second), int(third)))
