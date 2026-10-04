---
title: Initialization order
nav: Initialization order
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1032
source: https://web.archive.org/web/20100213071200/http://java2s.com/Code/Java/Class/Initializationorder.htm
---
```java title=Example.java
// : c04:OrderOfInitialization.java
// Demonstrates initialization order.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
// When the constructor is called to create a
// Tag object, you'll see a message:
class Tag {
  Tag(int marker) {
    System.out.println("Tag(" + marker + ")");
  }
}
class Card {
  Tag t1 = new Tag(1); // Before constructor
  Card() {
    // Indicate we're in the constructor:
    System.out.println("Card()");
    t3 = new Tag(33); // Reinitialize t3
  }
  Tag t2 = new Tag(2); // After constructor
  void f() {
    System.out.println("f()");
  }
  Tag t3 = new Tag(3); // At end
}
public class OrderOfInitialization {
  public static void main(String[] args) {
    Card t = new Card();
    t.f(); // Shows that construction is done
  }
} ///:~
```

1.  static Initialization block
---  ---
2.  Initialization block Demo
3.  Shared array
4.  To show that certain things really must be initialized
5.  Java Instance Initialization
