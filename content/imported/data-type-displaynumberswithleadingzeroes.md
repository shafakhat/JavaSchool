---
title: Display numbers with leading zeroes
nav: Display numbers with leadi...
description: Imported from the java2s.com archive: Display numbers with leading zeroes
section: Imported - java2s Archive
order: 1092
source: https://web.archive.org/web/20100525043937/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/Displaynumberswithleadingzeroes.htm
---
```java title=Example.java
import java.text.DecimalFormat;
public class Main {
  public static void main(String args[]) {
    DecimalFormat df = new DecimalFormat("0000000000000000");
    String z = df.format(123456);
    System.out.println(z);
  }
}
```
