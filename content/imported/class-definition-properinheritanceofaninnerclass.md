---
title: Proper inheritance of an inner class.
nav: Proper inheritance of an i...
description: Imported from the java2s.com archive: Proper inheritance of an inner class.
section: Imported - java2s Archive
order: 1276
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Properinheritanceofaninnerclass.htm
---
```java title=Example.java
class A {
  protected class InnerA {
    public InnerA() {
      System.out.println("A.InnerA()");
    }
    public void f() {
      System.out.println("A.InnerA.f()");
    }
  }
  private InnerA y = new InnerA();
  public A() {
    System.out.println("New A()");
  }
  public void insertYolk(InnerA yy) {
    y = yy;
  }
  public void g() {
    y.f();
  }
}
class B extends A {
  public class InnerB extends A.InnerA {
    public InnerB() {
      System.out.println("B.InnerB()");
    }
    public void f() {
      System.out.println("B.InnerB.f()");
    }
  }
  public B() {
    insertYolk(new InnerB());
  }
}
public class MainClass {
  public static void main(String[] args) {
    A e2 = new B();
    e2.g();
  }
}
java title=Example.java
A.InnerA()
New A()
A.InnerA()
B.InnerB()
B.InnerB.f()
```
