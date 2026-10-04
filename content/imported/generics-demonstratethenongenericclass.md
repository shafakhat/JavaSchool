---
title: Demonstrate the non generic class
nav: Demonstrate the non generi...
description: 2. Stats attempts (unsuccessfully) to create a generic class
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/20090409005922/http://www.java2s.com:80/Code/Java/Generics/Demonstratethenongenericclass.htm
---
Demonstrate the non generic class

```java title=Example.java
class NonGen {
  Object ob;
  NonGen(Object o) {
    ob = o;
  }
  Object getob() {
    return ob;
  }
  void showType() {
    System.out.println("Type of ob is " +
                       ob.getClass().getName());
  }
}
public class NonGenDemo {
  public static void main(String args[]) {
    NonGen integerObject;
    integerObject = new NonGen(88);
    integerObject.showType();
    int v = (Integer) integerObject.getob();
    System.out.println("value: " + v);
    NonGen strOb = new NonGen("Non-Generics Test");
    strOb.showType();
    String str = (String) strOb.getob();
    System.out.println("value: " + str);
    integerObject = strOb;
    v = (Integer) integerObject.getob();
  }
}
```

1.  A simple generic class.
---  ---
2.  Stats attempts (unsuccessfully) to create a generic class
3.  A simple generic class heirarchy.
4.  A nongeneric class can be the superclass of a generic subclass.
5.  Use the instanceof operator with a generic class hierarchy.
6.  Java hierarchy generic class
7.  Custom Generic Object Tester
