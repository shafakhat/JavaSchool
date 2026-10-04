---
title: The clone operation works for only a few items in the standard Java library
nav: The clone operation works ...
description: The clone operation works for only a few items in the standard Java library
section: Imported - java2s Archive
order: 1078
source: https://web.archive.org/web/20081009143521/http://www.java2s.com:80/Code/Java/Class/ThecloneoperationworksforonlyafewitemsinthestandardJavalibrary.htm
---
```java title=Example.java
// : appendixa:Cloning.java
// The clone() operation works for only a few
// items in the standard Java library.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
import java.util.ArrayList;
import java.util.Iterator;
class Int {
  private int i;
  public Int(int ii) {
    i = ii;
  }
  public void increment() {
    i++;
  }
  public String toString() {
    return Integer.toString(i);
  }
}
public class Cloning {
  public static void main(String[] args) {
    ArrayList v = new ArrayList();
    for (int i = 0; i < 10; i++)
      v.add(new Int(i));
    System.out.println("v: " + v);
    ArrayList v2 = (ArrayList) v.clone();
    // Increment all v2's elements:
    for (Iterator e = v2.iterator(); e.hasNext();)
      ((Int) e.next()).increment();
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
10.  Go through a few gyrations to add cloning to your own class
11.  Checking to see if a reference can be cloned
12.  Demonstration of cloning
13.  Simple demo of avoiding side-effects by using Object.clone
14.  Clone demo
