---
title: DecimalFormat("000E00")
nav: DecimalFormat("000E00")
description: Imported from the java2s.com archive: DecimalFormat("000E00")
section: Imported - java2s Archive
order: 1078
source: https://web.archive.org/web/20100525043922/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/DecimalFormat000E00.htm
---
```java title=Example.java
import java.text.DecimalFormat;
public class Main {
  public static void main(String[] argv) throws Exception {
    DecimalFormat formatter = new DecimalFormat("000E00");
    String s = formatter.format(-1234.567); // -123E01
    System.out.println(s);
  }
}
```
