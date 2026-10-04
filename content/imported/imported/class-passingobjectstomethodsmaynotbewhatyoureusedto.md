---
title: Passing objects to methods may not be what you're used to.
nav: Passing objects to methods...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1057
source: https://web.archive.org/web/20090504072516/http://www.java2s.com:80/Code/Java/Class/Passingobjectstomethodsmaynotbewhatyoureusedto.htm
---
```java title=Example.java
//: c03:PassObject.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Letter {
  char c;
}
public class PassObject {
  static void f(Letter y) {
    y.c = 'z';
  }
  public static void main(String[] args) {
    Letter x = new Letter();
    x.c = 'a';
    System.out.println("1: x.c: " + x.c);
    f(x);
    System.out.println("2: x.c: " + x.c);
  }
} ///:~
```

1.  Create Object Demo
---  ---
2.  Demonstrates Reference objects
3.  A companion class to modify immutable objects
4.  Objects that cannot be modified are immune to aliasing
5.  Examination of the way the class loader works
6.  A changeable wrapper class
