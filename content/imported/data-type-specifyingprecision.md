---
title: Specifying Precision
nav: Specifying Precision
description: A precision specifier can be applied to the %f, %e, %g, and %s format specifiers.
section: Imported - java2s Archive
order: 1051
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SpecifyingPrecision.htm
---
A precision specifier can be applied to the %f, %e, %g, and %s format specifiers.

When applying to floating-point data using the %f, %e, or %g specifiers, it determines the number of decimal places displayed.

The default precision is 6.

For example, %10.4f displays a number at least ten characters wide with four decimal places.

```java title=Example.java
import java.util.Formatter;
publicclass MainClass {
  publicstaticvoid main(String args[]) {
    Formatter fmt;
    fmt = new Formatter();
    fmt.format("%1.4f", 1234567890.123456789);
    System.out.println(fmt);
  }
}
```

```java title=Example.java
1234567890.1235
```
