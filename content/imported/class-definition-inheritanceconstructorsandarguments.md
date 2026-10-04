---
title: Inheritance, constructors and arguments
nav: Inheritance, constructors ...
description: Imported from the java2s.com archive: Inheritance, constructors and arguments
section: Imported - java2s Archive
order: 1288
source: https://web.archive.org/web/20140829075335/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Inheritanceconstructorsandarguments.htm
---
```java title=Example.java
class A {
  A(int i) {
    System.out.println("A constructor");
  }
}
class B extends A {
  B(int i) {
    super(i);
    System.out.println("B constructor");
  }
}
class C extends B {
  C() {
    super(11);
    System.out.println("C constructor");
  }
}
public class MainClass {
  public static void main(String[] args) {
    C x = new C();
  }
}
java title=Example.java
A constructor
B constructor
C constructor
```
