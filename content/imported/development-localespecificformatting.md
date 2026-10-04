---
title: locale-specific formatting.
nav: locale-specific formatting.
description: Imported from the java2s.com archive: locale-specific formatting.
section: Imported - java2s Archive
order: 1198
source: https://web.archive.org/web/20140829080822/http://www.java2s.com/Tutorial/Java/0120__Development/localespecificformatting.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.Formatter;
import java.util.Locale;
public class Main {
  public static void main(String args[]) {
    Formatter fmt = new Formatter();
    Calendar cal = Calendar.getInstance();
    fmt = new Formatter();
    fmt.format("Default locale: %tc\n", cal);
    fmt.format(Locale.GERMAN, "For Locale.GERMAN: %tc\n", cal);
    fmt.format(Locale.ITALY, "For Locale.ITALY: %tc\n", cal);
    fmt.format(Locale.FRANCE, "For Locale.FRANCE: %tc\n", cal);
    System.out.println(fmt);
  }
}
```

| 6.4.1. | Write formatted output directly to the console and to a file. |
|---|---|
| 6.4.2. | Formatter.ioException() |
| 6.4.3. | new Formatter(new OutputStream('test.fmt')) |
| 6.4.4. | locale-specific formatting. |
