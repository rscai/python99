# Python基础

## 概要

TBD

## 解释型语言

TBD

## 编程范式

TBD

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