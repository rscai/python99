# Eval

>`eval(expression, globals=None, locals=None)`
>
>實參是一個字符串，以及可選的 globals 和 locals。 globals 實參必須是一個字典。 locals 可以是任何映射對象。
>
>expression 參數會作為一個 Python 表達式（從技術上說是一個條件列表）被解析並求值，使用 globals 和 locals 字典作為全局和局部命名空間。如果 globals 字典存在且不包含以 __builtins__ 為鍵的值，則會在解析 expression 之前插入以此為鍵的對內置模塊 builtins 的字典的引用。這意味著 expression 通常具有對標準 builtins 模塊的完全訪問權限且受限的環境會被傳播。如果省略 locals 字典則其默認值為 globals 字典。如果兩個字典同時省略，表達式會在 eval() 被調用的環境中執行。返回值為表達式求值的結果。語法錯誤將作為異常被報告。例如:
>

```python
>>> x = 1
>> eval('x+1')
2
```

>這個函數也可以用來執行任何代碼對象（如 compile() 創建的）。這種情況下，參數是代碼對象，而不是字符串。如果編譯該對象時的 mode 實參是 'exec' 那麼 eval() 返回值為 None 。
>
>提示： exec() 函數支持動態執行語句。 globals() 和 locals() 函數各自返回當前的全局和本地字典，因此您可以將它們傳遞給 eval() 或 exec() 來使用。
>
>另外可以參閱 ast.literal_eval()，該函數可以安全執行僅包含文字的表達式字符串。