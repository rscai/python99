# functools.reduce

`reduce`是Python標準庫提供的一個函數式的工具，其聲明為：

```python
reduce(function, iterable, initializer)
```

其功能是將`function`累積地、從左往右作用於`iterable`中的每一個元素。

reduce相當於如下代碼：

```python
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
```
