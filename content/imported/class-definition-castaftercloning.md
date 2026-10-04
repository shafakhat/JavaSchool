---
title: Cast after cloning
nav: Cast after cloning
description: public static void main(String[] args) throws CloneNotSupportedException {
section: Imported - java2s Archive
order: 1257
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Castaftercloning.htm
---
```java title=Example.java
class A {
  int l = 1;
}
class B extends A implements Cloneable {
  int m = 2;
}
class CloneDemo3 extends B {
  int n = 3;
  A a = new A();
  public static void main(String[] args) throws CloneNotSupportedException {
    CloneDemo3 c = new CloneDemo3();
    CloneDemo3 c2 = (CloneDemo3) c.clone();
    System.out.println(c.l);
    System.out.println(c2.l);
    System.out.println(c.m);
    System.out.println(c2.m);
    System.out.println(c.n);
    System.out.println(c2.n);
    System.out.println(c.a == c2.a);
  }
}
```
