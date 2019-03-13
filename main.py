@profile
def mem_func():
    lots_of_numbers = list(range(1500))
    x = ['letters'] * (5 ** 10)
    a = x
    del lots_of_numbers
    del x

    return None


if __name__ == "__main__":
    mem_func()