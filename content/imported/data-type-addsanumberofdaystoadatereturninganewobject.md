---
title: Adds a number of days to a date returning a new object.
nav: Adds a number of days to a...
description: Adds a number of days to a date returning a new object. : Date Calculation « Data Type « Java
section: Imported - java2s Archive
order: 1111
source: https://web.archive.org/web/20091030214224/http://www.java2s.com:80/Code/Java/Data-Type/Addsanumberofdaystoadatereturninganewobject.htm
---
Adds a number of days to a date returning a new object. : Date Calculation « Data Type « Java

```java title=Example.java
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
 * <p>A suite of utilities surrounding the use of the
 * {@link java.util.Calendar} and {@link java.util.Date} object.</p>
 *
 * <p>DateUtils contains a lot of common methods considering manipulations
 * of Dates or Calendars. Some methods require some extra explanation.
 * The truncate and round methods could be considered the Math.floor(),
 * Math.ceil() or Math.round versions for dates
 * This way date-fields will be ignored in bottom-up order.
 * As a complement to these methods we've introduced some fragment-methods.
 * With these methods the Date-fields will be ignored in top-down order.
 * Since a date without a year is not a valid date, you have to decide in what
 * kind of date-field you want your result, for instance milliseconds or days.
 * </p>
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
   * The original date object is unchanged.
   *
   * @param date  the date, not null
   * @param amount  the amount to add, may be negative
   * @return the new date object with the amount added
   * @throws IllegalArgumentException if the date is null
   */
  public static Date addDays(Date date, int amount) {
      return add(date, Calendar.DAY_OF_MONTH, amount);
  }
  //-----------------------------------------------------------------------
  /**
   * Adds to a date returning a new object.
   * The original date object is unchanged.
   *
   * @param date  the date, not null
   * @param calendarField  the calendar field to add to
   * @param amount  the amount to add, may be negative
   * @return the new date object with the amount added
   * @throws IllegalArgumentException if the date is null
   */
  private static Date add(Date date, int calendarField, int amount) {
      if (date == null) {
          throw new IllegalArgumentException("The date must not be null");
      }
      Calendar c = Calendar.getInstance();
      c.setTime(date);
      c.add(calendarField, amount);
      return c.getTime();
  }
}
```

1.  Get the days difference
---  ---
2.  Get the days passed from the specified date up to the date provided in the constructor
3.  Get the hours difference
4.  Get the minutes difference
5.  Get the seconds difference
6.  Adds a number of hours to a date returning a new object.
7.  Adds a number of milliseconds to a date returning a new object.
8.  Adds a number of minutes to a date returning a new object.
9.  Adds a number of months to a date returning a new object.
10.  Adds a number of seconds to a date returning a new object.
11.  Adds a number of weeks to a date returning a new object.
12.  Adds a number of years to a date returning a new object.
13.  Returns a Date set just to Noon, to the closest possible millisecond of the day.
14.  Returns a Date set to the first possible millisecond of the day, just after midnight.
15.  Returns a Date set to the first possible millisecond of the month, just after midnight.
16.  Returns a Date set to the last possible millisecond of the day, just before midnight.
17.  Returns a Date set to the last possible millisecond of the minute.
18.  Returns a Date set to the last possible millisecond of the month, just before midnight.
19.  Returns a java.sql.Timestamp equal to the current time
20.  Returns the number of days within the fragment.
21.  Returns the number of hours within the fragment.
22.  Returns the number of milliseconds within the fragment.
23.  Returns the number of minutes within the fragment.
24.  Returns the number of seconds within the fragment.
25.  Returns true if endDate is after startDate or if startDate equals endDate.
26.  Roll the days forward or backward
27.  Roll the java.sql.Date forward or backward
28.  Roll the java.util.Date forward or backward
29.  Roll the java.util.Time forward or backward
30.  Roll the years forward or backward
31.  Round this date, leaving the field specified as the most significant field.
32.  Checking date as String formatted by a date format
33.  Checks if a calendar date is after today and within a number of days in the future
34.  Checks if a calendar date is today
35.  Checks if a date is after today and within a number of days in the future
36.  Checks if the first calendar date is after the second calendar date ignoring time
37.  Checks if the first calendar date is before the second calendar date ignoring time
38.  Checks if the first date is after the second date ignoring time
39.  Checks if the first date is before the second date ignoring time
40.  Checks if two calendars represent the same day ignoring time
41.  Checks if two dates are on the same day ignoring time
42.  Checks the day, month and year are equal
43.  Checks the hour, minute and second are equal
44.  Make the date go forward of the specified amount of minutes
45.  Make the date go back of the specified amount of days
46.  Returns the maximum of two dates. A null date is treated as being less than any non-null date
47.  Utilities to working with dates java.util.Date
48.  Calculate Holidays
49.  Compare two dates
