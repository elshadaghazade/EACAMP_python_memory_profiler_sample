from memory_profiler import profile

@profile
def without_memoryview():
    a = "salam".encode() * (5 ** 10)
    b = a[1:]

    print(id(a))
    print(id(b))

    return None


@profile
def with_memoryview():
    a = "salam".encode() * (5 ** 10)
    a = memoryview(a)
    b = a[1:]

    print(id(a))
    print(id(b))

    return None


if __name__ == "__main__":
    without_memoryview()
    with_memoryview()