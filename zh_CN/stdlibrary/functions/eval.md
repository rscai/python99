# Eval

>`eval(expression, globals=None, locals=None)`
>
>实参是一个字符串，以及可选的 globals 和 locals。 globals 实参必须是一个字典。 locals 可以是任何映射对象。
>
>expression 参数会作为一个 Python 表达式（从技术上说是一个条件列表）被解析并求值，使用 globals 和 locals 字典作为全局和局部命名空间。如果 globals 字典存在且不包含以 __builtins__ 为键的值，则会在解析 expression 之前插入以此为键的对内置模块 builtins 的字典的引用。这意味着 expression 通常具有对标准 builtins 模块的完全访问权限且受限的环境会被传播。如果省略 locals 字典则其默认值为 globals 字典。如果两个字典同时省略，表达式会在 eval() 被调用的环境中执行。返回值为表达式求值的结果。语法错误将作为异常被报告。例如:
>

```python
>>> x = 1
>> eval('x+1')
2
```

>这个函数也可以用来执行任何代码对象（如 compile() 创建的）。这种情况下，参数是代码对象，而不是字符串。如果编译该对象时的 mode 实参是 'exec' 那么 eval() 返回值为 None 。
>
>提示： exec() 函数支持动态执行语句。 globals() 和 locals() 函数各自返回当前的全局和本地字典，因此您可以将它们传递给 eval() 或 exec() 来使用。
>
>另外可以参阅 ast.literal_eval()，该函数可以安全执行仅包含文字的表达式字符串。