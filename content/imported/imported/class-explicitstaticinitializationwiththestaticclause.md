---
title: Explicit static initialization with the static clause
nav: Explicit static initializa...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20090602110626/http://www.java2s.com:80/Code/Java/Class/Explicitstaticinitializationwiththestaticclause.htm
---
```java title=Example.java
// : c04:ExplicitStatic.java
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Cup {
  Cup(int marker) {
    System.out.println("Cup(" + marker + ")");
  }
  void f(int marker) {
    System.out.println("f(" + marker + ")");
  }
}
class Cups {
  static Cup c1;
  static Cup c2;
  static {
    c1 = new Cup(1);
    c2 = new Cup(2);
  }
  Cups() {
    System.out.println("Cups()");
  }
}
public class ExplicitStatic {
  public static void main(String[] args) {
    System.out.println("Inside main()");
    Cups.c1.f(99); // (1)
  }
  // static Cups x = new Cups(); // (2)
  // static Cups y = new Cups(); // (2)
} ///:~
```

1.  Java static member variable example
---  ---
2.  Java static method
3.  Using Static Variables
4.  Static Init Demo
5.  Show that you do inherit static fields
6.  Show that you can't have static variables in a method
7.  Static field, constructor and exception
