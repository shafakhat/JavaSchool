---
title: Convert an int value to String
nav: Convert an int value to St...
description: System.out.println(str + " : " + new Integer(i).toString().getClass());
section: Imported - java2s Archive
order: 1026
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/ConvertanintvaluetoStringnewIntegeritoString.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    int i = 50;
    String str = new Integer(i).toString();
    System.out.println(str + " : " + new Integer(i).toString().getClass());
  }
}
//50 : class java.lang.String
```
