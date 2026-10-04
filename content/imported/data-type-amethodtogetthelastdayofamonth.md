---
title: A method to get the last day of a month
nav: A method to get the last d...
description: * The AusStage Utilities Package is free software: you can redistribute
section: Imported - java2s Archive
order: 1128
source: https://web.archive.org/web/20110722180212/http://www.java2s.com:80/Code/Java/Data-Type/Amethodtogetthelastdayofamonth.htm
---
A method to get the last day of a month

```java title=Example.java
/*
 * This file is part of the AusStage Utilities Package
 *
 * The AusStage Utilities Package is free software: you can redistribute
 * it and/or modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * The AusStage Utilities Package is distributed in the hope that it will
 * be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
 * of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with the AusStage Utilities Package.
 * If not, see <http://www.gnu.org/licenses/>.
*/
//package au.edu.ausstage.utils;
// import additional libraries
import java.util.GregorianCalendar;
import java.util.Calendar;
import java.text.DateFormat;
/**
 * A class of methods useful when processing dates in AusStage Services
 */
public class DateUtils {
  /**
   * A method to get the last day of a month
   *
   * @param year  the four digit year
   * @param month the two digit month
   *
   * @return      the last day of the specified month
   */
  public static String getLastDay(String year, String month) {
    // get a calendar object
    GregorianCalendar calendar = new GregorianCalendar();
    // convert the year and month to integers
    int yearInt = Integer.parseInt(year);
    int monthInt = Integer.parseInt(month);
    // adjust the month for a zero based index
    monthInt = monthInt - 1;
    // set the date of the calendar to the date provided
    calendar.set(yearInt, monthInt, 1);
    int dayInt = calendar.getActualMaximum(GregorianCalendar.DAY_OF_MONTH);
    return Integer.toString(dayInt);
  } // end getLastDay method
}
```

1.  Get the days difference
2.  Get the days passed from the specified date up to the date provided in the constructor
3.  Get the hours difference
4.  Get the minutes difference
5.  Get the seconds difference
6.  Adds a number of days to a date returning a new object.
7.  Adds a number of hours to a date returning a new object.
8.  Adds a number of milliseconds to a date returning a new object.
9.  Adds a number of minutes to a date returning a new object.
10.  Adds a number of months to a date returning a new object.
11.  Adds a number of seconds to a date returning a new object.
12.  Adds a number of weeks to a date returning a new object.
13.  Adds a number of years to a date returning a new object.
14.  Returns a Date set just to Noon, to the closest possible millisecond of the day.
15.  Returns a Date set to the first possible millisecond of the day, just after midnight.
16.  Returns a Date set to the first possible millisecond of the month, just after midnight.
17.  Returns a Date set to the last possible millisecond of the day, just before midnight.
18.  Returns a Date set to the last possible millisecond of the minute.
19.  Returns a Date set to the last possible millisecond of the month, just before midnight.
20.  Returns a java.sql.Timestamp equal to the current time
21.  Returns the number of days within the fragment.
22.  Returns the number of hours within the fragment.
23.  Returns the number of milliseconds within the fragment.
24.  Returns the number of minutes within the fragment.
25.  Returns the number of seconds within the fragment.
26.  Returns true if endDate is after startDate or if startDate equals endDate.
27.  Roll the days forward or backward
28.  Roll the java.sql.Date forward or backward
29.  Roll the java.util.Date forward or backward
30.  Roll the java.util.Time forward or backward
31.  Roll the years forward or backward
32.  Round this date, leaving the field specified as the most significant field.
33.  Checking date as String formatted by a date format
34.  Checks if a calendar date is after today and within a number of days in the future
35.  Checks if a calendar date is today
36.  Checks if a date is after today and within a number of days in the future
37.  Checks if the first calendar date is after the second calendar date ignoring time
38.  Checks if the first calendar date is before the second calendar date ignoring time
39.  Checks if the first date is after the second date ignoring time
40.  Checks if the first date is before the second date ignoring time
41.  Checks if two calendars represent the same day ignoring time
42.  Checks if two dates are on the same day ignoring time
43.  Checks the day, month and year are equal
44.  Checks the hour, minute and second are equal
45.  Make the date go forward of the specified amount of minutes
46.  Make the date go back of the specified amount of days
47.  Returns the maximum of two dates. A null date is treated as being less than any non-null date
48.  Utilities to working with dates java.util.Date
49.  Calculate Holidays
50.  Compare two dates
51.  Convert time in milliseconds into a display string of the form [h]h:mm[am  pm]
52.  convert a minute-of-week time to time of day as dd:dd [AM  PM]
53.  Convert a minute-of-week time to time of day as dd:dd (24 hour format)
54.  Convert passed time into an offset string
55.  convert date in milliseconds into the native format of the server - i.e. minute of the week
56.  Convert date in milliseconds into minute of the day
57.  Convert date in minute of the week format into millisecond format
58.  Convert milliseconds into the day of the week string
59.  Convert milliseconds into a short day of the week string
60.  Convert milliseconds into the month of the year string
61.  Convert time to a sliding window format
62.  Get age
63.  Get Next Monday
64.  Get next Sunday
65.  Get File system Path From Date
66.  Get today's date
67.  Get Month, Day of Month, year from a Date
68.  Get Age
69.  Get date of yesterday
70.  Get date of last week
71.  Get date of last month
72.  Utility for setting the time on a date.
73.  Get last Date of This Month
74.  General purpose date utilities.
75.  Get Last day from previous Month
76.  Get Local Epoch
