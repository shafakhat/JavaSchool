---
title: DecimalFormat("00.00E0")
nav: DecimalFormat("00.00E0")
description: Imported from the java2s.com archive: DecimalFormat("00.00E0")
section: Imported - java2s Archive
order: 1077
source: https://web.archive.org/web/20100525043915/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/DecimalFormat0000E0.htm
---
```java title=Example.java
import java.text.DecimalFormat;
public class Main {
  public static void main(String[] argv) throws Exception {
    DecimalFormat formatter = new DecimalFormat("00.00E0");
    String s = formatter.format(-1234.567); // -12.35E2
    System.out.println(s);
    s = formatter.format(-.1234567); // -12.35E-2
    System.out.println(s);
  }
}
```
