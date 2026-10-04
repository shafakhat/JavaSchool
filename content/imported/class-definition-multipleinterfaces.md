---
title: Multiple interfaces
nav: Multiple interfaces
description: Imported from the java2s.com archive: Multiple interfaces
section: Imported - java2s Archive
order: 1155
source: https://web.archive.org/web/20140829084651/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Multipleinterfaces.htm
---
```java title=Example.java
interface A {
  void aMethod();
}
interface B {
  void bMethod();
}
interface C {
  void cMethod();
}
class ClassA {
  public void aMethod() {
  }
}
class D extends ClassA implements A, B, C {
  public void bMethod() {
  }
  public void cMethod() {
  }
}
public class MainClass {
  public static void t(A x) {
    x.aMethod();
  }
  public static void u(B x) {
    x.bMethod();
  }
  public static void v(C x) {
    x.cMethod();
  }
  public static void w(ClassA x) {
    x.aMethod();
  }
  public static void main(String[] args) {
    D h = new D();
    t(h);
    u(h);
    v(h);
    w(h);
  }
}
```

| 5.29.1. | Interfaces and Abstract Classes |
|---|---|
| 5.29.2. | Fields and Methods in an Interface |
| 5.29.3. | To implement an interface: use the implements keyword after the class declaration |
| 5.29.4. | A Partial Interface Implementation |
| 5.29.5. | Extending Interfaces |
| 5.29.6. | Interfaces and Multiple Inheritance |
| 5.29.7. | Interfaces and Polymorphism: Using Multiple Interfaces |
| 5.29.8. | Nesting Classes in an Interface Definition |
| 5.29.9. | Encapsulating Constants in a Program |
| 5.29.10. | Multiple interfaces |
| 5.29.11. | Initializing interface fields with non-constant initializers |
