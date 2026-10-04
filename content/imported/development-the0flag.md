---
title: The 0 flag
nav: The 0 flag
description: The 0 flag causes output to be padded with zeros rather than spaces.
section: Imported - java2s Archive
order: 1520
source: https://web.archive.org/web/20140829090807/http://www.java2s.com/Tutorial/Java/0120__Development/The0flag.htm
---
The 0 flag causes output to be padded with zeros rather than spaces.
The 0 flag can be used with all format specifiers except %n.

```java title=Example.java
import java.util.Formatter;
public class MainClass {
  public static void main(String args[]) {
    Formatter fmt = new Formatter();
    fmt.format("%05d", 100);
    System.out.println(fmt);
  }
}
java title=Example.java
00100
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
