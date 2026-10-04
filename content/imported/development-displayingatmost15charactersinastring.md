---
title: Displaying at most 15 characters in a string
nav: Displaying at most 15 char...
description: Imported from the java2s.com archive: Displaying at most 15 characters in a string
section: Imported - java2s Archive
order: 1487
source: https://web.archive.org/web/20140829091751/http://www.java2s.com/Tutorial/Java/0120__Development/Displayingatmost15charactersinastring.htm
---
```java title=Example.java
import java.util.Formatter;
public class MainClass {
  public static void main(String args[]) {
    Formatter fmt = new Formatter();
    fmt = new Formatter();
    fmt.format("%.15s", "Formatting with Java is now easy.");
    System.out.println(fmt);
  }
}
java title=Example.java
Formatting with
```

| 6.7.1. | Specifying a Minimum Field Width |
|---|---|
| 6.7.2. | The minimum field width specifier by applying it to the %f conversion |
| 6.7.3. | To produce tables with the columns lining up |
| 6.7.4. | Format to 2 decimal places in a 16-character field |
| 6.7.5. | Displaying at most 15 characters in a string |
| 6.7.6. | Limit the number of decimal digits by specifying the precision |
