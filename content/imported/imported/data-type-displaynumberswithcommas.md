---
title: Display numbers with commas
nav: Display numbers with commas
description: Imported from the java2s.com archive: Display numbers with commas
section: Imported - java2s Archive
order: 1091
source: https://web.archive.org/web/20100525043932/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Displaynumberswithcommas.htm
---
```java title=Example.java
import java.text.DecimalFormat;
public class Main {
  public static void main(String args[]) {
    double d = 123456.7890;
    DecimalFormat df = new DecimalFormat("#####0.00");
    System.out.println(df.format(d));
  }
}
//123456.79
```
