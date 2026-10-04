---
title: Left justification
nav: Left justification
description: Imported from the java2s.com archive: Left justification
section: Imported - java2s Archive
order: 1511
source: https://web.archive.org/web/20140829090847/http://www.java2s.com/Tutorial/Java/0120__Development/Leftjustification.htm
---
| By default, all output is right-justified. |
|---|
| You can force output to be left-justified by placing a minus sign directly after the %. |
| For example, %-10.2f left-justifies a floating-point number with two decimal places in a ten-character field. |

```java title=Example.java
import java.util.*;
public class MainClass {
  public static void main(String args[]) {
    Formatter fmt = new Formatter();
    // Right justify by default.
    fmt.format("|%10.2f|", 123.123);
    System.out.println(fmt);
    // Now, left justify.
    fmt = new Formatter();
    fmt.format("|%-10.2f|", 123.123);
    System.out.println(fmt);
  }
}
java title=Example.java
|    123.12|
|123.12    |
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
