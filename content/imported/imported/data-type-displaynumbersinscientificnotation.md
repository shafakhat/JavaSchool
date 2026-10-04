---
title: Display numbers in scientific notation
nav: Display numbers in scienti...
description: Imported from the java2s.com archive: Display numbers in scientific notation
section: Imported - java2s Archive
order: 1090
source: https://web.archive.org/web/20100525043626/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Displaynumbersinscientificnotation.htm
---
```java title=Example.java
import java.text.DecimalFormat;
import java.text.NumberFormat;
public class Main {
  public static void main(String args[]) {
    NumberFormat formatter = new DecimalFormat();
    int maxinteger = Integer.MAX_VALUE;
    formatter = new DecimalFormat("0.######E0");
    System.out.println(formatter.format(maxinteger));
  }
}
//2.147484E9
```
