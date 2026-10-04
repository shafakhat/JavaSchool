---
title: Demonstration of both constructor and ordinary method overloading
nav: Demonstration of both cons...
description: System.out.println("Creating new Tree that is " + i + " feet tall");
section: Imported - java2s Archive
order: 1018
source: https://web.archive.org/web/20070707111855/http://www.java2s.com:80/Tutorial/Java/0100__Class-Definition/Demonstrationofbothconstructorandordinarymethodoverloading.htm
---
```java title=Example.java
class MyClass {
  int height;
  MyClass() {
    System.out.println("Planting a seedling");
    height = 0;
  }
  MyClass(int i) {
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
public class MainClass {
  public static void main(String[] args) {
    MyClass t = new MyClass(0);
    t.info();
    t.info("overloaded method");
    // Overloaded constructor:
    new MyClass();
  }
}
```

```java title=Example.java

Creating new Tree that is 0 feet tall
Tree is 0 feet tall
overloaded method: Tree is 0 feet tall
Planting a seedling
```
