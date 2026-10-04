---
title: Using group separators.
nav: Using group separators.
description: Imported from the java2s.com archive: Using group separators.
section: Imported - java2s Archive
order: 1493
source: https://web.archive.org/web/20140829074934/http://www.java2s.com/Tutorial/Java/0120__Development/Usinggroupseparators.htm
---
```java title=Example.java
import java.util.Formatter;
public class Main {
  public static void main(String[] argv) throws Exception {
    Formatter fmt = new Formatter();
    fmt.format("No group separators: %d\n", 123456789);
    fmt.format("With group separators: %,d\n\n", 123456789);
    System.out.println(fmt);
  }
}
/*No group separators: 123456789
With group separators: 123,456,789
*/
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
