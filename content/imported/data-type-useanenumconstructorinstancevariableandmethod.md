---
title: Use an enum constructor, instance variable, and method.
nav: Use an enum constructor, i...
description: System.out.println("D costs " + Apple.D.getPrice() + " cents.\n");
section: Imported - java2s Archive
order: 1096
source: https://web.archive.org/web/20140829083644/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Useanenumconstructorinstancevariableandmethod.htm
---
```java title=Example.java
enum Apple {
  A(10), B(9), C(12), D(15), E(8);
  private int price; // price of each apple
  Apple(int p) {
    price = p;
  }
  int getPrice() {
    return price;
  }
}
class EnumDemo3 {
  public static void main(String args[]) {
    Apple ap;
    System.out.println("D costs " + Apple.D.getPrice() + " cents.\n");
    System.out.println("All apple prices:");
    for (Apple a : Apple.values())
      System.out.println(a + " costs " + a.getPrice() + " cents.");
  }
}
```
