---
title: Use java.text.DecimalFormat to format integer
nav: Use java.text.DecimalForma...
description: System.out.println(new DecimalFormat("0.#####E0").format(123456));
section: Imported - java2s Archive
order: 1138
source: https://web.archive.org/web/20100525043640/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/UsejavatextDecimalFormattoformatinteger.htm
---
```java title=Example.java
import java.text.DecimalFormat;
public class Main {
  public static void main(String args[]) {
    System.out.println(new DecimalFormat("0.#####E0").format(123456));
  }
}
//1.23456E5
```
