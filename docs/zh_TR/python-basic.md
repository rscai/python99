# Python Basic

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