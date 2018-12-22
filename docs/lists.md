# Lists

一個list，用遞歸形式定義，其是空或由第一元素及一個尾部構成的，這個尾部也是一個list。Python內建了一個數據類型`list`，其可以承載多個元素。且這些元素在其中都是有序存放的，每個元素都可以通過順序索引訪問。

## P101: Find the last element of a list

[include](../tests/lists/p101_test.py)

Python內建的`list`是有序序列，其中每個元素都可以通過位置索引直接訪問。且Python內建了函數`len`，用讀取任意有序序列的長度。先用`len`讀取`list`的長度，將長度減去一即為末尾元素的位置索引「位置索引是從`0`開始的」。

[include](../python99/lists/p101.py)

## P102: Find the last but one element of a list

[include](../tests/lists/p102_test.py)

`list` 是有序序列，其中每個元素都可以通過位置索引直接訪問。

[include](../python99/lists/p102.py)

## P103: Find the K'th element of a list

[include](../tests/lists/p103_test.py)