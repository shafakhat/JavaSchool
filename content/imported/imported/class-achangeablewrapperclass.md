---
title: A changeable wrapper class
nav: A changeable wrapper class
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1124
source: https://web.archive.org/web/20090504072712/http://www.java2s.com:80/Code/Java/Class/Achangeablewrapperclass.htm
---
```java title=Example.java
// : appendixa:MutableInteger.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
import java.util.ArrayList;
import java.util.List;
class IntValue {
  private int n;
  public IntValue(int x) {
    n = x;
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
public class MutableInteger {
  public static void main(String[] args) {
    List v = new ArrayList();
    for (int i = 0; i < 10; i++)
      v.add(new IntValue(i));
    System.out.println(v);
    for (int i = 0; i < v.size(); i++)
      ((IntValue) v.get(i)).increment();
    System.out.println(v);
  }
} ///:~
```

1.  Create Object Demo
---  ---
2.  Passing objects to methods may not be what you're used to.
3.  Demonstrates Reference objects
4.  A companion class to modify immutable objects
5.  Objects that cannot be modified are immune to aliasing
6.  Examination of the way the class loader works
