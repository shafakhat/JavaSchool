---
title: DecimalFormat("###E0") (exponent must be multiple of 3)
nav: DecimalFormat("###E0") (ex...
description: Imported from the java2s.com archive: DecimalFormat("###E0") (exponent must be multiple of 3)
section: Imported - java2s Archive
order: 1080
source: https://web.archive.org/web/20100402235318/http://www.java2s.com:80/Tutorial/Java/0040__Data-Type/DecimalFormatE0exponentmustbemultipleof3.htm
---
```java title=Example.java
import java.text.DecimalFormat;
public class Main {
  public static void main(String[] argv) {
    DecimalFormat formatter = new DecimalFormat("###E0");
    String s = formatter.format(-1234.567); // -1.23E3
    System.out.println(s);
    s = formatter.format(-123.4567); // -123E0
    System.out.println(s);
    s = formatter.format(-12.34567); // -12.3E0
    System.out.println(s);
    s = formatter.format(-1.234567); // -12.3E0
    System.out.println(s);
    s = formatter.format(-.1234567); // -123E-3
    System.out.println(s);
  }
}
```
