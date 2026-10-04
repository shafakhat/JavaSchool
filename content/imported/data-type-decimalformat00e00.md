---
title: DecimalFormat("00E00")
nav: DecimalFormat("00E00")
description: Imported from the java2s.com archive: DecimalFormat("00E00")
section: Imported - java2s Archive
order: 1033
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DecimalFormat00E00.htm
---
```java title=Example.java
import java.text.DecimalFormat;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    DecimalFormat formatter = new DecimalFormat("00E00");
    String s = formatter.format(-1234.567);
    System.out.println(s);
  }
}
// -12E02
```
