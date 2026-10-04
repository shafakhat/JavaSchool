---
title: Specifying Precision
nav: Specifying Precision
description: Imported from the java2s.com archive: Specifying Precision
section: Imported - java2s Archive
order: 1311
source: https://web.archive.org/web/20140119064900/http://www.java2s.com/Tutorial/Java/0040__Data-Type/SpecifyingPrecision.htm
---
| A precision specifier can be applied to the %f, %e, %g, and %s format specifiers. |
|---|
| When applying to floating-point data using the %f, %e, or %g specifiers, it determines the number of decimal places displayed. |
| The default precision is 6. |
| For example, %10.4f displays a number at least ten characters wide with four decimal places. |

```java title=Example.java
import java.util.Formatter;
public class MainClass {
  public static void main(String args[]) {
    Formatter fmt;
    fmt = new Formatter();
    fmt.format("%1.4f", 1234567890.123456789);
    System.out.println(fmt);
  }
}
java title=Example.java
1234567890.1235
```

| 2.14.1. | Number formatting helps make your numbers more readable. |
|---|---|
| 2.14.2. | Specifying Precision |
| 2.14.3. | Applied to strings, the precision specifier specifies the maximum field length |
| 2.14.4. | Illustrating the precision specifier |
| 2.14.5. | Add leading zeros to a number |
| 2.14.6. | NumberFormat.getInstance() |
| 2.14.7. | NumberFormat.getCurrencyInstance(Locale.ENGLISH) |
| 2.14.8. | NumberFormat: Minimum Integer Digits, Maximum/Minimum Fraction Digits |
| 2.14.9. | Number format with FieldPosition |
| 2.14.10. | NumberFormat.getPercentInstance(Locale.ENGLISH) |
| 2.14.11. | A number formatter for logarithmic values. This formatter does not support parsing. |
| 2.14.12. | Format a percentage for presentation to the user |
| 2.14.13. | Get Percent Value |
| 2.14.14. | Helper class for format number and currency |
