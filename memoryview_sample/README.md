# Python built-in memoryview

Python's ***memoryview*** module is powerful tool to manage memory efficiently. See examples:

```python
@profile
def without_memoryview():
    a = "salam".encode() * (5 ** 10)
    b = a[1:]

    print(id(a))
    print(id(b))

    return None
```

Output:

```
140011522871312
140011474042896
Filename: memoryview.py

Line #    Mem usage    Increment   Line Contents
================================================
     3     14.4 MiB     14.4 MiB   @profile
     4                             def without_memoryview():
     5     60.8 MiB     46.4 MiB       a = "salam".encode() * (5 ** 10)
     6    107.4 MiB     46.7 MiB       b = a[1:]
     7                             
     8    107.4 MiB      0.0 MiB       print(id(a))
     9    107.4 MiB      0.0 MiB       print(id(b))
    10                             
    11    107.4 MiB      0.0 MiB       return None

```

```python
@profile
def with_memoryview():
    a = "salam".encode() * (5 ** 10)
    a = memoryview(a)
    b = a[1:]

    print(id(a))
    print(id(b))

    return None
```

```
140011576566792
140011576566024
Filename: memoryview.py

Line #    Mem usage    Increment   Line Contents
================================================
    14     14.4 MiB     14.4 MiB   @profile
    15                             def with_memoryview():
    16     60.8 MiB     46.4 MiB       a = "salam".encode() * (5 ** 10)
    17     60.8 MiB      0.0 MiB       a = memoryview(a)
    18     60.8 MiB      0.0 MiB       b = a[1:]
    19                             
    20     60.8 MiB      0.0 MiB       print(id(a))
    21     60.8 MiB      0.0 MiB       print(id(b))
    22                             
    23     60.8 MiB      0.0 MiB       return None
```


---

Created by [Elshad Agayev](https://elshadaghazade.wordpress.com/about/) | [EACAMP](https://elshadaghazade.com)