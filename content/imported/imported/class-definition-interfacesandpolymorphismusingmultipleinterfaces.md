---
title: Interfaces and Polymorphism
nav: Interfaces and Polymorphism
description: // Class definition including methods from both interfaces...
section: Imported - java2s Archive
order: 1030
source: https://web.archive.org/web/20070430051204/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/InterfacesandPolymorphismUsingMultipleInterfaces.htm
---
```java title=Example.java
interface ThisInterface {
  public void thisMethod();
}
interface ThatInterface {
  public void thatMethod();
}
class MyClass implements ThisInterface, ThatInterface {
  // Class definition including methods from both interfaces...
  public void thisMethod() {
    System.out.println("this");
  }
  public void thatMethod() {
    System.out.println("that");
  }
}
public class MainClass {
  public static void main(String[] a) {
    MyClass cls = new MyClass();
    cls.thisMethod();
    cls.thatMethod();
  }
}
```

```java title=Example.java

this
that
```
