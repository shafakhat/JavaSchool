---
title: Find the Difference Between Two Given Dates
nav: Find the Difference Betwee...
description: public static Date makeDate(String dateString) throws Exception {
section: Imported - java2s Archive
order: 1152
source: https://web.archive.org/web/20140217221634/http://www.java2s.com/Tutorial/Java/0040__Data-Type/FindtheDifferenceBetweenTwoGivenDates.htm
---
```java title=Example.java
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
public class MainClass {
  public static int diff(Date date1, Date date2) {
    Calendar c1 = Calendar.getInstance();
    Calendar c2 = Calendar.getInstance();
    c1.setTime(date1);
    c2.setTime(date2);
    int diffDay = 0;
    if (c1.before(c2)) {
      diffDay = countDiffDay(c1, c2);
    } else {
      diffDay = countDiffDay(c2, c1);
    }
    return diffDay;
  }
  public static void DateDiff(Date date1, Date date2) {
    int diffDay = diff(date1, date2);
    System.out.println("Different Day : " + diffDay);
  }
  public static int countDiffDay(Calendar c1, Calendar c2) {
    int returnInt = 0;
    while (!c1.after(c2)) {
      c1.add(Calendar.DAY_OF_MONTH, 1);
      returnInt++;
    }
    if (returnInt > 0) {
      returnInt = returnInt - 1;
    }
    return (returnInt);
  }
  public static Date makeDate(String dateString) throws Exception {
    SimpleDateFormat formatter = new SimpleDateFormat("MM/dd/yyyy");
    return formatter.parse(dateString);
  }
  public static void main(String argv[]) throws Exception {
    Calendar cc1 = Calendar.getInstance();
    Calendar cc2 = Calendar.getInstance();
    cc1.add(Calendar.DAY_OF_MONTH, 10);
    DateDiff(cc1.getTime(), cc2.getTime());
    java.util.Date d1 = makeDate("10/10/2000");
    java.util.Date d2 = makeDate("10/18/2000");
    DateDiff(d1, d2);
    java.util.Date d3 = makeDate("1/1/2000");
    java.util.Date d4 = makeDate("12/31/2000");
    int diff34 = diff(d3, d4);
    System.out.println("diff34=" + diff34);
  }
}
```

| 2.42.1. | Compare date time using after method of Java Calendar |
|---|---|
| 2.42.2. | Compare date time using before method of Java Calendar |
| 2.42.3. | Increment and Decrement a Date Using the Calendar Class |
| 2.42.4. | Increment and Decrement Months Using the Calendar Class |
| 2.42.5. | Add or substract days to current date using Java Calendar |
| 2.42.6. | Substract days from current date using Calendar.add method |
| 2.42.7. | Add hours to current date using Calendar.add method |
| 2.42.8. | Calendar adjust date automatically |
| 2.42.9. | Substract hours from current date using Calendar.add method |
| 2.42.10. | Add minutes to current date using Calendar.add method |
| 2.42.11. | Substract minutes from current date using Calendar.add method |
| 2.42.12. | Add months to current date using Calendar.add method |
| 2.42.13. | Substract months from current date using Calendar.add method |
| 2.42.14. | Add seconds to current date using Calendar.add method |
| 2.42.15. | Substract seconds from current time using Calendar.add method |
| 2.42.16. | Add week to current date using Calendar.add method |
| 2.42.17. | Substract week from current date |
| 2.42.18. | Add year to current date using Calendar.add method |
| 2.42.19. | Substract year from current date |
| 2.42.20. | Substract 30 days from the calendar |
| 2.42.21. | Add 10 months to the calendar |
| 2.42.22. | Substract 1 year from the calendar |
| 2.42.23. | If a date is after another date |
| 2.42.24. | If a date is before another date |
| 2.42.25. | Compute days between 2 dates |
| 2.42.26. | Calculate the age |
| 2.42.27. | Determining If a Year Is a Leap Year |
| 2.42.28. | Determining the Day-of-Week for a Particular Date |
| 2.42.29. | Add hours, minutes or seconds to a date |
| 2.42.30. | Find the Difference Between Two Given Dates |
| 2.42.31. | add another 12 hours and print out the date and time |
| 2.42.32. | subtract 4 hours from the time and print out the date and time |
| 2.42.33. | add 8 days to the current date and print out the date and time |
| 2.42.34. | Returns the number of days within the fragment. |
| 2.42.35. | Returns the number of hours within the fragment. |
| 2.42.36. | Returns the number of milliseconds within the fragment. |
| 2.42.37. | Returns the number of minutes within the fragment. |
| 2.42.38. | Returns the number of seconds within the fragment. |
| 2.42.39. | Returns a Date set just to Noon, to the closest possible millisecond of the day. |
| 2.42.40. | Returns a Date set to the last possible millisecond of the month, just before midnight. |
| 2.42.41. | Returns a Date set to the first possible millisecond of the month, just after midnight. |
| 2.42.42. | Returns a Date set to the last possible millisecond of the minute. |
| 2.42.43. | Returns a Date set to the last possible millisecond of the day, just before midnight. |
| 2.42.44. | Returns a Date set to the first possible millisecond of the day, just after midnight. |
| 2.42.45. | Returns true if endDate is after startDate or if startDate equals endDate. |
| 2.42.46. | Round this date, leaving the field specified as the most significant field. |
| 2.42.47. | Checks if two date objects represent the same instant in time |
| 2.42.48. | Checks if two calendar objects represent the same local time. |
| 2.42.49. | Checks if two date objects are on the same day ignoring time |
| 2.42.50. | Truncate this date(Calendar), leaving the field specified as the most significant field. |
| 2.42.51. | Truncate this date, leaving the field specified as the most significant field. |
| 2.42.52. | Days Till End Of Year |
| 2.42.53. | Convert day of year to day of month |
| 2.42.54. | Determine if an hour is between an interval |
