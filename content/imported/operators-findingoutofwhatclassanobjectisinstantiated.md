---
title: Finding Out of what Class an Object is Instantiated
nav: Finding Out of what Class ...
description: System.out.println("Object was an instance of the class java.util.Vector");
section: Imported - java2s Archive
order: 1148
source: https://web.archive.org/web/20140217004859/http://www.java2s.com/Tutorial/Java/0060__Operators/FindingOutofwhatClassanObjectisInstantiated.htm
---
```java title=Example.java
import java.util.ArrayList;
import java.util.Vector;
public class Main {
  public static void main(String[] args) {
    Object testObject = new Vector();
    if (testObject instanceof Vector)
      System.out.println("Object was an instance of the class java.util.Vector");
    else if (testObject instanceof ArrayList)
      System.out.println("Object was an instance of the class java.util.ArrayList");
    else
      System.out.println("Object was an instance of the " + testObject.getClass());
  }
}
//Object was an instance of the class java.util.Vector
```
