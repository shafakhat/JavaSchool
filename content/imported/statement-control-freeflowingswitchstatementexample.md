---
title: Free Flowing Switch Statement Example
nav: Free Flowing Switch Statem...
description: Imported from the java2s.com archive: Free Flowing Switch Statement Example
section: Imported - java2s Archive
order: 1174
source: https://web.archive.org/web/20140829080930/http://www.java2s.com/Tutorial/Java/0080__Statement-Control/FreeFlowingSwitchStatementExample.htm
---
```java title=Example.java
public class Main {
  public static void main(String[] args) {
    int i = 0;
    switch (i) {
    case 0:
      System.out.println("i is 0");
    case 1:
      System.out.println("i is 1");
    case 2:
      System.out.println("i is 2");
    default:
      System.out.println("Free flowing switch example!");
    }
  }
}
/*
i is 0
i is 1
i is 2
Free flowing switch example!
*/
```
