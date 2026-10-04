---
title: Overloading based on the order of the arguments
nav: Overloading based on the o...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1055
source: https://web.archive.org/web/20090531123200/http://www.java2s.com:80/Code/Java/Class/Overloadingbasedontheorderofthearguments.htm
---
Overloading based on the order of the arguments

```java title=Example.java
// : c04:OverloadingOrder.java
// Overloading based on the order of the arguments.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
public class OverloadingOrder {
  static void print(String s, int i) {
    System.out.println("String: " + s + ", int: " + i);
  }
  static void print(int i, String s) {
    System.out.println("int: " + i + ", String: " + s);
  }
  public static void main(String[] args) {
    print("String first", 11);
    print(99, "Int first");
  }
} ///:~
```

1.  Demonstration of both constructor and ordinary method overloading
---  ---
2.  Overloaded constructor
3.  Overloaded method
4.  Demonstration of overriding fields
5.  Promotion of primitives and overloading
6.  Overloading a base-class method name in a derived class does not hide the base-class versions
7.  Demotion of primitives and overloading
