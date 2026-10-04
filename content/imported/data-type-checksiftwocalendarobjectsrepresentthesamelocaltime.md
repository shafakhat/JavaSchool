---
title: Checks if two calendar objects represent the same local time.
nav: Checks if two calendar obj...
description: * Licensed to the Apache Software Foundation (ASF) under one or more
section: Imported - java2s Archive
order: 1349
source: https://web.archive.org/web/20140417231716/http://www.java2s.com/Tutorial/Java/0040__Data-Type/Checksiftwocalendarobjectsrepresentthesamelocaltime.htm
---
```java title=Example.java
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.Calendar;
import java.util.Date;
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
  //-----------------------------------------------------------------------
  /**
   *
   * This method compares the values of the fields of the two objects.
   * In addition, both calendars must be the same of the same type.
   *
   * @param cal1  the first calendar, not altered, not null
   * @param cal2  the second calendar, not altered, not null
   * @return true if they represent the same millisecond instant
   * @throws IllegalArgumentException if either date is <code>null</code>
   * @since 2.1
   */
  public static boolean isSameLocalTime(Calendar cal1, Calendar cal2) {
      if (cal1 == null || cal2 == null) {
          throw new IllegalArgumentException("The date must not be null");
      }
      return (cal1.get(Calendar.MILLISECOND) == cal2.get(Calendar.MILLISECOND) &&
              cal1.get(Calendar.SECOND) == cal2.get(Calendar.SECOND) &&
              cal1.get(Calendar.MINUTE) == cal2.get(Calendar.MINUTE) &&
              cal1.get(Calendar.HOUR) == cal2.get(Calendar.HOUR) &&
              cal1.get(Calendar.DAY_OF_YEAR) == cal2.get(Calendar.DAY_OF_YEAR) &&
              cal1.get(Calendar.YEAR) == cal2.get(Calendar.YEAR) &&
              cal1.get(Calendar.ERA) == cal2.get(Calendar.ERA) &&
              cal1.getClass() == cal2.getClass());
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
