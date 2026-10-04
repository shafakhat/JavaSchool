---
title: Display date using full names.
nav: Display date using full na...
description: Imported from the java2s.com archive: Display date using full names.
section: Imported - java2s Archive
order: 1501
source: https://web.archive.org/web/20140829090818/http://www.java2s.com/Tutorial/Java/0120__Development/Displaydateusingfullnames.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.Formatter;
public class Main {
  public static void main(String[] argv) throws Exception {
    Formatter fmt = new Formatter();
    Calendar cal = Calendar.getInstance();
    fmt.format("Long date format: ");
    fmt.format("%tA %1$tB %1$td, %1$tY\n", cal);
    System.out.println(fmt);
  }
}
//Long date format: Monday March 09, 2009
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
