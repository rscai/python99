# functools.reduce

`reduce`是Python标准库提供的一个函数式的工具，其声明为：

```python
reduce(function, iterable, initializer)
```

其功能是将`function`累积地、从左往右作用于`iterable`中的每一个元素。

reduce相当于如下代码：

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
