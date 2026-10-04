---
title: new DecimalFormat(abc#)
nav: new DecimalFormat(abc#)
description: Imported from the java2s.com archive: new DecimalFormat(abc#)
section: Imported - java2s Archive
order: 1067
source: https://web.archive.org/web/20100525043958/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/newDecimalFormatabc.htm
---
```java title=Example.java
import java.text.DecimalFormat;
import java.text.Format;
public class Main {
  public static void main(String[] argv) throws Exception {
    Format formatter = new DecimalFormat("'abc'#");
    String s = formatter.format(-1234.567);
    System.out.println(s);
  }
}
// -abc1235
```
