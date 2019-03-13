# Python Memory Profiling Samples

Third party memory_profiler module is the powerful tool for profiling memory. This tool allows you to print, report or plot memory usage of your codes.

# Prerequisites

1. Install memory_profiler module

    ```
    pip install memory_profiler
    ```

2. Install matplotlib
    
    ```
    pip install matplotlib
    ```

# Usage samples

1. Create **main.py** file and copy+paste following codes below:

```python
@profile
def mem_func():
    lots_of_numbers = list(range(1500))
    x = ['letters'] * (5 ** 10)
    del lots_of_numbers
    return None
```

2. To see memory usage run the following commands in your terminal:

    ```
    python -m memory_profiler main.py
    ```

    Output:

    ```
    Line #    Mem usage    Increment   Line Contents
    ================================================
     1   14.555 MiB   14.555 MiB   @profile
     2                             def mem_func():
     3   14.555 MiB    0.000 MiB       lots_of_numbers = list(range(1500))
     4   89.062 MiB   74.508 MiB       x = ['letters'] * (5 ** 10)
     5   89.062 MiB    0.000 MiB       del lots_of_numbers
     6   89.062 MiB    0.000 MiB       return None

    ```

3. The memory_profiler also includes **mprof** which can be used to create full memory usage reports over time instead of line-by-line. It’s very easy to use; just take a look:

    ```
    mprof run memo_prof.py
    mprof: Sampling memory every 0.1s
    running as a Python program...
    ```

4. mprof can also create a graph that shows you how your application consumed memory over time. To get the graph, all you need to do is:

    ```
    mprof plot
    ```

    Result:

    ![](./mprof_graph.png)


---

Created by [Elshad Agayev](https://elshadaghazade.wordpress.com/about/) | [TechAcademy](https://tech.edu.az)