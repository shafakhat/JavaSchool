---
title: new DecimalFormat("0.######E0")
nav: new DecimalFormat("0.#####...
description: System.out.println(new DecimalFormat("0.######E0").format(12345));
section: Imported - java2s Archive
order: 1159
source: https://web.archive.org/web/20100523024821/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/newDecimalFormat0E0.htm
---
```java title=Example.java
import java.text.DecimalFormat;
public class Main {
  public static void main(String args[]) {
    System.out.println(new DecimalFormat("0.######E0").format(12345));
  }
}
//1.2345E4
```
