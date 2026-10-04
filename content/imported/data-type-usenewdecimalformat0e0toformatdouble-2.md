---
title: Use new DecimalFormat("0.#####E0") to format double
nav: Use new DecimalFormat("0.#...
description: System.out.println(new DecimalFormat("0.#####E0").format(d));
section: Imported - java2s Archive
order: 1042
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/UsenewDecimalFormat0E0toformatdouble.htm
---
```java title=Example.java
import java.text.DecimalFormat;
publicclass Main {
  publicstaticvoid main(String args[]) {
    double d = 0.12345;
    System.out.println(new DecimalFormat("0.#####E0").format(d));
  }
}
//1.2345E-1
```
