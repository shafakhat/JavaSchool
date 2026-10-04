---
title: Demonstration of both constructor and ordinary method overloading
nav: Demonstration of both cons...
description: Demonstration of both constructor and ordinary method overloading
section: Imported - java2s Archive
order: 1010
source: https://web.archive.org/web/20090531122122/http://www.java2s.com:80/Code/Java/Class/Demonstrationofbothconstructorandordinarymethodoverloading.htm
---
Demonstration of both constructor and ordinary method overloading

```java title=Example.java
// : c04:JavaOverloading.java
// Demonstration of both constructor and ordinary method overloading.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
class Tree {
  int height;
  Tree() {
    System.out.println("Planting a seedling");
    height = 0;
  }
  Tree(int i) {
    System.out.println("Creating new Tree that is " + i + " feet tall");
    height = i;
  }
  void info() {
    System.out.println("Tree is " + height + " feet tall");
  }
  void info(String s) {
    System.out.println(s + ": Tree is " + height + " feet tall");
  }
}
public class JavaOverloading {
  public static void main(String[] args) {
    for (int i = 0; i < 5; i++) {
      Tree t = new Tree(i);
      t.info();
      t.info("overloaded method");
    }
    // Overloaded constructor:
    new Tree();
  }
} ///:~
```

1.  Overloaded constructor
---  ---
2.  Overloaded method
3.  Demonstration of overriding fields
4.  Overloading based on the order of the arguments
5.  Promotion of primitives and overloading
6.  Overloading a base-class method name in a derived class does not hide the base-class versions
7.  Demotion of primitives and overloading
