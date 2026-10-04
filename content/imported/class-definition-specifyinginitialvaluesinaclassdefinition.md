---
title: Specifying initial values in a class definition
nav: Specifying initial values ...
description: Imported from the java2s.com archive: Specifying initial values in a class definition
section: Imported - java2s Archive
order: 1048
source: https://web.archive.org/web/20070716122016/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Specifyinginitialvaluesinaclassdefinition.htm
---
```java title=Example.java
class A {
  A(int marker) {
    System.out.println("Bowl(" + marker + ")");
  }
  void f(int marker) {
    System.out.println("f(" + marker + ")");
  }
}
class B {
  static A a = new A(1);
  B() {
    System.out.println("Table()");
    staticA.f(1);
  }
  void f2(int marker) {
    System.out.println("f2(" + marker + ")");
  }
  static A staticA = new A(2);
}
class C {
  A a = new A(3);
  static A staticA = new A(4);
  C() {
    System.out.println("Cupboard()");
    staticA.f(2);
  }
  void f3(int marker) {
    System.out.println("f3(" + marker + ")");
  }
  static A staticA2 = new A(5);
}
public class MainClass {
  public static void main(String[] args) {
    System.out.println("Creating new Cupboard() in main");
    new C();
    System.out.println("Creating new Cupboard() in main");
    new C();
    t2.f2(1);
    t3.f3(1);
  }
  static B t2 = new B();
  static C t3 = new C();
}
```

```java title=Example.java
Bowl(1)
Bowl(2)
Table()
f(1)
Bowl(4)
Bowl(5)
Bowl(3)
Cupboard()
f(2)
Creating new Cupboard() in main
Bowl(3)
Cupboard()
f(2)
Creating new Cupboard() in main
Bowl(3)
Cupboard()
f(2)
f2(1)
f3(1)
```
