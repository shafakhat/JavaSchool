---
title: Demonstrate the %g format specifier.
nav: Demonstrate the %g format ...
description: Imported from the java2s.com archive: Demonstrate the %g format specifier.
section: Imported - java2s Archive
order: 1538
source: https://web.archive.org/web/20140829090635/http://www.java2s.com/Tutorial/Java/0120__Development/Demonstratethegformatspecifier.htm
---
```java title=Example.java
import java.util.Formatter;
public class Main{
  public static void main(String args[]) {
    Formatter fmt = new Formatter();
    for (double i = 1000; i < 1.0e+10; i *= 100) {
      fmt.format("%g ", i);
      System.out.println(fmt);
    }
  }
}
/*
1000.00
1000.00 100000
1000.00 100000 1.00000e+07
1000.00 100000 1.00000e+07 1.00000e+09
*/
```

| 6.6.1. | Using the Format Flags |
|---|---|
| 6.6.2. | The %n inserts a newline: the %n and %% format specifiers |
| 6.6.3. | Left justification |
| 6.6.4. | The Space, +, 0, and '(' Flags: To show a '+' sign before positive numeric values, add the + flag |
| 6.6.5. | Demonstrating the space format specifiers |
| 6.6.6. | To show negative numeric output inside parentheses, rather than with a leading -, use the '(' flag |
| 6.6.7. | The 0 flag |
| 6.6.8. | The Comma Flag(,) : to add grouping specifiers |
| 6.6.9. | The # Flag |
| 6.6.10. | format: %#x |
| 6.6.11. | format: %#o |
| 6.6.12. | Demonstrate the %g format specifier. |
