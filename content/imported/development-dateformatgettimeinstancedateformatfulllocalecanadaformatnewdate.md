---
title: DateFormat.getTimeInstance(DateFormat.FULL, Locale.CANADA).format(new Date())
nav: DateFormat.getTimeInstance...
description: String s = DateFormat.getTimeInstance(DateFormat.FULL, Locale.CANADA).format(new Date());
section: Imported - java2s Archive
order: 1663
source: https://web.archive.org/web/2016/http://www.java2s.com/Tutorial/Java/0120__Development/DateFormatgetTimeInstanceDateFormatFULLLocaleCANADAformatnewDate.htm
---
```java title=Example.java
import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;
public class Main {
  public static void main(String[] argv) throws Exception {
    String s = DateFormat.getTimeInstance(DateFormat.FULL, Locale.CANADA).format(new Date());
    System.out.println(s);
  }
}
```

| 6.13.1. | Formatting and Parsing a Time for a Locale Using Default Formats |
|---|---|
| 6.13.2. | DateFormat.getTimeInstance(DateFormat.MEDIUM, Locale.CANADA).format(new Date()) |
| 6.13.3. | DateFormat.getTimeInstance(DateFormat.LONG, Locale.CANADA).format(new Date()) |
| 6.13.4. | DateFormat.getTimeInstance(DateFormat.FULL, Locale.CANADA).format(new Date()) |
| 6.13.5. | DateFormat.getTimeInstance(DateFormat.DEFAULT, Locale.CANADA).format(new Date()) |
| 6.13.6. | Parse date string input with DateFormat.getTimeInstance(DateFormat.DEFAULT, Locale.CANADA) |
| 6.13.7. | Formatting and Parsing a Time for a Locale: specify the locale when creating the SimpleDateFormat object. |
| 6.13.8. | Format with a default format |
| 6.13.9. | Convert string date to long value |
| 6.13.10. | Format a date-time value:short, medium and long |
| 6.13.11. | Convert Date to String |
| 6.13.12. | Validate a date Using DateFormat |
| 6.13.13. | Format date in Default format |
| 6.13.14. | Format date in Full format |
| 6.13.15. | Format date in Long format |
| 6.13.16. | Format date in Medium format |
| 6.13.17. | Find the current date format |
| 6.13.18. | DateFormat.SHORT |
