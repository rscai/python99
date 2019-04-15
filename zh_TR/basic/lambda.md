# Lambda 表達式

>小型慝名函數可以用`lambda`關鍵詞來創建。`lambda a, b: a+b`這個函數返回兩個參數的和。Lambda函數可以在任何需要函數對象的地方使用。它們在語法上限於單個表達式。從語義上講，它們只是包裹在常規函數定義外面的語法糖。與嵌套函數定義類似，lambda函數可以引用同範圍內的變量。

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

>上述例子使用lambda表達式返回一個函數。另一個用法是傳入一個小函數作為參數：

```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```