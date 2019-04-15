# Sorted

>Python列表有一个内置的list.sort（）方法可以直接修改列表。还有一个sorted（）内置函数，它会从一个可迭代对象构建一个新的排序列表。
>
>在本文档中，我们将探索使用Python中对数据进行排序的各种技术。

## 基本排序

>简单的升序排序非常简单：只需调用 sorted() 函数即可。它会返回一个新的已排序列表。

```python
>>> sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
```

>你也可以使用list.sort() 方法，它会直接修改原列表（并返回None 以避免混淆），通常来说它不如sorted() 方便——— 但如果你不需要原列表，它会更有效率。

```python
>>> a = [5, 2, 3, 1, 4]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5]
```

>另外一个区别是， list.sort() 方法只是为列表定义的，而 sorted() 函数可以接受任何可迭代对象。

```python
>>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]
```

### 关键函数

>list.sort() 和 sorted() 都有一个 key 形参来指定在进行比较之前要在每个列表元素上进行调用的函数。
>
>例如，下面是一个不区分大小写的字符串比较：

```python
>>> sorted("This is a test string from Andrew".split(), key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
```

>key 形参的值应该是一个函数，它接受一个参数并并返回一个用于排序的键。这种技巧速度很快，因为对于每个输入记录只会调用一次 key 函数。
>
>一种常见的模式是使用对象的一些索引作为键对复杂对象进行排序。例如：

```python
>>> student_tuples = [
...     ('john', 'A', 15),
...     ('jane', 'B', 12),
...     ('dave', 'B', 10),
... ]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

>同样的技术也适用于具有命名属性的对象。例如：

```python
>>> class Student:
...     def __init__(self, name, grade, age):
...         self.name = name
...         self.grade = grade
...         self.age = age
...     def __repr__(self):
...         return repr((self.name, self.grade, self.age))
```

```python
>>> student_objects = [
...     Student('john', 'A', 15),
...     Student('jane', 'B', 12),
...     Student('dave', 'B', 10),
... ]
>>> sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

[排序指南](https://docs.python.org/zh-cn/3/howto/sorting.html)