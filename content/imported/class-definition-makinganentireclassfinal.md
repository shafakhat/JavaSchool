---
title: Making an entire class final
nav: Making an entire class final
description: Imported from the java2s.com archive: Making an entire class final
section: Imported - java2s Archive
order: 1137
source: https://web.archive.org/web/20140829085230/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Makinganentireclassfinal.htm
---
```java title=Example.java
class A {
}
final class B {
  int i = 7;
  int j = 1;
  A x = new A();
  void f() {
  }
}
public class MainClass {
  public static void main(String[] args) {
    B n = new B();
    n.f();
    n.i = 40;
    n.j++;
  }
}
```

| 5.27.1. | final Variables |
|---|---|
| 5.27.2. | 'Blank' final fields |
| 5.27.3. | Java Final variable: Once created and initialized, its value can not be changed |
| 5.27.4. | Using 'final' with method arguments |
| 5.27.5. | The effect of final on fields |
| 5.27.6. | You can override a private or private final method |
| 5.27.7. | Making an entire class final |
| 5.27.8. | Demonstrates how final variables are replaced at compilation time |
| 5.27.9. | Demonstration of final class members |
| 5.27.10. | Base class for demonstation of final methods |
| 5.27.11. | Demonstration of final constants |
| 5.27.12. | Demonstration of final variables |
