---
title: Inheritance and upcasting.
nav: Inheritance and upcasting.
description: Imported from the java2s.com archive: Inheritance and upcasting.
section: Imported - java2s Archive
order: 1290
source: https://web.archive.org/web/20140829075215/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/Inheritanceandupcasting.htm
---
```java title=Example.java
class A {
  public void play() {
  }
  static void tune(A i) {
    i.play();
  }
}
// Wind objects are instruments
// because they have the same interface:
class B extends A {
}
public class MainClass {
  public static void main(String[] args) {
    B flute = new B();
    A.tune(flute); // Upcasting
  }
}
```
