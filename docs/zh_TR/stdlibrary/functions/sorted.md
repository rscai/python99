# Sorted

>Python列表有一個內置的list.sort（）方法可以直接修改列表。還有一個sorted（）內置函數，它會從一個可迭代對象構建一個新的排序列表。
>
>在本文檔中，我們將探索使用Python中對數據進行排序的各種技術。

## 基本排序

>簡單的升序排序非常簡單：只需調用 sorted() 函數即可。它會返回一個新的已排序列表。

```python
>>> sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
```

>你也可以使用list.sort() 方法，它會直接修改原列表（並返回None 以避免混淆），通常來說它不如sorted() 方便——— 但如果你不需要原列表，它會更有效率。

```python
>>> a = [5, 2, 3, 1, 4]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5]
```

>另外一個區別是， list.sort() 方法只是為列表定義的，而 sorted() 函數可以接受任何可迭代對象。

```python
>>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]
```

### 關鍵函數

>list.sort() 和 sorted() 都有一個 key 形參來指定在進行比較之前要在每個列表元素上進行調用的函數。
>
>例如，下面是一個不區分大小寫的字符串比較：

```python
>>> sorted("This is a test string from Andrew".split(), key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
```

>key 形參的值應該是一個函數，它接受一個參數並並返回一個用於排序的鍵。這種技巧速度很快，因為對於每個輸入記錄只會調用一次 key 函數。
>
>一種常見的模式是使用對象的一些索引作為鍵對複雜對象進行排序。例如：

```python
>>> student_tuples = [
...     ('john', 'A', 15),
...     ('jane', 'B', 12),
...     ('dave', 'B', 10),
... ]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

>同樣的技術也適用於具有命名屬性的對象。例如：

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