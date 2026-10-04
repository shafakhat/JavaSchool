---
title: Convert an int value to String
nav: Convert an int value to St...
description: System.out.println(str + " : " + Integer.toString(i).getClass());
section: Imported - java2s Archive
order: 1025
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertanintvaluetoStringIntegertoStringi.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    int i = 50;
    String str = Integer.toString(i);
    System.out.println(str + " : " + Integer.toString(i).getClass());
  }
}
//50 : class java.lang.String
```
