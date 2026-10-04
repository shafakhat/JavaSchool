---
title: Unknown Format Conversion Exception
nav: Unknown Format Conversion ...
description: Exception in thread "main" java.util.UnknownFormatConversionException: Conversion = 't'
section: Imported - java2s Archive
order: 1481
source: https://web.archive.org/web/20140829074754/http://www.java2s.com/Tutorial/Java/0120__Development/UnknownFormatConversionException.htm
---
```java title=Example.java
import java.util.Date;
import java.util.Formatter;
public class MainClass {
  public static void main(String args[]) {
    Formatter fmt = new Formatter();
    fmt.format("%t", new Date());
    System.out.println(fmt);
  }
}
java title=Example.java
Exception in thread "main" java.util.UnknownFormatConversionException: Conversion = 't'
  at java.util.Formatter$FormatSpecifier.(Formatter.java:2646)
  at java.util.Formatter.parse(Formatter.java:2477)
  at java.util.Formatter.format(Formatter.java:2411)
  at java.util.Formatter.format(Formatter.java:2364)
  at MainClass.main(MainClass.java:8)
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
