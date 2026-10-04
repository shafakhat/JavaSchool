---
title: Objects that cannot be modified are immune to aliasing
nav: Objects that cannot be mod...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1050
source: https://web.archive.org/web/20090504071927/http://www.java2s.com:80/Code/Java/Class/Objectsthatcannotbemodifiedareimmunetoaliasing.htm
---
```java title=Example.java
// : appendixa:Immutable1.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
public class Immutable1 {
  private int data;
  public Immutable1(int initVal) {
    data = initVal;
  }
  public int read() {
    return data;
  }
  public boolean nonzero() {
    return data != 0;
  }
  public Immutable1 multiply(int multiplier) {
    return new Immutable1(data * multiplier);
  }
  public static void f(Immutable1 i1) {
    Immutable1 quad = i1.multiply(4);
    System.out.println("i1 = " + i1.read());
    System.out.println("quad = " + quad.read());
  }
  public static void main(String[] args) {
    Immutable1 x = new Immutable1(47);
    System.out.println("x = " + x.read());
    f(x);
    System.out.println("x = " + x.read());
  }
} ///:~
```

1.  Create Object Demo
---  ---
2.  Passing objects to methods may not be what you're used to.
3.  Demonstrates Reference objects
4.  A companion class to modify immutable objects
5.  Examination of the way the class loader works
6.  A changeable wrapper class
