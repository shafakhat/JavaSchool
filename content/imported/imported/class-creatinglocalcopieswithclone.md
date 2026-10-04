---
title: Creating local copies with clone
nav: Creating local copies with...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1000
source: https://web.archive.org/web/20081009143446/http://www.java2s.com:80/Code/Java/Class/Creatinglocalcopieswithclone.htm
---
Creating local copies with clone

```java title=Example.java
// : appendixa:LocalCopy.java
// Creating local copies with clone().
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class MyObject implements Cloneable {
  private int n;
  public MyObject(int n) {
    this.n = n;
  }
  public Object clone() {
    Object o = null;
    try {
      o = super.clone();
    } catch (CloneNotSupportedException e) {
      System.err.println("MyObject can't clone");
    }
    return o;
  }
  public int getValue() {
    return n;
  }
  public void setValue(int n) {
    this.n = n;
  }
  public void increment() {
    n++;
  }
  public String toString() {
    return Integer.toString(n);
  }
}
public class LocalCopy {
  public static MyObject g(MyObject v) {
    // Passing a reference, modifies outside object:
    v.increment();
    return v;
  }
  public static MyObject f(MyObject v) {
    v = (MyObject) v.clone(); // Local copy
    v.increment();
    return v;
  }
  public static void main(String[] args) {
    MyObject a = new MyObject(11);
    MyObject b = g(a);
    // Reference equivalence, not object equivalence:
    System.out.println("a == b: " + (a == b) + "\na = " + a + "\nb = " + b);
    MyObject c = new MyObject(47);
    MyObject d = f(c);
    System.out.println("c == d: " + (c == d) + "\nc = " + c + "\nd = " + d);
  }
} ///:~
```

1.  A Cloning Example
---  ---
2.  Creating a Deep Copy
3.  Shallow Copy Test
4.  Deep Copy Test
5.  Tests cloning to see if destination of references are also cloned
6.  You can insert Cloneability at any level of inheritance
7.  Cloning a composed object
8.  Serializable and clone
9.  Go through a few gyrations to add cloning to your own class
10.  Checking to see if a reference can be cloned
11.  The clone operation works for only a few items in the standard Java library
12.  Demonstration of cloning
13.  Simple demo of avoiding side-effects by using Object.clone
14.  Clone demo
