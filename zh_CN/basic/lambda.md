# Lambda 表达式

>小型慝名函数可以用`lambda`关键词来创建。`lambda a, b: a+b`这个函数返回两个参数的和。Lambda函数可以在任何需要函数对象的地方使用。它们在语法上限于单个表达式。从语义上讲，它们只是包裹在常规函数定义外面的语法糖。与嵌套函数定义类似，lambda函数可以引用同范围内的变量。

```python
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```

>上述例子使用lambda表达式返回一个函数。另一个用法是传入一个小函数作为参数：

```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```