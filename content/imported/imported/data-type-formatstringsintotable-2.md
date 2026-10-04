---
title: Format strings into table
nav: Format strings into table
description: Imported from the java2s.com archive: Format strings into table
section: Imported - java2s Archive
order: 1011
source: https://web.archive.org/web/20100410214823/http://java2s.com:80/Tutorial/Java/0040__Data-Type/Formatstringsintotable.htm
---
```java title=Example.java
public class Main {
  public static void main(String args[]) {
    String format = "|%1$-10s|%2$-10s|%3$-20s|\n";
    System.out.format(format, "A", "AA", "AAA");
    System.out.format(format, "B", "", "BBBBB");
    System.out.format(format, "C", "CCCCC", "CCCCCCCC");
    String ex[] = { "E", "EEEEEEEEEE", "E" };
    System.out.format(String.format(format, (Object[]) ex));
  }
}
/*
A  AA  AAA
B    BBBBB
C  CCCCC  CCCCCCCC
E  EEEEEEEEEE  E
*/
```
