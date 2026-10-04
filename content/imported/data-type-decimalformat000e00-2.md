---
title: DecimalFormat("000E00")
nav: DecimalFormat("000E00")
description: Imported from the java2s.com archive: DecimalFormat("000E00")
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DecimalFormat000E00.htm
---
```java title=Example.java
import java.text.DecimalFormat;
publicclass Main {
  publicstaticvoid main(String[] argv) throws Exception {
    DecimalFormat formatter = new DecimalFormat("000E00");
    String s = formatter.format(-1234.567); // -123E01
    System.out.println(s);
  }
}
```
