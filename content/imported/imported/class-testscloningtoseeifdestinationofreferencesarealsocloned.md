---
title: Tests cloning to see if destination of references are also cloned
nav: Tests cloning to see if de...
description: Tests cloning to see if destination of references are also cloned
section: Imported - java2s Archive
order: 1076
source: https://web.archive.org/web/20081009143516/http://www.java2s.com:80/Code/Java/Class/Testscloningtoseeifdestinationofreferencesarealsocloned.htm
---
```java title=Example.java
// : appendixa:Snake.java
// Tests cloning to see if destination
// of references are also cloned.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
public class Snake implements Cloneable {
  private Snake next;
  private char c;
  // Value of i == number of segments
  public Snake(int i, char x) {
    c = x;
    if (--i > 0)
      next = new Snake(i, (char) (x + 1));
  }
  public void increment() {
    c++;
    if (next != null)
      next.increment();
  }
  public String toString() {
    String s = ":" + c;
    if (next != null)
      s += next.toString();
    return s;
  }
  public Object clone() {
    Object o = null;
    try {
      o = super.clone();
    } catch (CloneNotSupportedException e) {
      System.err.println("Snake can't clone");
    }
    return o;
  }
  public static void main(String[] args) {
    Snake s = new Snake(5, 'a');
    System.out.println("s = " + s);
    Snake s2 = (Snake) s.clone();
    System.out.println("s2 = " + s2);
    s.increment();
    System.out.println("after s.increment, s2 = " + s2);
  }
} ///:~
```

1.  A Cloning Example
---  ---
2.  Creating a Deep Copy
3.  Shallow Copy Test
4.  Deep Copy Test
5.  Creating local copies with clone
6.  You can insert Cloneability at any level of inheritance
7.  Cloning a composed object
8.  Serializable and clone
9.  Go through a few gyrations to add cloning to your own class
10.  Checking to see if a reference can be cloned
11.  The clone operation works for only a few items in the standard Java library
12.  Demonstration of cloning
13.  Simple demo of avoiding side-effects by using Object.clone
14.  Clone demo
