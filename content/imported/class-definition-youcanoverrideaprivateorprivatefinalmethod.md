---
title: You can override a private or private final method
nav: You can override a private...
description: Imported from the java2s.com archive: You can override a private or private final method
section: Imported - java2s Archive
order: 1145
source: https://web.archive.org/web/20140829091536/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Youcanoverrideaprivateorprivatefinalmethod.htm
---
```java title=Example.java
class A {
  // Identical to "private" alone:
  private final void f() {
    System.out.println("WithFinals.f()");
  }
  // Also automatically "final":
  private void g() {
    System.out.println("WithFinals.g()");
  }
}
class B extends A {
  private final void f() {
    System.out.println("OverridingPrivate.f()");
  }
  private void g() {
    System.out.println("OverridingPrivate.g()");
  }
}
class C extends B {
  public final void f() {
    System.out.println("OverridingPrivate2.f()");
  }
  public void g() {
    System.out.println("OverridingPrivate2.g()");
  }
}
public class MainClass {
  public static void main(String[] args) {
    C op2 = new C();
    op2.f();
    op2.g();
    B op = op2;
    // op.f();
    // op.g();
    A wf = op2;
    // wf.f();
    // wf.g();
  }
}
java title=Example.java
OverridingPrivate2.f()
OverridingPrivate2.g()
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
