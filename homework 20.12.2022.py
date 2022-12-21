import random


def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


def retry(attempts=5, desired_value=None):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):

            i = 0
            while i < attempts:
                if func(*args, **kwargs) == desired_value:
                    print(desired_value)
                    return desired_value
                elif func(*args, **kwargs) != desired_value:
                    print(func(*args, **kwargs))

                i += 1
            print('бажаного значення досягти не вдалося')

        return inner_wrapper
    return wrapper




@retry(desired_value=3)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(desired_value=[1, 2])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


@retry(attempts=7, desired_value=3)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(attempts=2, desired_value=[1, 2, 3])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


get_random_value()
get_random_values([1, 2, 3, 4])
get_random_values([1, 2, 3, 4], 3)
get_random_values([1, 2, 3, 4], size=1)


def square(n):

    for i in range(n):

        if i == 0:
            print('*' * n)
        elif i < n:
            print('*' + '-' * (n - 2) + '*')
        elif i == n:
            print('*' * n)
    return square()

square(5)









