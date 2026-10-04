---
title: Convert Java String Object to Boolean Object
nav: Convert Java String Object...
description: // Use valueOf method of Boolean class. This is a static method.
section: Imported - java2s Archive
order: 1001
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertJavaStringObjecttoBooleanObject.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    String str = "false";
    // Convert using constructor
    Boolean blnObj1 = new Boolean(str);
    System.out.println(blnObj1);
    // Use valueOf method of Boolean class. This is a static method.
    Boolean blnObj2 = Boolean.valueOf(str);
    System.out.println(blnObj2);
  }
}
```
