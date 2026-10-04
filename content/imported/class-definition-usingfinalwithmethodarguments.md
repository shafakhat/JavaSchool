---
title: Using 'final' with method arguments
nav: Using 'final' with method ...
description: Imported from the java2s.com archive: Using 'final' with method arguments
section: Imported - java2s Archive
order: 1134
source: https://web.archive.org/web/20140829085750/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Usingfinalwithmethodarguments.htm
---
```java title=Example.java
class A {
  public void spin() {
  }
}
class B {
  void with(final A g) {
    // g = new A(); // Illegal -- g is final
  }
  void without(A g) {
    g = new A(); // OK -- g not final
    g.spin();
  }
  int g(final int i) {
    return i + 1;
  }
}
public class MainClass {
  public static void main(String[] args) {
    B bf = new B();
    bf.without(null);
    bf.with(null);
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
