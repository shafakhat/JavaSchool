---
title: Specifying a Minimum Field Width
nav: Specifying a Minimum Field...
description: Imported from the java2s.com archive: Specifying a Minimum Field Width
section: Imported - java2s Archive
order: 1485
source: https://web.archive.org/web/20140829091846/http://www.java2s.com/Tutorial/Java/0120__Development/SpecifyingaMinimumFieldWidth.htm
---
| An integer between the % sign and the format conversion code acts as a minimum field width specifier. |
|---|
| The default padding is done with spaces. |
| If you want to pad with 0's, place a 0 before the field width specifier. |
| For example, %05d will pad a number of less than five digits with 0's. |

```java title=Example.java
import java.util.Formatter;
public class MainClass {
  public static void main(String args[]) {
    Formatter fmt = new Formatter();
    fmt.format("%05d", 88);
    System.out.println(fmt);
  }
}
java title=Example.java
00088
```

| 6.7.1. | Specifying a Minimum Field Width |
|---|---|
| 6.7.2. | The minimum field width specifier by applying it to the %f conversion |
| 6.7.3. | To produce tables with the columns lining up |
| 6.7.4. | Format to 2 decimal places in a 16-character field |
| 6.7.5. | Displaying at most 15 characters in a string |
| 6.7.6. | Limit the number of decimal digits by specifying the precision |
