---
title: Returns the number of days within the fragment.
nav: Returns the number of days...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1296
source: https://web.archive.org/web/20140418011059/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Returnsthenumberofdayswithinthefragment.htm
---
```java title=Example.java
import java.util.Calendar;
import java.util.Date;
import java.util.Iterator;
import java.util.TimeZone;
/**
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * A suite of utilities surrounding the use of the
 * {@link java.util.Calendar} and {@link java.util.Date} object.
 *
 * DateUtils contains a lot of common methods considering manipulations
 * of Dates or Calendars. Some methods require some extra explanation.
 * The truncate and round methods could be considered the Math.floor(),
 * Math.ceil() or Math.round versions for dates
 * This way date-fields will be ignored in bottom-up order.
 * As a complement to these methods we've introduced some fragment-methods.
 * With these methods the Date-fields will be ignored in top-down order.
 * Since a date without a year is not a valid date, you have to decide in what
 * kind of date-field you want your result, for instance milliseconds or days.
 *
 *
 *
 *
 * @author <a href="mailto:sergek@lokitech.com">Serge Knystautas</a>
 * @author Stephen Colebourne
 * @author Janek Bogucki
 * @author <a href="mailto:ggregory@seagullsw.com">Gary Gregory</a>
 * @author Phil Steitz
 * @author Robert Scholte
 * @since 2.0
 * @version $Id: DateUtils.java 634096 2008-03-06 00:58:11Z niallp $
 */
public class Main {
  /**
   * The UTC time zone  (often referred to as GMT).
   */
  public static final TimeZone UTC_TIME_ZONE = TimeZone.getTimeZone("GMT");
  /**
   * Number of milliseconds in a standard second.
   * @since 2.1
   */
  public static final long MILLIS_PER_SECOND = 1000;
  /**
   * Number of milliseconds in a standard minute.
   * @since 2.1
   */
  public static final long MILLIS_PER_MINUTE = 60 * MILLIS_PER_SECOND;
  /**
   * Number of milliseconds in a standard hour.
   * @since 2.1
   */
  public static final long MILLIS_PER_HOUR = 60 * MILLIS_PER_MINUTE;
  /**
   * Number of milliseconds in a standard day.
   * @since 2.1
   */
  public static final long MILLIS_PER_DAY = 24 * MILLIS_PER_HOUR;
  /**
   * This is half a month, so this represents whether a date is in the top
   * or bottom half of the month.
   */
  public final static int SEMI_MONTH = 1001;
  private static final int[][] fields = {
          {Calendar.MILLISECOND},
          {Calendar.SECOND},
          {Calendar.MINUTE},
          {Calendar.HOUR_OF_DAY, Calendar.HOUR},
          {Calendar.DATE, Calendar.DAY_OF_MONTH, Calendar.AM_PM
              /* Calendar.DAY_OF_YEAR, Calendar.DAY_OF_WEEK, Calendar.DAY_OF_WEEK_IN_MONTH */
          },
          {Calendar.MONTH, DateUtils.SEMI_MONTH},
          {Calendar.YEAR},
          {Calendar.ERA}};
  /**
   * A week range, starting on Sunday.
   */
  public final static int RANGE_WEEK_SUNDAY = 1;
  /**
   * A week range, starting on Monday.
   */
  public final static int RANGE_WEEK_MONDAY = 2;
  /**
   * A week range, starting on the day focused.
   */
  public final static int RANGE_WEEK_RELATIVE = 3;
  /**
   * A week range, centered around the day focused.
   */
  public final static int RANGE_WEEK_CENTER = 4;
  /**
   * A month range, the week starting on Sunday.
   */
  public final static int RANGE_MONTH_SUNDAY = 5;
  /**
   * A month range, the week starting on Monday.
   */
  public final static int RANGE_MONTH_MONDAY = 6;
  /**
   * Returns the number of days within the
   * fragment. All datefields greater than the fragment will be ignored.
   *
   * Asking the days of any date will only return the number of days
   * of the current month (resulting in a number between 1 and 31). This
   * method will retrieve the number of days for any fragment.
   * For example, if you want to calculate the number of days past this year,
   * your fragment is Calendar.YEAR. The result will be all days of the
   * past month(s).
   *
   * Valid fragments are: Calendar.YEAR, Calendar.MONTH, both
   * Calendar.DAY_OF_YEAR and Calendar.DATE, Calendar.HOUR_OF_DAY,
   * Calendar.MINUTE, Calendar.SECOND and Calendar.MILLISECOND
   * A fragment less than or equal to a DAY field will return 0.
   *
   *
   * <ul>
   *  <li>January 28, 2008 with Calendar.MONTH as fragment will return 28
   *   (equivalent to calendar.get(Calendar.DAY_OF_MONTH))</li>
   *  <li>February 28, 2008 with Calendar.MONTH as fragment will return 28
   *   (equivalent to calendar.get(Calendar.DAY_OF_MONTH))</li>
   *  <li>January 28, 2008 with Calendar.YEAR as fragment will return 28
   *   (equivalent to calendar.get(Calendar.DAY_OF_YEAR))</li>
   *  <li>February 28, 2008 with Calendar.YEAR as fragment will return 59
   *   (equivalent to calendar.get(Calendar.DAY_OF_YEAR))</li>
   *  <li>January 28, 2008 with Calendar.MILLISECOND as fragment will return 0
   *   (a millisecond cannot be split in days)</li>
   * </ul>
   *
   *
   * @param calendar the calendar to work with, not null
   * @param fragment the Calendar field part of calendar to calculate
   * @return number of days within the fragment of date
   * @throws IllegalArgumentException if the date is <code>null</code> or
   * fragment is not supported
   * @since 2.4
   */
  public static long getFragmentInDays(Calendar calendar, int fragment) {
      return getFragment(calendar, fragment, Calendar.DAY_OF_YEAR);
  }
  /**
   * Date-version for fragment-calculation in any unit
   *
   * @param date the date to work with, not null
   * @param fragment the Calendar field part of date to calculate
   * @param unit Calendar field defining the unit
   * @return number of units within the fragment of the date
   * @throws IllegalArgumentException if the date is <code>null</code> or
   * fragment is not supported
   * @since 2.4
   */
  private static long getFragment(Date date, int fragment, int unit) {
      if(date == null) {
          throw  new IllegalArgumentException("The date must not be null");
      }
      Calendar calendar = Calendar.getInstance();
      calendar.setTime(date);
      return getFragment(calendar, fragment, unit);
  }
  /**
   * Calendar-version for fragment-calculation in any unit
   *
   * @param calendar the calendar to work with, not null
   * @param fragment the Calendar field part of calendar to calculate
   * @param unit Calendar field defining the unit
   * @return number of units within the fragment of the calendar
   * @throws IllegalArgumentException if the date is <code>null</code> or
   * fragment is not supported
   * @since 2.4
   */
  private static long getFragment(Calendar calendar, int fragment, int unit) {
      if(calendar == null) {
          throw  new IllegalArgumentException("The date must not be null");
      }
      long millisPerUnit = getMillisPerUnit(unit);
      long result = 0;
      // Fragments bigger than a day require a breakdown to days
      switch (fragment) {
          case Calendar.YEAR:
              result += (calendar.get(Calendar.DAY_OF_YEAR) * MILLIS_PER_DAY) / millisPerUnit;
              break;
          case Calendar.MONTH:
              result += (calendar.get(Calendar.DAY_OF_MONTH) * MILLIS_PER_DAY) / millisPerUnit;
              break;
      }
      switch (fragment) {
          // Number of days already calculated for these cases
          case Calendar.YEAR:
          case Calendar.MONTH:
          // The rest of the valid cases
          case Calendar.DAY_OF_YEAR:
          case Calendar.DATE:
              result += (calendar.get(Calendar.HOUR_OF_DAY) * MILLIS_PER_HOUR) / millisPerUnit;
          case Calendar.HOUR_OF_DAY:
              result += (calendar.get(Calendar.MINUTE) * MILLIS_PER_MINUTE) / millisPerUnit;
          case Calendar.MINUTE:
              result += (calendar.get(Calendar.SECOND) * MILLIS_PER_SECOND) / millisPerUnit;
          case Calendar.SECOND:
              result += (calendar.get(Calendar.MILLISECOND) * 1) / millisPerUnit;
              break;
          case Calendar.MILLISECOND: break;//never useful
              default: throw new IllegalArgumentException("The fragment " + fragment + " is not supported");
      }
      return result;
  }
  /**
   * Returns the number of millis of a datefield, if this is a constant value
   *
   * @param unit A Calendar field which is a valid unit for a fragment
   * @return number of millis
   * @throws IllegalArgumentException if date can't be represented in millisenconds
   * @since 2.4
   */
  private static long getMillisPerUnit(int unit) {
      long result = Long.MAX_VALUE;
      switch (unit) {
          case Calendar.DAY_OF_YEAR:
          case Calendar.DATE:
              result = MILLIS_PER_DAY;
              break;
          case Calendar.HOUR_OF_DAY:
              result = MILLIS_PER_HOUR;
              break;
          case Calendar.MINUTE:
              result = MILLIS_PER_MINUTE;
              break;
          case Calendar.SECOND:
              result = MILLIS_PER_SECOND;
              break;
          case Calendar.MILLISECOND:
              result = 1;
              break;
          default: throw new IllegalArgumentException("The unit " + unit + " cannot be represented is milleseconds");
      }
      return result;
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
