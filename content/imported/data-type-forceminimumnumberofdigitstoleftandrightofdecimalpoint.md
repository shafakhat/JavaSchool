---
title: Force minimum number of digits to left and right of decimal point
nav: Force minimum number of di...
description: Imported from the java2s.com archive: Force minimum number of digits to left and right of decimal point
section: Imported - java2s Archive
order: 1103
source: https://web.archive.org/web/20111105193609/http://java2s.com/Tutorial/Java/0040__Data-Type/Forceminimumnumberofdigitstoleftandrightofdecimalpoint.htm
---
```java title=Example.java
import java.text.DecimalFormat;
public class Main {
  public static void main(String[] argv) throws Exception {
    DecimalFormat formatter = new DecimalFormat("0.0E0");
    String s = formatter.format(-1234.567); // -1.2E3
    System.out.println(s);
  }
}
```
