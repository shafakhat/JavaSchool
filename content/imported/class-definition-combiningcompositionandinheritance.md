---
title: Combining composition and inheritance
nav: Combining composition and ...
description: Imported from the java2s.com archive: Combining composition and inheritance
section: Imported - java2s Archive
order: 1295
source: https://web.archive.org/web/20140829075402/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Combiningcompositionandinheritance.htm
---
```java title=Example.java
class A {
  A(int i) {
    System.out.println("A constructor");
  }
}
class SubA extends A {
  SubA(int i) {
    super(i);
    System.out.println("SubA constructor");
  }
}
class B {
  B(int i) {
    System.out.println("B constructor");
  }
}
class SubB1 extends B {
  SubB1(int i) {
    super(i);
    System.out.println("SubB1 constructor");
  }
}
class SubB2 extends B {
  SubB2(int i) {
    super(i);
    System.out.println("SubB2 constructor");
  }
}
class SubB3 extends B {
  SubB3(int i) {
    super(i);
    System.out.println("SubB3 constructor");
  }
}
// A cultural way of doing something:
class C {
  C(int i) {
    System.out.println("C constructor");
  }
}
class SubC extends C {
  private SubB1 subB1;
  private SubB2 subB2;
  private SubB3 subB3;
  private SubA subA;
  public SubC(int i) {
    super(i + 1);
    subB1 = new SubB1(i + 2);
    subB2 = new SubB2(i + 3);
    subB3 = new SubB3(i + 4);
    subA = new SubA(i + 5);
    System.out.println("SubC constructor");
  }
}
public class MainClass{
  public static void main(String[] args) {
    SubC x = new SubC(9);
  }
}
java title=Example.java
C constructor
B constructor
SubB1 constructor
B constructor
SubB2 constructor
B constructor
SubB3 constructor
A constructor
SubA constructor
SubC constructor
```
