---
title: Static field, constructor and exception
nav: Static field, constructor ...
description: Imported from the java2s.com archive: Static field, constructor and exception
section: Imported - java2s Archive
order: 1072
source: https://web.archive.org/web/20090602111630/http://www.java2s.com:80/Code/Java/Class/Staticfieldconstructorandexception.htm
---
```java title=Example.java
public class Main {
  static Bar bar;
  static {
    try {
      bar = new Bar();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
  public static void main(String[] argv) {
    System.out.println(bar);
  }
}
class Bar {
  public Bar() throws Exception {
  }
  public String toString() {
    return "Bar";
  }
}
```

1.  Java static member variable example
---  ---
2.  Java static method
3.  Using Static Variables
4.  Static Init Demo
5.  Show that you do inherit static fields
6.  Show that you can't have static variables in a method
7.  Explicit static initialization with the static clause
