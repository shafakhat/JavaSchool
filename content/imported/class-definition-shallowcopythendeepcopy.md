---
title: Shallow copy then deep copy
nav: Shallow copy then deep copy
description: public static void main(String[] args) throws CloneNotSupportedException {
section: Imported - java2s Archive
order: 1261
source: https://web.archive.org/web/20140829080347/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Shallowcopythendeepcopy.htm
---
```java title=Example.java
class A {
  int l = 1;
}
class B extends A implements Cloneable {
  int m = 2;
}
class CloneDemo4 extends B {
  int n = 3;
  A a = new A();
  public static void main(String[] args) throws CloneNotSupportedException {
    CloneDemo4 c = new CloneDemo4();
    CloneDemo4 c2 = (CloneDemo4) c.clone();
    System.out.println(c.l);
    System.out.println(c2.l);
    System.out.println(c.m);
    System.out.println(c2.m);
    System.out.println(c.n);
    System.out.println(c2.n);
    System.out.println(c.a == c2.a);
  }
  protected Object clone() throws CloneNotSupportedException {
    // First, perform a shallow copy.
    CloneDemo4 temp = (CloneDemo4) super.clone();
    if (a != null)
      temp.a = new A();
    return temp;
  }
}
```
