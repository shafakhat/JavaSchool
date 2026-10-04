---
title: Left shifting as a quick way to multiply by 2
nav: Left shifting as a quick w...
description: Imported from the java2s.com archive: Left shifting as a quick way to multiply by 2
section: Imported - java2s Archive
order: 1163
source: https://web.archive.org/web/20140829084639/http://www.java2s.com/Tutorial/Java/0060__Operators/Leftshiftingasaquickwaytomultiplyby2.htm
---
```java title=Example.java
public class MainClass {
  public static void main(String args[]) {
    int i;
    int num = 0xFFFFFFE;
    for(i=0; i<4; i++) {
      num = num << 1;
      System.out.println(num);
    }
  }
}
java title=Example.java
536870908
1073741816
2147483632
-32
```
