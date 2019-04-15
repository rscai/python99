# Python基础

## 概要

>Python，是一种广泛使用的高阶程式语言，属于通用型程式语言，由吉多．范罗苏姆创造，第一版释出于1991年。可以视之为一种改良（加入一些其他程式语言的优点，如物件导向）的LISP。作为一种直译语言，Python的设计哲学强调程式码的可读性和简洁的语法（尤其是使用空格缩排划分程式码块，而非使用大括号或者关键词）。相比于C++或Java，Python让开发者能够用更少的代码表达想法。不管是小型还是大型程式，该语言都试图让程式的结构清晰明了。[^wiki-python]

Python是一种「解释型/直译式（Interpreted）」、「多范式」，「动态类型」高阶程序设计语言。

## 解释型语言

Python是一种解释型语言，其源代码无需编译即可在虚拟机上执行。

## 多范式

Python支持多种编程范式，包括「面向对象/物件导向（Object Oriented）」和「函数式（Functional）」编程范式。

### 面向对象编程范式

面向对象编程范式中最核心的两个概念是「类/类别（Class）」和「对象/物件（Object）」。

#### 类

Python使用关键词「class」来定义类。类定义的基本形式为：

```python
class className(superClass):
    def __init__(self[, args]):
        [statement]
```

* `class`, `class`关键词指明后续代码为类定义
* `className`，任何合法的标识符都可以作类名
* `superClass`，继承的超类，可不显示指明。未显示指明时则是继承至`object`「一个名为`object`的内建类」
* `def __init__(self)

#### 对象

## 动态类型



```uml
@startuml
class A <<Entity>> {
    -a: String
    #b: Int
    +c: list
}
class B <<Entity>>

A "0..1" --o "1..*" B
@enduml
```

## 参考文献

[^wiki-python]: https://zh.wikipedia.org/wiki/Python
