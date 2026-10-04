---
title: Check for a Leap Year
nav: Check for a Leap Year
description: public static void main(String[] args) throws ParseException {
section: Imported - java2s Archive
order: 1336
source: https://web.archive.org/web/20140616101721/http://www.java2s.com/Tutorial/Java/0040__Data-Type/CheckforaLeapYear.htm
---
```java title=Example.java
import java.text.ParseException;
public class MainClass {
  public static void main(String[] args) throws ParseException {
    System.out.println(isLeapYear(2000));
  }
  public static boolean isLeapYear(int year) {
    if (year < 0) {
      return false;
    }
    if (year % 400 == 0) {
      return true;
    } else if (year % 100 == 0) {
      return false;
    } else if (year % 4 == 0) {
      return true;
    } else {
      return false;
    }
  }
}
```

| 2.39.1. | The java.util.Calendar Class |
|---|---|
| 2.39.2. | Create instance of java.sql.Date from Calendar.getTimeInMillis() |
| 2.39.3. | Create a Date object using the Calendar class |
| 2.39.4. | Using the Calendar Class to Display Current Time in Different Time Zones |
| 2.39.5. | Get day of week |
| 2.39.6. | Display Day of Week using Java Calendar |
| 2.39.7. | Display Month of year using Java Calendar |
| 2.39.8. | Get current date, year and month |
| 2.39.9. | Get current time information |
| 2.39.10. | Get the last date of a month |
| 2.39.11. | Get the last day of a month |
| 2.39.12. | Display full date time |
| 2.39.13. | Get time in milliseconds using Java Calendar |
| 2.39.14. | Get Week of month and year using Java Calendar |
| 2.39.15. | Construct a Calendar object by using the setTime method |
| 2.39.16. | To obtain a date part, such as the hour, the month, or the year, use the get method |
| 2.39.17. | To change a date/time component, use its set method: public void set (int field, int value) |
| 2.39.18. | Change multiple components at the same time |
| 2.39.19. | Check for a Leap Year |
| 2.39.20. | Checking for a Leap Year: using GregorianCalendar |
| 2.39.21. | Get Days Of The Week for different locale |
| 2.39.22. | Get the number of days in that month |
| 2.39.23. | Try month in a leap year |
