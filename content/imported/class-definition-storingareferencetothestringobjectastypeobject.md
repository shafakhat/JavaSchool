---
title: Storing a reference to the String object as type Object
nav: Storing a reference to the...
description: A variable of type Object can store a reference to an object of any class type.
section: Imported - java2s Archive
order: 1248
source: https://web.archive.org/web/20140829085856/http://www.java2s.com/Tutorial/Java/0100__Class-Definition/StoringareferencetotheStringobjectastypeObject.htm
---
A variable of type Object can store a reference to an object of any class type.

```java title=Example.java
public class MainClass {
  public static void main(String[] a) {
    String saying = "A stitch in time saves nine.";
    Object str = saying;
    System.out.println(str);
    System.out.println(str.getClass().getName());
  }
}
java title=Example.java
A stitch in time saves nine.
java.lang.String
```
