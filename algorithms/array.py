from random import randint


def create_array(size=100, min=0, max=100):
    return [randint(min, max) for _ in range(size)]