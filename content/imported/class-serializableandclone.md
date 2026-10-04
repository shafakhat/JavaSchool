---
title: Serializable and clone
nav: Serializable and clone
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1066
source: https://web.archive.org/web/20081009143501/http://www.java2s.com:80/Code/Java/Class/Serializableandclone.htm
---
```java title=Example.java
// : appendixa:Compete.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
class Thing1 implements Serializable {
}
class Thing2 implements Serializable {
  Thing1 o1 = new Thing1();
}
class Thing3 implements Cloneable {
  public Object clone() {
    Object o = null;
    try {
      o = super.clone();
    } catch (CloneNotSupportedException e) {
      System.err.println("Thing3 can't clone");
    }
    return o;
  }
}
class Thing4 implements Cloneable {
  private Thing3 o3 = new Thing3();
  public Object clone() {
    Thing4 o = null;
    try {
      o = (Thing4) super.clone();
    } catch (CloneNotSupportedException e) {
      System.err.println("Thing4 can't clone");
    }
    // Clone the field, too:
    o.o3 = (Thing3) o3.clone();
    return o;
  }
}
public class Compete {
  public static final int SIZE = 25000;
  public static void main(String[] args) throws Exception {
    Thing2[] a = new Thing2[SIZE];
    for (int i = 0; i < a.length; i++)
      a[i] = new Thing2();
    Thing4[] b = new Thing4[SIZE];
    for (int i = 0; i < b.length; i++)
      b[i] = new Thing4();
    long t1 = System.currentTimeMillis();
    ByteArrayOutputStream buf = new ByteArrayOutputStream();
    ObjectOutputStream o = new ObjectOutputStream(buf);
    for (int i = 0; i < a.length; i++)
      o.writeObject(a[i]);
    // Now get copies:
    ObjectInputStream in = new ObjectInputStream(new ByteArrayInputStream(
        buf.toByteArray()));
    Thing2[] c = new Thing2[SIZE];
    for (int i = 0; i < c.length; i++)
      c[i] = (Thing2) in.readObject();
    long t2 = System.currentTimeMillis();
    System.out.println("Duplication via serialization: " + (t2 - t1)
        + " Milliseconds");
    // Now try cloning:
    t1 = System.currentTimeMillis();
    Thing4[] d = new Thing4[SIZE];
    for (int i = 0; i < d.length; i++)
      d[i] = (Thing4) b[i].clone();
    t2 = System.currentTimeMillis();
    System.out.println("Duplication via cloning: " + (t2 - t1)
        + " Milliseconds");
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
9.  Go through a few gyrations to add cloning to your own class
10.  Checking to see if a reference can be cloned
11.  The clone operation works for only a few items in the standard Java library
12.  Demonstration of cloning
13.  Simple demo of avoiding side-effects by using Object.clone
14.  Clone demo
