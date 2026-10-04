---
title: Use java.text.DecimalFormat to format integer
nav: Use java.text.DecimalForma...
description: System.out.println(new DecimalFormat("0.#####E0").format(123456));
section: Imported - java2s Archive
order: 1062
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/UsejavatextDecimalFormattoformatinteger.htm
---
```java title=Example.java
import java.text.DecimalFormat;
publicclass Main {
  publicstaticvoid main(String args[]) {
    System.out.println(new DecimalFormat("0.#####E0").format(123456));
  }
}
//1.23456E5
```
