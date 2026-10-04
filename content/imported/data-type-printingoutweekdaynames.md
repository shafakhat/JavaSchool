---
title: Printing out weekday names
nav: Printing out weekday names
description: String[] weekdays = new DateFormatSymbols().getWeekdays(); // Get day names
section: Imported - java2s Archive
order: 1271
source: https://web.archive.org/web/20140829080321/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Printingoutweekdaynames.htm
---
```java title=Example.java
import java.text.DateFormatSymbols;
public class MainClass {
  public static void main(String[] args) {
    String[] weekdays = new DateFormatSymbols().getWeekdays(); // Get day names
    for(String s: weekdays){
      System.out.println(s);
    }
  }
}
java title=Example.java
Sunday
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
```

| 2.40.1. | Creating Gregorian Calendars |
|---|---|
| 2.40.2. | Specifying the locale(TimeZone) explicitly for Gregorian Calendar |
| 2.40.3. | Creating a Calendar object from a locale |
| 2.40.4. | Creating a Date Object for a Particular Date |
| 2.40.5. | Setting the Date and Time |
| 2.40.6. | Setting a GregorianCalendar object to a particular date |
| 2.40.7. | Integer constants for the third version of set() |
| 2.40.8. | Calendar.DAY_OF_WEEK |
| 2.40.9. | Set with GregorianCalendar.YEAR, MONTH and DATE |
| 2.40.10. | Getting Date and Time Information: get the day of the week |
| 2.40.11. | Using a switch statement on the values for day |
| 2.40.12. | Modifying Dates and Times: adding 14 to the year |
| 2.40.13. | To go into the past: making the second argument negative in the 'add' method |
| 2.40.14. | To increment or decrement a field of a calendar by 1 using the roll() method |
| 2.40.15. | Comparing Calendars |
| 2.40.16. | Displaying Date by weekday name |
| 2.40.17. | Printing out weekday names |
| 2.40.18. | Determine the day of the week |
