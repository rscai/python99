# Python基礎

## 概要

>Python，是一種廣泛使用的高階程式語言，屬於通用型程式語言，由吉多．范羅蘇姆創造，第一版釋出於1991年。可以視之為一種改良（加入一些其他程式語言的優點，如物件導向）的LISP。作為一種直譯語言，Python的設計哲學強調程式碼的可讀性和簡潔的語法（尤其是使用空格縮排劃分程式碼塊，而非使用大括號或者關鍵詞）。相比於C++或Java，Python讓開發者能夠用更少的代碼表達想法。不管是小型還是大型程式，該語言都試圖讓程式的結構清晰明了。[^wiki-python]

Python是一種「解釋型/直譯式（Interpreted）」、「多範式」，「動態類型」高階程序設計語言。

## 解釋型語言

Python是一種解釋型語言，其源代碼無需編譯即可在虛擬機上執行。

## 多範式

Python支持多種編程範式，包括「面向對象/物件導向（Object Oriented）」和「函數式（Functional）」編程範式。

### 面向對象編程範式

面向對象編程範式中最核心的兩個概念是「類/類別（Class）」和「對象/物件（Object）」。

#### 類

Python使用關鍵詞「class」來定義類。類定義的基本形式為：

```python
class className(superClass):
    def __init__(self[, args]):
        [statement]
```

* `class`, `class`關鍵詞指明後續代碼為類定義
* `className`，任何合法的標識符都可以作類名
* `superClass`，繼承的超類，可不顯示指明。未顯示指明時則是繼承至`object`「一個名為`object`的內建類」
* `def __init__(self)

#### 對象

## 動態類型



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

## 參考文献

[^wiki-python]: https://zh.wikipedia.org/wiki/Python
