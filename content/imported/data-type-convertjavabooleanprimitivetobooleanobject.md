---
title: Convert Java boolean Primitive to Boolean object
nav: Convert Java boolean Primi...
description: Imported from the java2s.com archive: Convert Java boolean Primitive to Boolean object
section: Imported - java2s Archive
order: 1029
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertJavabooleanPrimitivetoBooleanobject.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    boolean b = true;
    // using constructor
    Boolean blnObj1 = new Boolean(b);
    // using valueOf method of Boolean class.
    Boolean blnObj2 = Boolean.valueOf(b);
  }
}
```
