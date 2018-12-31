# Python基礎

## 概要

TBD

## 解釋型語言

TBD

## 編程範式

TBD

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