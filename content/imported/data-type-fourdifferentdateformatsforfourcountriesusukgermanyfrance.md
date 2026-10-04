---
title: Four different date formats for four countries
nav: Four different date format...
description: System.out.println("\nThe Date for " + locale.getDisplayCountry() + ":");
section: Imported - java2s Archive
order: 1178
source: https://web.archive.org/web/2018/http://www.java2s.com/Tutorial/Java/0040__Data-Type/FourdifferentdateformatsforfourcountriesUSUKGERMANYFRANCE.htm
---
```java title=Example.java
import static java.text.DateFormat.FULL;
import static java.text.DateFormat.LONG;
import static java.text.DateFormat.MEDIUM;
import static java.text.DateFormat.SHORT;
import static java.util.Locale.FRANCE;
import static java.util.Locale.GERMANY;
import static java.util.Locale.UK;
import static java.util.Locale.US;
import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;
public class MainClass {
  public static void main(String[] args) {
    Date today = new Date();
    Locale[] locales = { US, UK, GERMANY, FRANCE };
    int[] styles = { FULL, LONG, MEDIUM, SHORT };
    String[] styleNames = { "FULL", "LONG", "MEDIUM", "SHORT" };
    DateFormat fmt = null;
    for (Locale locale : locales) {
      System.out.println("\nThe Date for " + locale.getDisplayCountry() + ":");
      for (int i = 0; i < styles.length; i++) {
        fmt = DateFormat.getDateInstance(styles[i], locale);
        System.out.println("\tIn " + styleNames[i] + " is " + fmt.format(today));
      }
    }
  }
}
java title=Example.java
The Date for United States:
  In FULL is Tuesday, January 16, 2007
  In LONG is January 16, 2007
  In MEDIUM is Jan 16, 2007
  In SHORT is 1/16/07
The Date for United Kingdom:
  In FULL is 16 January 2007
  In LONG is 16 January 2007
  In MEDIUM is 16-Jan-2007
  In SHORT is 16/01/07
The Date for Germany:
  In FULL is Dienstag, 16. Januar 2007
  In LONG is 16. Januar 2007
  In MEDIUM is 16.01.2007
  In SHORT is 16.01.07
The Date for France:
  In FULL is mardi 16 janvier 2007
  In LONG is 16 janvier 2007
  In MEDIUM is 16 janv. 2007
  In SHORT is 16/01/07
```

| 2.41.1. | Date Parsing and Formatting with DateFormat |
|---|---|
| 2.41.2. | Parsing the Time Using a Custom Format |
| 2.41.3. | Parse with a custom format |
| 2.41.4. | Parse with a default format |
| 2.41.5. | Parse string date value input with SimpleDateFormat('dd-MMM-yy') |
| 2.41.6. | Parse a date and time |
| 2.41.7. | Parse string date value input with SimpleDateFormat('E, dd MMM yyyy HH:mm:ss Z') |
| 2.41.8. | Parse string date value with default format: DateFormat.getDateInstance(DateFormat.DEFAULT) |
| 2.41.9. | Leniency |
| 2.41.10. | Formatting String Symbols for SimpleDateFormat |
| 2.41.11. | SimpleDateFormat: hh:mm:ss, dd MMM yyyy hh:mm:ss zzz, E MMM dd yyyy |
| 2.41.12. | Simply format a date as YYYYMMDD |
| 2.41.13. | Express a duration in term of HH:MM:SS |
| 2.41.14. | Date Format with SimpleDateFormat |
| 2.41.15. | Demonstrate date formats with different DateFormat constants |
| 2.41.16. | Demonstrate time formats. |
| 2.41.17. | DateFormat.getDateTimeInstance(DateFormat.FULL,DateFormat.MEDIUM) |
| 2.41.18. | print out the current date and time |
| 2.41.19. | Date Era change |
| 2.41.20. | Format Date with System.out.format |
| 2.41.21. | SimpleDateFormat |
| 2.41.22. | Formatting Dates and Times |
| 2.41.23. | Four different date formats for four countries: US, UK, GERMANY, FRANCE |
| 2.41.24. | Various Date format |
| 2.41.25. | Display date with day name in a short format |
| 2.41.26. | Display date with a short day and month name |
| 2.41.27. | Format a date into dd/mm/yyyy |
| 2.41.28. | Format current date and time with the SimpleDateFormat: dd/MM/yyyy |
| 2.41.29. | Format current date and time with the SimpleDateFormat: HH:mm:ss |
| 2.41.30. | Formatting Symbols for SimpleDateFormat |
| 2.41.31. | Formatting the Time Using a Custom Format |
| 2.41.32. | Change date formatting symbols |
| 2.41.33. | Get a List of Short Month Names |
| 2.41.34. | Get a List of Weekday Names |
| 2.41.35. | Get a List of Short Weekday Names |
| 2.41.36. | Time in 12-hour format |
| 2.41.37. | Time in 24-hour format |
| 2.41.38. | Date and time with month |
| 2.41.39. | Date and time with day and month fully spelled-out |
| 2.41.40. | Output current time: %tc |
| 2.41.41. | Formatter that caches formatted date information |
| 2.41.42. | RFC date format |
| 2.41.43. | A formatter that formats dates to show the elapsed time relative to some base date. |
