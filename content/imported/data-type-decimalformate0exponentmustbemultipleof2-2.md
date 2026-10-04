---
title: DecimalFormat("##E0") (exponent must be multiple of 2)
nav: DecimalFormat("##E0") (exp...
description: Imported from the java2s.com archive: DecimalFormat("##E0") (exponent must be multiple of 2)
section: Imported - java2s Archive
order: 1028
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DecimalFormatE0exponentmustbemultipleof2.htm
---
```java title=Example.java
import java.text.DecimalFormat;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    DecimalFormat formatter = new DecimalFormat("##E0");
    String s = formatter.format(-1234.567);
    System.out.println(s);
    s = formatter.format(-123.4567);
    System.out.println(s);
    s = formatter.format(-12.34567);
    System.out.println(s);
  }
}
// -12E2
// -1.2E2
// -12E0
```
