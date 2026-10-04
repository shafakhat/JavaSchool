---
title: Convert boolean value to Boolean
nav: Convert boolean value to B...
description: Imported from the java2s.com archive: Convert boolean value to Boolean
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertbooleanvaluetoBoolean.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    boolean b = true;
    Boolean bool = Boolean.valueOf(b);
    System.out.println("bool = " + bool);
    if (bool.equals(Boolean.TRUE)) {
      System.out.println("bool = " + bool);
    }
    String s = "false";
    Boolean bools = Boolean.valueOf(s);
    System.out.println("bools = " + bools);
    String f = "abc";
    Boolean abc = Boolean.valueOf(f);
    System.out.println("abc = " + abc);
  }
}
```
