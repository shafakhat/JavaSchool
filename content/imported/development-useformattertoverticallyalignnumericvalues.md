---
title: Use Formatter to vertically align numeric values.
nav: Use Formatter to verticall...
description: Imported from the java2s.com archive: Use Formatter to vertically align numeric values.
section: Imported - java2s Archive
order: 1480
source: https://web.archive.org/web/20140829074742/http://www.java2s.com/Tutorial/Java/0120__Development/UseFormattertoverticallyalignnumericvalues.htm
---
```java title=Example.java
import java.util.Formatter;
public class Main {
  public static void main(String[] argv) throws Exception {
    double data[] = { 12.3, 45.6, -7.89, -1.0, 1.01 };
    Formatter fmt = new Formatter();
    fmt.format("%12s %12s\n", "Value", "Cube Root");
    for (double v : data) {
      fmt.format("%12.4f %12.4f\n", v, Math.cbrt(v));
    }
    System.out.println(fmt);
  }
}
/*       Value    Cube Root
     12.3000       2.3084
     45.6000       3.5726
     -7.8900      -1.9908
     -1.0000      -1.0000
      1.0100       1.0033
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
