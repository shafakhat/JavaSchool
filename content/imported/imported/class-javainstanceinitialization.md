---
title: Java Instance Initialization
nav: Java Instance Initialization
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1037
source: https://web.archive.org/web/20100213071107/http://java2s.com/Code/Java/Class/JavaInstanceInitialization.htm
---
Java Instance Initialization

```java title=Example.java
//: c04:Mugs.java
// Java "Instance Initialization."
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Mug {
  Mug(int marker) {
    System.out.println("Mug(" + marker + ")");
  }
  void f(int marker) {
    System.out.println("f(" + marker + ")");
  }
}
public class Mugs {
  Mug c1;
  Mug c2;
  {
    c1 = new Mug(1);
    c2 = new Mug(2);
    System.out.println("c1 & c2 initialized");
  }
  Mugs() {
    System.out.println("Mugs()");
  }
  public static void main(String[] args) {
    System.out.println("Inside main()");
    Mugs x = new Mugs();
  }
} ///:~
```

1.  static Initialization block
---  ---
2.  Initialization block Demo
3.  Shared array
4.  To show that certain things really must be initialized
5.  Initialization order
