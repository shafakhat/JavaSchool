---
title: using the %t specifier with Formatter.
nav: using the %t specifier wit...
description: Imported from the java2s.com archive: using the %t specifier with Formatter.
section: Imported - java2s Archive
order: 1496
source: https://web.archive.org/web/20140829074700/http://www.java2s.com/Tutorial/Java/0120__Development/usingthetspecifierwithFormatter.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.Formatter;
public class Main {
  public static void main(String[] argv) throws Exception {
    Formatter fmt = new Formatter();
    Calendar cal = Calendar.getInstance();
    // Display 12-hour time format.
    fmt.format("Time using 12-hour clock: %tr\n", cal);
    System.out.println(fmt);
  }
}
//Time using 12-hour clock: 03:00:51 PM
```

| 6.5.1. | Formatting Output with Formatter |
|---|---|
| 6.5.2. | The Format Specifiers |
| 6.5.3. | The %g format specifier causes Formatter to use either %f or %e, whichever is shorter |
| 6.5.4. | Hex: %x, Octal: %o: Integer hexadecimal, Octal integer |
| 6.5.5. | %h: Hash code of the argument |
| 6.5.6. | %a: Floating-point hexadecimal |
| 6.5.7. | Unknown Format Conversion Exception |
| 6.5.8. | Formatter with different data types |
| 6.5.9. | using the %t specifier with Formatter. |
| 6.5.10. | Use Formatter to vertically align numeric values. |
| 6.5.11. | Use Formatter to left-justify strings within a table. |
| 6.5.12. | Using group separators. |
| 6.5.13. | The # symbol shows a digit or nothing if no digit present |
