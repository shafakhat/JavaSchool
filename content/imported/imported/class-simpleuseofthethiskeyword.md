---
title: Simple use of the this keyword
nav: Simple use of the this key...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1070
source: https://web.archive.org/web/20090530095650/http://www.java2s.com:80/Code/Java/Class/Simpleuseofthethiskeyword.htm
---
Simple use of the this keyword

```java title=Example.java
// : c04:Leaf.java
// Simple use of the "this" keyword.
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
public class Leaf {
  int i = 0;
  Leaf increment() {
    i++;
    return this;
  }
  void print() {
    System.out.println("i = " + i);
  }
  public static void main(String[] args) {
    Leaf x = new Leaf();
    x.increment().increment().increment().print();
  }
} ///:~
```

1.  This shows off the uses of this
2.  Calling constructors with this
