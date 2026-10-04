---
title: Use Double constructor to convert double primitive type to a Double object.
nav: Use Double constructor to ...
description: Imported from the java2s.com archive: Use Double constructor to convert double primitive type to a Double object.
section: Imported - java2s Archive
order: 1040
source: https://web.archive.org/web/20140323115302/http://www.java2s.com/Tutorial/Java/0040__Data-Type/UseDoubleconstructortoconvertdoubleprimitivetypetoaDoubleobject.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    double d = 10.56;
    Double dObj = new Double(d);
    System.out.println(dObj);
  }
}
```
