---
title: Display numbers with commas
nav: Display numbers with commas
description: Imported from the java2s.com archive: Display numbers with commas
section: Imported - java2s Archive
order: 1024
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Displaynumberswithcommas.htm
---
```java title=Example.java
import java.text.DecimalFormat;
publicclass Main {
  publicstaticvoid main(String args[]) {
    double d = 123456.7890;
    DecimalFormat df = new DecimalFormat("#####0.00");
    System.out.println(df.format(d));
  }
}
//123456.79
```
