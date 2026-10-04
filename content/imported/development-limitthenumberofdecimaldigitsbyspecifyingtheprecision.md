---
title: Limit the number of decimal digits by specifying the precision
nav: Limit the number of decima...
description: Imported from the java2s.com archive: Limit the number of decimal digits by specifying the precision
section: Imported - java2s Archive
order: 1488
source: https://web.archive.org/web/20140829092104/http://www.java2s.com/Tutorial/Java/0120__Development/Limitthenumberofdecimaldigitsbyspecifyingtheprecision.htm
---
```java title=Example.java
import java.util.Formatter;
public class Main {
  public static void main(String[] argv) throws Exception {
    Formatter fmt = new Formatter();
    fmt.format("Default precision: %f\n", 10.0 / 3.0);
    fmt.format("Two decimal digits: %.2f\n\n", 10.0 / 3.0);
    System.out.println(fmt);
  }
}
```

| 6.7.1. | Specifying a Minimum Field Width |
|---|---|
| 6.7.2. | The minimum field width specifier by applying it to the %f conversion |
| 6.7.3. | To produce tables with the columns lining up |
| 6.7.4. | Format to 2 decimal places in a 16-character field |
| 6.7.5. | Displaying at most 15 characters in a string |
| 6.7.6. | Limit the number of decimal digits by specifying the precision |
