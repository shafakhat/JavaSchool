---
title: A companion class to modify immutable objects
nav: A companion class to modif...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1127
source: https://web.archive.org/web/20090504072113/http://www.java2s.com:80/Code/Java/Class/Acompanionclasstomodifyimmutableobjects.htm
---
```java title=Example.java
// : appendixa:Immutable2.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Mutable {
  private int data;
  public Mutable(int initVal) {
    data = initVal;
  }
  public Mutable add(int x) {
    data += x;
    return this;
  }
  public Mutable multiply(int x) {
    data *= x;
    return this;
  }
  public Immutable2 makeImmutable2() {
    return new Immutable2(data);
  }
}
public class Immutable2 {
  private int data;
  public Immutable2(int initVal) {
    data = initVal;
  }
  public int read() {
    return data;
  }
  public boolean nonzero() {
    return data != 0;
  }
  public Immutable2 add(int x) {
    return new Immutable2(data + x);
  }
  public Immutable2 multiply(int x) {
    return new Immutable2(data * x);
  }
  public Mutable makeMutable() {
    return new Mutable(data);
  }
  public static Immutable2 modify1(Immutable2 y) {
    Immutable2 val = y.add(12);
    val = val.multiply(3);
    val = val.add(11);
    val = val.multiply(2);
    return val;
  }
  // This produces the same result:
  public static Immutable2 modify2(Immutable2 y) {
    Mutable m = y.makeMutable();
    m.add(12).multiply(3).add(11).multiply(2);
    return m.makeImmutable2();
  }
  public static void main(String[] args) {
    Immutable2 i2 = new Immutable2(47);
    Immutable2 r1 = modify1(i2);
    Immutable2 r2 = modify2(i2);
    System.out.println("i2 = " + i2.read());
    System.out.println("r1 = " + r1.read());
    System.out.println("r2 = " + r2.read());
  }
} ///:~
```

1.  Create Object Demo
---  ---
2.  Passing objects to methods may not be what you're used to.
3.  Demonstrates Reference objects
4.  Objects that cannot be modified are immune to aliasing
5.  Examination of the way the class loader works
6.  A changeable wrapper class
