---
title: An inner class cannot be overriden like a method
nav: An inner class cannot be o...
description: Imported from the java2s.com archive: An inner class cannot be overriden like a method
section: Imported - java2s Archive
order: 1270
source: https://web.archive.org/web/20140829090900/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Aninnerclasscannotbeoverridenlikeamethod.htm
---
```java title=Example.java
class A {
  private InnerA y;
  protected class InnerA {
    public InnerA() { System.out.println("A.InnerA()"); }
  }
  public A() {
    System.out.println("New A()");
    y = new InnerA();
  }
}
class B extends A {
  public class InnerB {
    public InnerB() { System.out.println("B.InnerB()"); }
  }
}
public class MainClass{
  public static void main(String[] args) {
    new B();
  }
}
```
