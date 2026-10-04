---
title: Determine the Day of the Week from Today's Date
nav: Determine the Day of the W...
description: The answer to this question is to use java.util.Calendar.SUNDAY, java.util.Calendar.MONDAY, and so on:
section: Imported - java2s Archive
order: 1126
source: https://web.archive.org/web/20140829090927/http://www.java2s.com/Tutorial/Java/0040__Data-Type/DeterminetheDayoftheWeekfromTodaysDate.htm
---
The answer to this question is to use java.util.Calendar.SUNDAY, java.util.Calendar.MONDAY, and so on:

```java title=Example.java
import java.text.ParseException;
public class MainClass {
  public static void main(String[] args) throws ParseException {
    java.util.Date today = new java.util.Date();
    java.sql.Date date = new java.sql.Date(today.getTime());
    java.util.GregorianCalendar cal = new java.util.GregorianCalendar();
    cal.setTime(date);
    System.out.println(cal.get(java.util.Calendar.DAY_OF_WEEK));
  }
}
```

| 2.38.1. | The java.util.Date Class |
|---|---|
| 2.38.2. | Show date and time using only Date methods. |
| 2.38.3. | Obtaining a Date Object From a String |
| 2.38.4. | Convert from a java.util.Date Object to a java.sql.Date Object |
| 2.38.5. | Convert a String Date Such as 2003/01/10 into a java.util.Date Object |
| 2.38.6. | Create Yesterday's Date from a Date in the String Format of MM/DD/YYYY |
| 2.38.7. | Create a java.util.Date Object from a Year, Month, Day Format |
| 2.38.8. | Create a java.sql.Time Object from java.util.Date |
| 2.38.9. | Convert the Current Time to a java.sql.Date Object |
| 2.38.10. | Convert Date into milliseconds example |
| 2.38.11. | Create java Date from specific time example |
| 2.38.12. | Determine the Day of the Week from Today's Date |
| 2.38.13. | ISO 8601 date parsing utility. |
| 2.38.14. | Parses a string representing a date by trying a variety of different parsers. |
| 2.38.15. | Perform date validations |
