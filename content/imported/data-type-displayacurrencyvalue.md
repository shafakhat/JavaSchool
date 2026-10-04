---
title: Display a currency value
nav: Display a currency value
description: Imported from the java2s.com archive: Display a currency value
section: Imported - java2s Archive
order: 1088
source: https://web.archive.org/web/20111105182113/http://java2s.com/Tutorial/Java/0040__Data-Type/Displayacurrencyvalue.htm
---
```java title=Example.java
import java.text.DecimalFormat;
public class Main {
  public static void main(String[] argv) throws Exception {
    DecimalFormat df = new DecimalFormat("\u00a4#,##0.00");
    System.out.println(df.format(4232.19));
    System.out.println(df.format(-4232.19));
  }
}
```
