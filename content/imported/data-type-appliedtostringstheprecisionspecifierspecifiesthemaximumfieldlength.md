---
title: Applied to strings, the precision specifier specifies the maximum field length
nav: Applied to strings, the pr...
description: For example, %5.7s displays a string at least five and not exceeding seven characters long. If the string is longer than the maximum field width, the end characters will
section: Imported - java2s Archive
order: 1288
source: https://web.archive.org/web/20140121010916/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Appliedtostringstheprecisionspecifierspecifiesthemaximumfieldlength.htm
---
For example, %5.7s displays a string at least five and not exceeding seven characters long. If the string is longer than the maximum field width, the end characters will be truncated.

```java title=Example.java
import java.util.Formatter;
public class MainClass {
  public static void main(String args[]) {
    Formatter fmt;
    fmt = new Formatter();
    fmt.format("%5.7s", "abcdefghijklmn");
    System.out.println(fmt);
    fmt = new Formatter();
    fmt.format("%5.7s", "abc");
    System.out.println(fmt);
  }
}
java title=Example.java
abcdefg
abc
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
