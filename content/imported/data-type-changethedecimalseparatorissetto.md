---
title: Change the decimal separator is set to "."
nav: Change the decimal separat...
description: Imported from the java2s.com archive: Change the decimal separator is set to "."
section: Imported - java2s Archive
order: 1012
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Changethedecimalseparatorissetto.htm
---
```java title=Example.java
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
publicclass Main {
  publicstaticvoid main(String args[]) {
    double d = 123456.7890;
    DecimalFormat df = new DecimalFormat("#####0.00");
    DecimalFormatSymbols dfs = df.getDecimalFormatSymbols();
    dfs.setDecimalSeparator('.');
    df.setDecimalFormatSymbols(dfs);
    System.out.println(df.format(d));
  }
}
```
