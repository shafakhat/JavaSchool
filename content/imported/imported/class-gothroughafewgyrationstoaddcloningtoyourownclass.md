---
title: Go through a few gyrations to add cloning to your own class
nav: Go through a few gyrations...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20081009143456/http://www.java2s.com:80/Code/Java/Class/Gothroughafewgyrationstoaddcloningtoyourownclass.htm
---
Go through a few gyrations to add cloning to your own class

```java title=Example.java
// : appendixa:AddingClone.java
// You must go through a few gyrations
// to add cloning to your own class.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
import java.util.ArrayList;
import java.util.Iterator;
class Int2 implements Cloneable {
  private int i;
  public Int2(int ii) {
    i = ii;
  }
  public void increment() {
    i++;
  }
  public String toString() {
    return Integer.toString(i);
  }
  public Object clone() {
    Object o = null;
    try {
      o = super.clone();
    } catch (CloneNotSupportedException e) {
      System.err.println("Int2 can't clone");
    }
    return o;
  }
}
// Inheritance doesn't remove cloneability:
class Int3 extends Int2 {
  private int j; // Automatically duplicated
  public Int3(int i) {
    super(i);
  }
}
public class AddingClone {
  public static void main(String[] args) {
    Int2 x = new Int2(10);
    Int2 x2 = (Int2) x.clone();
    x2.increment();
    System.out.println("x = " + x + ", x2 = " + x2);
    // Anything inherited is also cloneable:
    Int3 x3 = new Int3(7);
    x3 = (Int3) x3.clone();
    ArrayList v = new ArrayList();
    for (int i = 0; i < 10; i++)
      v.add(new Int2(i));
    System.out.println("v: " + v);
    ArrayList v2 = (ArrayList) v.clone();
    // Now clone each element:
    for (int i = 0; i < v.size(); i++)
      v2.set(i, ((Int2) v2.get(i)).clone());
    // Increment all v2's elements:
    for (Iterator e = v2.iterator(); e.hasNext();)
      ((Int2) e.next()).increment();
    System.out.println("v2: " + v2);
    // See if it changed v's elements:
    System.out.println("v: " + v);
  }
} ///:~
```

1.  A Cloning Example
---  ---
2.  Creating a Deep Copy
3.  Shallow Copy Test
4.  Deep Copy Test
5.  Tests cloning to see if destination of references are also cloned
6.  Creating local copies with clone
7.  You can insert Cloneability at any level of inheritance
8.  Cloning a composed object
9.  Serializable and clone
10.  Checking to see if a reference can be cloned
11.  The clone operation works for only a few items in the standard Java library
12.  Demonstration of cloning
13.  Simple demo of avoiding side-effects by using Object.clone
14.  Clone demo
