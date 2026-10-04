---
title: Java static member variable example
nav: Java static member variabl...
description: Imported from the java2s.com archive: Java static member variable example
section: Imported - java2s Archive
order: 1038
source: https://web.archive.org/web/20090602102402/http://www.java2s.com:80/Code/Java/Class/Javastaticmembervariableexample.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    Counter object1 = new Counter();
    System.out.println(object1.getNumberOfObjects());
    Counter object2 = new Counter();
    System.out.println(object2.getNumberOfObjects());
  }
}
class Counter {
  static int counter = 0;
  public Counter() {
    counter++;
  }
  public int getNumberOfObjects() {
    return counter;
  }
}
```

1.  Java static method
---  ---
2.  Using Static Variables
3.  Static Init Demo
4.  Show that you do inherit static fields
5.  Show that you can't have static variables in a method
6.  Explicit static initialization with the static clause
7.  Static field, constructor and exception
