---
title: Calling constructors with this
nav: Calling constructors with ...
description: // www.BruceEckel.com. See copyright notice in CopyRight.txt.
section: Imported - java2s Archive
order: 1136
source: https://web.archive.org/web/20090903024258/http://www.java2s.com:80/Code/Java/Class/Callingconstructorswiththis.htm
---
Calling constructors with this

```java title=Example.java
// : c04:Flower.java
// Calling constructors with "this."
// From 'Thinking in Java, 3rd ed.' (c) Bruce Eckel 2002
// www.BruceEckel.com. See copyright notice in CopyRight.txt.
public class Flower {
  int petalCount = 0;
  String s = new String("null");
  Flower(int petals) {
    petalCount = petals;
    System.out.println("Constructor w/ int arg only, petalCount= "
        + petalCount);
  }
  Flower(String ss) {
    System.out.println("Constructor w/ String arg only, s=" + ss);
    s = ss;
  }
  Flower(String s, int petals) {
    this(petals);
    //! this(s); // Can't call two!
    this.s = s; // Another use of "this"
    System.out.println("String & int args");
  }
  Flower() {
    this("hi", 47);
    System.out.println("default constructor (no args)");
  }
  void print() {
    //! this(11); // Not inside non-constructor!
    System.out.println("petalCount = " + petalCount + " s = " + s);
  }
  public static void main(String[] args) {
    Flower x = new Flower();
    x.print();
  }
} ///:~
```

1.  Simple use of the this keyword
2.  This shows off the uses of this
