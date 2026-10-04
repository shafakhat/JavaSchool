---
title: Applied to strings, the precision specifier specifies the maximum field length
nav: Applied to strings, the pr...
description: For example, %5.7s displays a string at least five and not exceeding seven characters long. If the string is longer than the maximum field width, the end characters will
section: Imported - java2s Archive
order: 1009
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Appliedtostringstheprecisionspecifierspecifiesthemaximumfieldlength.htm
---
For example, %5.7s displays a string at least five and not exceeding seven characters long. If the string is longer than the maximum field width, the end characters will be truncated.

```java title=Example.java
import java.util.Formatter;
publicclass MainClass {
  publicstaticvoid main(String args[]) {
    Formatter fmt;
    fmt = new Formatter();
    fmt.format("%5.7s", "abcdefghijklmn");
    System.out.println(fmt);
    fmt = new Formatter();
    fmt.format("%5.7s", "abc");
    System.out.println(fmt);
  }
}
```

```java title=Example.java
abcdefg
abc
```
