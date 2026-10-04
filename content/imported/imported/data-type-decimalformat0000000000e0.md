---
title: DecimalFormat("0000000000E0")
nav: DecimalFormat("0000000000E...
description: Imported from the java2s.com archive: DecimalFormat("0000000000E0")
section: Imported - java2s Archive
order: 1076
source: https://web.archive.org/web/20100525043610/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/DecimalFormat0000000000E0.htm
---
```java title=Example.java
import java.text.DecimalFormat;
public class Main {
  public static void main(String[] argv) throws Exception {
    DecimalFormat formatter = new DecimalFormat("0000000000E0");
    String s = formatter.format(-1234.567); // -1234567000E-6
    System.out.println(s);
  }
}
```
