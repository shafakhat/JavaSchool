---
title: %tc
nav: %tc
description: Imported from the java2s.com archive: %tc
section: Imported - java2s Archive
order: 1510
source: https://web.archive.org/web/2014/http://www.java2s.com/Tutorial/Java/0120__Development/tcDisplaycompletetimeanddateinformation.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.Formatter;
public class MainClass {
  public static void main(String args[]) {
    Formatter fmt = new Formatter();
    // .
    fmt = new Formatter();
    fmt.format("%tc", Calendar.getInstance());
    System.out.println(fmt);
  }
}
java title=Example.java
Fri Dec 01 08:58:44 PST 2006
```

| 6.9.1. | Formatting Time and Date: The Time and Date Format Suffixes |
|---|---|
| 6.9.2. | %tr: Formatting time and date |
| 6.9.3. | %tc: Display complete time and date information |
| 6.9.4. | %tl:%tM: Display just hour and minute |
| 6.9.5. | %tB %tb %tm: Display month by name and number |
| 6.9.6. | Display 12-hour time format |
| 6.9.7. | Display 24-hour time format. |
| 6.9.8. | Display short date format. |
| 6.9.9. | Display date using full names. |
| 6.9.10. | Display complete time and date information: using %T rather than %t. |
| 6.9.11. | Display hour and minute, and include AM or PM indicator. |
| 6.9.12. | The Time and Date Format Suffixes |
| 6.9.13. | Display several time and date formats |
